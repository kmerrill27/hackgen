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
        # Get the theme to be used
        self.theme = self.getTheme()

        # Should our logo be on the left?
        self.logoLeft = bool(random.getrandbits(1))

        # Get the buttons to be in the left and right of the navbar
        buttons = ['About', 'Register', 'Support', 'Blog', 'Contact Us', 'Sign in']
        i = random.randint(1,len(buttons))
        j = random.randint(i,len(buttons))
        k = random.randint(j,len(buttons))
        self.leftButtons = buttons[:i]
        self.rightButtons = buttons[j:k]

    def getTheme(self):
        return 'theme' + random.randint(1,11) + '.css'

if __name__ == "__main__":
    app.run()
