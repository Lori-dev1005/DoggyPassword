import sys

from flask import Flask, render_template, request

from password_generator import PasswordGenerator
from password_validator import PasswordValidator


app = Flask(__name__, template_folder=".", static_folder="../static")


@app.route("/", methods=["GET", "POST"])
def index():
    length = 12
    password = ""
    error = ""

    if request.method == "POST":
        try:
            length = int(request.form.get("length", ""))
        except ValueError:
            error = "Enter a whole-number password length."
        else:
            if not PasswordGenerator.MIN_LENGTH <= length <= PasswordGenerator.MAX_LENGTH:
                error = (
                    f"Choose a length from {PasswordGenerator.MIN_LENGTH} "
                    f"to {PasswordGenerator.MAX_LENGTH}."
                )
            else:
                password = PasswordGenerator(length).generate()

    password_is_valid = bool(password) and PasswordValidator(password).is_valid()
    return render_template(
        "password.html",
        password=password,
        length=length,
        error=error,
        password_is_valid=password_is_valid,
    )


if __name__ == "__main__" and "--console" in sys.argv[1:]:
    length = int(input("Enter Length: "))
    password = PasswordGenerator(length).generate()
    print("Your random password is: ", password)
elif __name__ == "__main__":
    app.run(debug=True)
