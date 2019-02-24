import generate_blog
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return generate_blog.generate_post()
