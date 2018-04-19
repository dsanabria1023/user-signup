from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def signup_index():
    return render_template('signup.html', title="Signup")

@app.route("/signup", methods=["POST"])
def validate():
    username = str(request.form["username"])
    password = str(request.form["password"])
    verify = str(request.form["verify"])
    email = str(request.form["email"])

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if not username:
        username_error = "Please enter a username"
    elif len(username) < 3:
        username_error = "Username is too short"
    elif len(username) > 20:
        username_error = "Username is too long"
    else:
        for char in username:
            if char == " ":
                username_error = "That is not a vaild username"

    if not password:
        password_error = "Please enter a password"
    elif len(password) < 3:
        password_error = "Password is too short"
    elif len(password) > 20:
        password_error = "Password is too long"
    else:
        for char in password:
            if char == " ":
                password_error = "That is not a vaild password"

    if verify != password:
        verify_error = "Passwords do not match"

    if not email:
        if not username_error and not password_error and not verify_error and not email_error:
            return render_template("welcome.html", title="Welcome", 
            username=username)
    elif len(email) < 3:
        email_error = "Email is too short"
    elif len(email) > 20:
        email_error = "Email is too long"
    else:
        for char in email:
            if char == " ":
                email_error = "That is not a vaild email"
            elif "@" not in email:
                email_error = "That is not a vaild email"
            elif "." not in email:
                email_error = "That is not a vaild email"
            elif email.count(".") > 1:
                email_error = "That is not a vaild email"

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/welcome")
    else:
        return render_template("signup.html", title="Signup", 
        username_error=username_error, password_error=password_error,
        verify_error=verify_error, email_error=email_error)

@app.route('/welcome', methods=['POST'])
def welcome_index():
    username = request.form["username"]

    return render_template("welcome.html", title="Welcome", username=username)

app.run()