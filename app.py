from flask import Flask, render_template, redirect, flash
from password_generator import passgen
from forms import PassLength

app = Flask(__name__)
app.config["SECRET_KEY"] = "development"


@app.route('/')
def home():
    return render_template("home.html", title="Home Page", name="Home")


@app.route('/pass_gen/', methods=["GET", "POST"])
def pass_gen():
    form = PassLength()
    if form.validate_on_submit():
        flash(passgen(form.password_length.data))
        return redirect("/pass_gen")
    return render_template("pass_gen.html", title="Password Generator", form=form)


#if __name__ == '__main__':
#    app.run()
