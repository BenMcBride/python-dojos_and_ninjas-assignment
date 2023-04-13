from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    # change 'ninjas' to the table_name and 'Ninja' to the Class_name
    dojos = Dojo.get_all()
    # change all_ninjas to be the list of what you're 'getting all of'
    return render_template("index.html", all_dojos = dojos)

@app.route('/dojo/new')
def new_dojo():
    return render_template("add_dojo.html")


@app.route('/create_dojo', methods=["POST"]) # change /create_dojo to match the form action in the HTML
def create_dojo():
    #change "fname, lname" etc to match the form inputs in the HTML
    data = {
        "name": request.form["name"],
    }
    # We pass the data dictionary into the save method from the dojo class.
    Dojo.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/show/<int:id>')
def show(id):
    # calling the get_one method from table_name.py
    # change 'dojo_id' and 'Dojo' class to be the id of the table/class you're using
    ninjas = Ninja.get_all(id)
    dojo = Dojo.get_one(id)
    # it's currently setup to render a show_dojo.html that includes the variable 'dojo'
    return render_template("show_dojo.html", dojo = dojo, all_ninjas = ninjas)