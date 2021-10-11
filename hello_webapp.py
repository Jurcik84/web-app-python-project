from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.temp.html')



@app.route("/pacient-stories")
def pacient_stories():
     return render_template('pacient-stories.temp.html')
    

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
