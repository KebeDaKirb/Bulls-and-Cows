# save this as app.py
from flask import Flask, render_template, request, session, redirect
from bulls_and_cows import guess_calc, ANS_LENGTH, MAX_GUESS
import random

app = Flask(__name__)
app.secret_key = "super_secret"
app.config["SECRET_KEY"] = "super_secret"


@app.route("/", methods=["GET", "POST"])
def bulls_and_cows():
    feedback = ""
    guess = []
    if "secret" not in session:
        session["secret"] = random.sample(range(1, 10), 4)
        session["count"] = 1
        session["history"] = []
        session["playing"] = True
    history = session["history"]

    if not session["playing"]:
        return render_template(
            "index.html",
            feedback="Your game is over. Please Reset",
            guess=guess,
            history=history,
        )

    print(session["secret"])
    print(session["history"])
    if request.method == "POST":
        form_values = request.form.to_dict()
        user_guess = form_values["user_guess"]
        guess, error_feedback = guess_calc(user_guess)
        if not guess:
            return render_template(
                "index.html",
                feedback=error_feedback,
                guess=guess,
                history=history,
            )
        bulls = 0
        cows = 0
        for x in range(ANS_LENGTH):
            if guess[x] == session["secret"][x]:
                bulls += 1
            elif guess[x] in session["secret"]:
                cows += 1
        history.append(f"{guess} -> Cows: {cows}\nBulls: {bulls}")
        session["history"] = history
        session["count"] += 1
        if bulls == ANS_LENGTH:
            session["playing"] = False
            return render_template(
                "index.html", feedback="You Win!", guess=guess, history=history
            )
        if session["count"] > MAX_GUESS:
            session["playing"] = False
            return render_template(
                "index.html", feedback="You Lose!", guess=guess, history=history
            )
    return render_template(
        "index.html", feedback=feedback, guess=guess, history=history
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
