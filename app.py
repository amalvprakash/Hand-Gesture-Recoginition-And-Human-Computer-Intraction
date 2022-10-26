from flask import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mediaplayer')
def mediaplayer():
    import vlctest
    return vlctest


@app.route('/mouse')
def mouse():
    import AIVirtualMouseProject
    return AIVirtualMouseProject


if __name__ == '__main__':
    app.run()