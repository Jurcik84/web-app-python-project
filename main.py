from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.temp.html')


@app.route("/pacient-stories")
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


@app.route("/pacient-story")
def pacient_story():
    return render_template('pacient-story.temp.html')


@app.route("/about-us")
def about_us():
    return render_template('about-us.temp.html')


@app.route("/about-doctors")
def about_doctors():
    return render_template('home.temp.html')


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
