import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5434/test_db7'
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)

    def __init__(self, name, months):
        self.name = name
        self.terms = [
            Term(months=months)
        ]

class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    months = db.Column(db.String(32), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref=db.backref('terms', lazy=True))

@app.route('/', methods=['GET'])
def hello():
    return flask.render_template('index.html', companies=Company.query.all())

@app.route('/add_message', methods=['POST'])
def add_message():
    company = flask.request.form['company']
    months = flask.request.form['months']

    db.session.add(Company(company, months))
    db.session.commit()

    return flask.redirect(flask.url_for('hello'))

with app.app_context():
    db.create_all()

app.run()
