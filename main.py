from flask import Flask, render_template
import requests

app = Flask(__name__)
data = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Who knew that cacti lived such interesting lives.",
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
    },
    {
        "id": 2,
        "title": "Top 15 Things to do When You are Bored",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
    },
    {
        "id": 3,
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Learn about the newest health craze.",
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
    },
]


@app.route("/")
def index():
    # data = requests.get(url="https://api.npoint.io/5bde7be30288fb5212b2").json()
    return render_template("index.html", datas=data)


@app.route("/about")
def page_about():
    return render_template("about.html")


@app.route("/contact")
def page_contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def make_post(index):
    index -= 1
    # response = requests.get(url="https://api.npoint.io/5bde7be30288fb5212b2")
    # data = response.json()[id-1]
    return render_template("post.html", post=data[index])


if __name__ == "__main__":
    app.run(debug=True)
