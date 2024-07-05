from flask import Flask, render_template, request, jsonify
from models import db, connectdb, Cupcake
import requests
"""Flask app for Cupcakes"""

app = Flask(__name__)

app.config["SECRET_KEY"] = "CUPCAKE123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake_db"
app.config["SQLALCHEMY_ECHO"] = True


app.app_context().push()
connectdb(app)
db.create_all()

@app.route("/cupcakes")
def show_cupcakes():
    """Lists cupcakes"""
    cakes = Cupcake.query.all()
    return render_template("cake_index.html", cakes=cakes)

@app.route("/api/cupcakes")
def list_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_new_cupcakes():
    new_cake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cake)
    db.session.commit()
    return  (jsonify(new_cake= new_cake.serialize()), 201)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="DELETED")