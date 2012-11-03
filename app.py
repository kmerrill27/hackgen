from flask import Flask, render_template, url_for
import random
app = Flask(__name__)

@app.route("/")
def show_random():
    vals = RandomValues()
    return render_template('index.html', vals=vals)

class RandomValues:
    def __init__(self):
        # Brand Name
        self.name = "HackGen"

        # Get the theme to be used
        self.theme = self.getTheme()

        # Get the buttons to be in the left and right of the navbar
        buttons = ['About', 'Register', 'Support', 'Blog', 'Contact Us', 'Sign in']
        i = random.randint(1,len(buttons))
        j = random.randint(i,len(buttons))
        k = random.randint(j,len(buttons))

        self.leftButtons = [self.name]
        self.leftButtons.extend(buttons[:i])
        self.rightButtons = buttons[j:k]

        self.searchBar = randBool()

    def getTheme(self):
        return 'theme' + str(random.randint(1,11)) + '.css'


def randBool():
    return bool(random.getrandbits(1))

if __name__ == "__main__":
    app.run(debug=True)
