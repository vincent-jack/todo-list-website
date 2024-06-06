from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import pandas
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired, URL, Length
import os

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

df = pandas.read_csv("instance/task-data.csv")


class AddTaskForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(max=100)],
                       render_kw={"class": "form-control border border-secondary border-3"})


@app.route("/", methods=['GET', 'POST'])
def home():
    add_form = AddTaskForm()
    if add_form.validate_on_submit():
        text = add_form.name.data
        df.loc[len(df.index)] = {"name": text, "complete": False}
        df.to_csv("instance/task-data.csv", index=False)

    return render_template("index.html", tasks=df, add_form=add_form)


if __name__ == "__main__":
    app.run(debug=True)
