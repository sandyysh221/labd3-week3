from flask import render_template

from app import app
from models.tobuy_list import *


@app.route("/")
def index():
    return render_template("index.html", title="Home", orders=orders)


@app.route("/orders/<index>")
def order_index(index):
    order = orders[int(index)]
    return render_template("order.html", title="Home", order=order)
