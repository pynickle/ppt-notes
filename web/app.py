from flask import Flask, render_template, request, send_file, redirect
from werkzeug import secure_filename

from src import produce_pptx

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def post():
    if 'file' not in request.files:
        flash('未上传文件！')
        return redirect("/")
    file = request.files['file']
    if file.filename == '':
        flash('未上传文件！')
        return redirect("/")
    file.save("notes.txt")
    produce_pptx()
    return redirect("/file")

@app.route("/file")
def file():
    return render_template("file.html")

@app.route("/download")
def download():
    return send_file("res.pptx", as_attachment=True)

if __name__ == "__main__":
    app.run(port=1234)