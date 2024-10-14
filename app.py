from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/projects/")
def projects():
    return render_template('projects.html')

@app.route("/resume/")
def resume():
    return render_template('resume.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/form/")
def form():
    return render_template('form.html')

@app.route('/form/complete', methods=['GET', 'POST'])
def complete():
    return render_template('complete.html')