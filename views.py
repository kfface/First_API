from First_API import app

@app.route('/')
def index():
    return render_template('checkout.html!')