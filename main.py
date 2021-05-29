from flask import Flask, render_template,url_for,request,redirect
from db_functions import add_content,get_content_name,get_content_post


app = Flask(__name__,
    template_folder='templates'
    )

@app.route('/')
def index():
    
    name = get_content_name()
    post = get_content_post()
    count=len(name)
    return render_template('index.html', name=name, post=post, count=count)

@app.route('/add', methods=["POST"])
def add():
    content_name = request.form["post_name"]
    content_post = request.form["post_item"]
    add_content(content_name,content_post)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
