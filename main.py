from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

url_list = ["/poskodeny-metacrillom", "/mudr-ivana-nemeckova-metacrill-praha", "/mudr-zavadilova-vybulkova-metacrill-praha"]


###############################################
#          Render HOME PAGE                   #
###############################################

@app.route("/", methods=["GET"])
def index():
    return render_template('home.temp.html')

###############################################
#          Render NEMECKOVA                   #
###############################################

@app.route(url_list[1], methods=["GET"])
def mudr_ivana_nemackova():
    return render_template('nemeckova.temp.html')


###############################################
#          Render Zavadilova                  #
###############################################

@app.route(url_list[2], methods=["GET"])
def mudr_vybulkova_zavadilova():
    return render_template('zavadilova.temp.html')


###############################################
#          Render Poskodeny metacrillom       #
###############################################

@app.route("/poskodeny-metacrillom", methods=["GET"])
def poskodeny_metacrillom():
    return render_template('poskodeny-metacrillom.temp.html')






###############################################
#          Render PACIENT STORIES             #
###############################################

@app.route("/pacient-stories", methods=["GET"])
def pacient_stories():
    pacient_stories = [{
        "title": "Juraj story",
        "subtitle": "Juraj damanges by doc nemeckova",
        "path": "/juraj-story",
        "image": "https://preview.redd.it/lrzvbgyuu8241.jpg?width=960&crop=smart&auto=webp&s=b2f8fc23b1f5fd733e82c312d35a3831a9f188cf"
    }, {
        "title": "Jana story",
        "subtitle": "Juraj damanges by doc nemeckova",
        "path": "/jana-story",
          "image": "https://preview.redd.it/lrzvbgyuu8241.jpg?width=960&crop=smart&auto=webp&s=b2f8fc23b1f5fd733e82c312d35a3831a9f188cf"
    }, {
        "title": "Brona story",
          "subtitle": "Juraj damanges by doc nemeckova",
        "path": "/brona-story",
          "image": "https://preview.redd.it/lrzvbgyuu8241.jpg?width=960&crop=smart&auto=webp&s=b2f8fc23b1f5fd733e82c312d35a3831a9f188cf"
    }, {
        "title": "Peter story",
         "subtitle": "Juraj damanges by doc nemeckova",
        "path": "peter-story",
          "image": "https://preview.redd.it/lrzvbgyuu8241.jpg?width=960&crop=smart&auto=webp&s=b2f8fc23b1f5fd733e82c312d35a3831a9f188cf"
    }, {
        "title": "Katka story",
         "subtitle": "Juraj damanges by doc nemeckova",
        "path": "katka-story",
          "image": "https://preview.redd.it/lrzvbgyuu8241.jpg?width=960&crop=smart&auto=webp&s=b2f8fc23b1f5fd733e82c312d35a3831a9f188cf"
    }]

    return render_template('pacient-stories.temp.html', data=pacient_stories)

###############################################
#          Render HOME PAGE                   #
###############################################

@app.route("/pacient-story", methods=["GET"])
def pacient_story():
    return render_template('pacient-story.temp.html')


###############################################
#          Render ABOUT US                    #
###############################################

@app.route("/about-us")
def about_us():
    return render_template('about-us.temp.html', methods=["GET"])

###############################################
#          Render About Doctores                 #
###############################################

@app.route("/about-doctors")
def about_doctors():
    return render_template('home.temp.html', methods=["GET"])


if __name__ == "__main__":
    app.run(port=5000, debug=True)


# Example:

# $ export FLASK_APP=main.py
# $ export FLASK_ENV=development
# $ flask run
# or in one command:

# $ FLASK_APP=main.py FLASK_ENV=development flask run
# If you want different port than the default (5000) add --port option.

# Example:

# $ FLASK_APP=main.py FLASK_ENV=development flask run --port 8080
# More options are available with:

# $ flask run --help
