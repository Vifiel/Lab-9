from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask("Telephone book")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    phone = db.Column(db.String(10))

    def __repr__(self):
        return f'{self.id}............{self.phone}'

@app.route("/add", methods=["POST"])
def add_contact():
    data = request.json
    product = Contact(**data)
    db.session.add(product)
    db.session.commit()
    return "Ok"

@app.route("/clear", methods=["GET"])
def clear():
    db.drop_all()
    with app.app_context():
        db.create_all()
    return "Ok"

@app.route("/")
def main():
    contacts = Contact.query.all()
    return render_template("index.html", contacts_list=contacts)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
