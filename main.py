from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import pandas
import os

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

df = pandas.read_csv("instance/task-data.csv")


@app.route("/", methods=['GET', 'POST'])
def home():
    if "add" in request.form:
        text = request.form.get("task-name")
        df.loc[len(df.index)] = {"name": text, "complete": False}
        df.to_csv("instance/task-data.csv", index=False)

    return render_template("index.html", tasks=df)


if __name__ == "__main__":
    app.run(debug=True)
