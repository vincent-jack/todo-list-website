from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import pandas
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

df = pandas.read_csv("instance/task-data.csv")


class AddTaskForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(max=100)],
                       render_kw={"class": "form-control border border-secondary border-3"})
    submit = SubmitField("Add New Task",
                         render_kw={"class": "btn btn-secondary", "style": "padding-left: 8%; padding-right: 8%;"})



class DeleteCompletedForm(FlaskForm):
    submit = SubmitField("Delete Completed Tasks",
                         render_kw={"class": "nav-link text-white"})


@app.route("/", methods=['GET', 'POST'])
def home():
    global df
    add_form = AddTaskForm()
    delete_form = DeleteCompletedForm()

    return render_template("index.html", tasks=df, add_form=add_form, delete_form=delete_form)


@app.route('/adddata', methods=['POST'])
def add_data():
    global df
    if request.method == "POST":
        text = request.form["name"]
        if text.strip() != "":
            df.loc[len(df.index)] = {"name": text, "complete": False}
            df.to_csv("instance/task-data.csv", index=False)
    return redirect(url_for("home"))


@app.route('/deletedata', methods=['POST'])
def delete_data():
    global df
    if request.method == "POST":
        df = df[df.complete != True]
        df.to_csv("instance/task-data.csv", index=False)
    return redirect(url_for("home"))


@app.route('/updatedata', methods=['POST'])
def update_data():
    index = int(request.form.get('row'))
    checked = False
    if request.form.get('checked') == "true":
        checked = True
    df.loc[index, "complete"] = checked
    df.to_csv("instance/task-data.csv", index=False)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
