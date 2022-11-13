from flask import Flask, render_template, request
import get_meme
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name","World"))


@app.route('/meme', methods=["POST"])
def meme_func():
    meme_pic, subreddit = get_meme.get_meme()
    return render_template("show_meme.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ =="__main__":
    app.run(port=PORT)
