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

        self.navTop = randBool()

        # Get the buttons to be in the left and right of the navbar
        buttons = ['Documentation', 'Press', 'API', 'Developers', 'Pricing', 'About', 'Register', 'Support', 'Blog', 'Contact Us', 'Sign in']
        numButtons = random.randint(0,6)

        if self.navTop:
            buttonsChosen = random.sample(buttons, numButtons)

            i = random.randint(0,numButtons)
            j = random.randint(i,numButtons)
            self.leftButtons = [self.name]
            self.leftButtons.extend(list(buttonsChosen)[:i])
            self.rightButtons = list(buttonsChosen)[i:j]
        else:
            self.buttons = list(random.sample(buttons, numButtons))

        self.searchBar = randBool()

        bottomButtons = ['Contact', 'Copyright', 'Privacy', 'Roadmap', 'Sitemap', 'Changes', 'Jobs', 'Status']
        self.bottomButtons = random.sample(bottomButtons, random.randint(1,len(bottomButtons)))

    def getTheme(self):
        return 'theme' + str(random.randint(1,11)) + '.css'


def randBool():
    return bool(random.getrandbits(1))

if __name__ == "__main__":
    app.run(debug=True)
