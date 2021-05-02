from flask import Flask, redirect, url_for, render_template, request
from beverages import menu
from utils import get_items_from_request, calculate_price

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/store")
def drinks():
    return render_template("store.html", menu=menu)


@app.route("/order", methods=["POST"])
def orders():
    items = get_items_from_request(request.form, menu)
    total = calculate_price(items)
    return render_template("order.html", items=items, total=total)


if __name__ == "__main__":
    app.run(debug=True)
