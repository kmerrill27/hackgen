from flask import Flask, render_template, url_for
from os import listdir
from os.path import isdir
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
        buttons = ['Documentation', 'Press', 'API', 'Developers', 'Pricing', 'About', 'Register', 'Support', 'Blog', 'Contact Us', 'Sign in']
        numButtons = random.randint(2,6)

        buttonsChosen = random.sample(buttons, numButtons)

        i = random.randint(0,numButtons)
        j = random.randint(i,numButtons)
        self.leftButtons = [self.name]
        self.leftButtons.extend(list(buttonsChosen)[:i])
        self.rightButtons = list(buttonsChosen)[i:j]

        self.searchBar = randBool()

        bottomButtons = ['Contact', 'Copyright', 'Privacy', 'Roadmap', 'Sitemap', 'Changes', 'Jobs', 'Status']
        self.bottomButtons = random.sample(bottomButtons, random.randint(2,4))

        self.feature3 = True
        if self.feature3:# randBool(): # build 3 feature
            self.generate3feature()

    def generate3feature(self):
        base_path = "static/img/feature3"
        img_group = random.choice(listdir("static/img/feature3"))
        imgs = map(lambda x: "static/img/feature3/" + img_group + "/" + x, listdir(base_path + "/" + img_group))
        random.shuffle(imgs)
        self.feature3s = []
        for i in range(3):
            self.feature3s.append(Feature(imgs[i], "tagline", "some text"))

    def getTheme(self):
        return 'theme' + str(random.randint(1,8)) + '.css'


class Feature():
    def __init__(self, img, tagline, text):
        self.img = img
        self.tagline = tagline
        self.text = text

def randBool():
    return bool(random.getrandbits(1))

if __name__ == "__main__":
    app.run(debug=True)
