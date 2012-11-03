from flask import (
    Flask,
    render_template)
import random
app = Flask(__name__)

@app.route("/")
def show_random():
    vals = RandomValues()
    return render_template('index.html', vals=vals)

class RandomValues:
    def __init__(self):
        self.theme = getTheme

    def getTheme(self):
        return 'theme' + random.randint(1,11) + '.css'

if __name__ == "__main__":
    app.run()
