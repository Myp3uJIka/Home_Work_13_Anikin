from flask import Flask, request, render_template, send_from_directory
import os
from functions import read_json, get_tags, find_tag
# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', tags_list=get_tags(read_json(POST_PATH)))


@app.route("/post_by_tag.html")
def page_tag():
    tag = request.args.get('tag')
    return render_template('post_by_tag.html', content=find_tag(tag, read_json(POST_PATH)))


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)

