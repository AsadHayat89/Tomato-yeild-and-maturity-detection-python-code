import flask
import werkzeug
import time
import os
from fireaseupload import *
app = flask.Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d")
        
        path = "testinmges/"+timestr
        print(path)
        isFile = os.path.exists(path)
        print(isFile)
        if isFile==False:
            os.mkdir("testinmges/"+timestr)
        timestr2 = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save("testinmges/"+timestr+"/"+timestr2+'_'+filename)
        image_num = image_num + 1
    print("\n")
    y=uploadToFirebase()
    print(y)
    if y:
        return "Image(s) Uploaded Successfully. Come Back Soon."
    else:
        return "Not Uploaded"
@app.route('/')
def index():
    print("asdfd")
    return "render_template('index.html')"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)