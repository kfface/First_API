from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)
app = Flask(__name__)

@app.route("/")
def checkout():
    return render_template("checkout.html")