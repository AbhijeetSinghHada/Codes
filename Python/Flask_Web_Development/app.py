from flask import Flask, render_template, request, redirect, url_for
from helper import Database
from utils.databaseConnection import DatabaseConnection

app = Flask(__name__)

a = Database()
posts = a.import_web_data


@app.route('/post/<int:post_id>')  # /post/0
def post(post_id):
    post = posts.get(post_id)
    if not post:  # post will be None if not found
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')

    return render_template('post.jinja2', post=post)

# 127.0.0.1:5000/post/create?title=dthrd&content=something


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        a = Database()
        a.upload_data(post_id, title, content)
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')


@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
