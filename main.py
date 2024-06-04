from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean, create_engine
import os


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
Bootstrap5(app)

db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
