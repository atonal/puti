import generate_blog
import putisplain
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/putify")
def hello():
    title, paragraphs= generate_blog.generate_post()
    return render_template('putify.html', title=title, paragraphs=paragraphs)

@app.route("/putisplain")
def splain():
    name = putisplain.generate_name()
    return render_template('putisplain.html', name=name)
