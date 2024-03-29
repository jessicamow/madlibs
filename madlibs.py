"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Show game or say goodbye depending on user response."""

    response = request.args.get("game-response")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route("/madlib", methods=["POST", "GET"])
def show_madlib():
    """Display the madlib"""

    if request.method == "GET":
        
        return render_template("genericmadlib.html")

    else: 
        
        ALLERGIES = []

        person = request.form.get("person")
        color = request.form.get("color")
        noun = request.form.get("noun")
        adjective = request.form.get("adjective")

        allergy0 = request.form.get("allergy0")

        if allergy0 != None: 
            ALLERGIES.append(allergy0)

        allergy1 = request.form.get("allergy1")

        if allergy1 != None: 
            ALLERGIES.append(allergy1)

        allergy2 = request.form.get("allergy2")
        
        if allergy2 != None: 
            ALLERGIES.append(allergy2)
        

        return render_template("madlib.html", 
                                person=person,
                                color=color,
                                noun=noun,
                                adjective=adjective,
                                allergies=ALLERGIES)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
