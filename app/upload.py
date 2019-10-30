from flask import request, redirect, render_template
from werkzeug.utils import secure_filename
from app import app

import os

app.config["IMAGE_UPLOADS"] = app.instance_path +  "/uploaded"
#app.config["IMAGE_UPLOADS"] = "/opt/app-root/src"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPG"]
app.config["MAX_IMAGE_FILESIZE"] = 30 *  1024 *  1024 #20Kb

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    print(ext.upper() == app.config["ALLOWED_IMAGE_EXTENSIONS"])

    if ext.upper() == app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    print("start upload")
    print(request.method )

    if request.method == "POST":
       image = request.files["image"]
       filename = secure_filename(image.filename)
       image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
       print("Image saved")
                

    return render_template("upload_image.html")