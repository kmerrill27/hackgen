from flask import (
    Flask,
    render_template)
app = Flask(__name__)

@app.route("/")
def show_random():
    vals = RandomValues()
    return render_template('index.html', vals=vals)

class RandomValues:
    def __init__(self):
        self.first = 1
        self.second = 2

if __name__ == "__main__":
    app.run()
