from random import choice

words = {'noun': ['hacker', 'user', 'manager', 'tweeter', 'newbie', 'pro', 'guru'],
        'adjective': ['open-source', 'scalable', 'really awesome', 'cloud-based', 'Web 3.0',
                        'professional', 'resilient', 'incredibly exciting', 'robust',
                        'long-awaited', 'agile'],
        'verb': ['code', 'conference', 'learn', 'network', 'connect',
                    'design', 'collaborate', 'synchronize'],
        'time': ['seconds', 'hours', 'minutes'],
        'startup': ['twitter', 'GitHub', 'reddit', 'facebook', 'weather.com', 'Quora',
                        'Square', 'Amazon', 'BuzzFeed', 'mongoDB', 'Python', 'Java',
                        '4chan', 'digg', 'jQuery', 'Ruby', 'Perl', 'Haskel'],
        'adverb': ['efficiently', 'quickly', 'perfectly', 'reliably'],
        'verbing': ['coding', 'socializing', 'networking', 'playing', 'working', 'developing'],
        'number': ['a hundred', 'three hundred', '10,000'],
        'firstName': ['Buzz', 'Cloud', 'My', 'Face', 'Git', 'Micro', 'Server',
                        'Hacker', 'Dr', 'Scale', 'Ghost', 'Fire', 'Agile'],
        'secondName': ['Feed', 'Book', 'Hub', '.js', 'DB', 'Flare', 'Connect',
                        'Py', 'Star', 'News', 'Bucket', 'Clound', 'Combinator'],
        'app': ['app', 'script', 'database', 'game', 'software', 'product'],
        'feature': ['aggregator', 'news feed', 'search engine', 'database',
                    'interpreter', 'ticker', 'algorithm', 'architecture'],
        'comparative': ['better', 'faster', 'cleaner', 'easier', 'smarter'],
        'superlative': ['quickest', 'easiest', 'fastest', 'cleanest', 'smartest'],
        'badNoun': ['limitations', 'a typo', 'connectivity', 'compatibility']
        }

blurb = '{name} is a {adjective1}, {adjective2} way for {noun}s to get {verbing} in {time}.'

paragraph = ('{name} is like {startup1} crossed with {startup2}. Within '
        '{time}, you\'ll have your {app} running {adverb}. Better yet, our '
        'built-in {feature} makes {verbing1} {comparative} than ever. '
         'With over {number} {noun}s {verbing2} on {name} daily, you\'ll never '
         'to worry about {badNoun} again.')
slogan = '{name}. The {superlative} way to {verb}.'

snippets = [('By {noun}s, for {noun}s', '{name} was made with {verbing} in mind.'),
            ('{comparative} than {startup}', '{name} aims to have the {superlative} {feature} out there.'),
            ('{verb} in {time}', 'We at {name} know that being {adjective1} doesn\'t mean sacrificing {adjective2} software.')]

chosen = list()

def get(string):
    word = choice(words[string])
    while word in chosen:
        word = choice(words[string])
    chosen.append(word)
    return word

def getWords():
    words = {'name': (get('firstName') + get('secondName')),
            'adjective1': get('adjective'),
            'adjective2': get('adjective'),
            'noun': get('noun'),
            'verbing': get('verbing'),
            'time': get('time'),
            'feature': get('feature'),
            'comparative': get('comparative'),
            'verbing1': get('verbing'),
            'verbing2': get('verbing'),
            'verb': get('verb'),
            'startup': get('startup'),
            'startup1': get('startup'),
            'startup2': get('startup'),
            'superlative': get('superlative'),
            'app': get('app'),
            'adverb': get('adverb'),
            'number': get('number'),
            'badNoun': get('badNoun')
            }
    global chosen
    del chosen[:]
    return words

def getData():
    words = getWords()

    # We gotta do some formatting on the snippets
    newSnippets = list()
    for title, buzz in snippets:
        newSnippets.append((title.format(**words).title(), buzz.format(**words)))

    return {'name': words['name'],
            'blurb': blurb.format(**words),
            'paragraph': paragraph.format(**words),
            'slogan': slogan.format(**words),
            'snippets': newSnippets}
