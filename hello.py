import json
import requests
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        return render_template("checkout.html")
    else:
        if request.method == 'POST':
            street = request.form['street_address']
            city = request.form['city']
            state = request.form['state']
            postcode = request.form['postcode']
            address = street + ", " + city + ", " + state + " " + postcode
            address = address.replace(" ", "+")
            website = "https://www.google.com/maps/place/"
            website += address 
            print(website)
            return redirect(url_for('/'))

