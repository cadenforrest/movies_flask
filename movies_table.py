from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    year = db.Column(db.Integer, index=True)
    cast = db.PickleType()
    genres = db.PickleType()

    def to_dict(self):
      return{
        'title': self.title,
        'year': self.year,
        'cast': self.cast,
        'genres': self.genres
      }

db.create_all()

@app.route('/')
def index():
    return render_template('table.html', title='Movies')

@app.route('/api/data')
def data():
    query = Movie.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Movie.name.like(f'%{search}%'),
            Movie.email.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['name', 'age', 'email']:
            col_name = 'name'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Movie, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [Movie.to_dict() for Movie in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Movie.query.count(),
        'draw': request.args.get('draw', type=int),
    }


if __name__ == '__main__':
    app.run(debug=True)

