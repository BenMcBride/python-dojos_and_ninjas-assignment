from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja/new')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", all_dojos = dojos)


@app.route('/create_ninja', methods=["POST"]) # change /create_ninja to match the form action in the HTML
def create_ninja():
    #change "fname, lname" etc to match the form inputs in the HTML
    data = {
        "dojo_id": request.form["dojo"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"]
    }
    # We pass the data dictionary into the save method from the ninja class.
    Ninja.save(data)
    address = f'/show/{request.form["dojo"]}'
    # Don't forget to redirect after saving to the database.
    return redirect(address)