import generate_blog
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/putify")
def hello():
    title, paragraphs= generate_blog.generate_post()
    return render_template('putify.html', title=title, paragraphs=paragraphs)
