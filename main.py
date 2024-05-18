from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tree.db"
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String[20])
    lname = db.Column(db.String[20])
    sfx = db.Column(db.String[10])
    g = db.Column(db.String[1])
    by = db.Column(db.Integer)
    dy = db.Column(db.Integer)
    f = db.Column(db.Integer)
    m = db.Column(db.Integer)

    def __init__(self, fname, lname, sfx, g, by, dy, f, m):
        self.fname = fname
        self.lname = lname
        self.sfx = sfx
        self.g = g
        self.by = by
        self.dy = dy
        self.f = f
        self.m = m


with app.app_context():
    db.create_all()


@app.route("/addperson", methods=["POST"])
def add_person():
    fname = request.form["fname"]
    lname = request.form["lname"]
    sfx = request.form["sfx"]
    g = request.form["g"]
    by = request.form["by"]
    dy = request.form["dy"]
    f = request.form["f"]
    m = request.form["m"]
    person = Person(fname, lname, sfx, g, by, dy, f, m)
    db.session.add(person)
    db.session.commit()
    return {"success": "person added"}


@app.route("/getperson/<int:id>")
def get_person(id):
    person = Person.query.get(id)
    if person:
        return jsonify({
            "fname": person.fname,
            "lname": person.lname,
            "sfx": person.sfx,
            "g": person.g,
            "by": person.by,
            "dy": person.dy,
            "f": person.f,
            "m": person.m
        })
    else:
        return {"error": "Person not found"}


@app.route("/test")
def test():
    return "I am the very model of a modern Roman emperor"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
