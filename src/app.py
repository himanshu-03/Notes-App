from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/insert', methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  
            notes.append(note)
            return redirect(url_for('display'))
    return render_template("insert.html")


@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.remove(note)
            return redirect(url_for('display'))
    return render_template("delete.html", notes=notes)

@app.route('/display')
def display():
    return render_template("display.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
