EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'Je',
        'eat': 'mange', 'drink': 'bois', 'John': 'Jean', 'friends': 'amis',
        'and': 'et', 'of': 'du', 'red': 'rough'}
FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I',
        'mange': 'eat', 'bois': 'drink', 'Jean': 'John', 'amis': 'friends',
        'et': 'and', 'du': 'of', 'rough': 'red'}
dicts = {'English to French': EtoF, 'French to English': FtoE}


def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


def translate(phrase, dicts, direction):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '.,;:?'
    letters = UC_letters + LC_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        elif word != '':
            if c in punctuation:
                c = c + ' '
            translation = (translation +
                           translate_word(word, dictionary) + c)
            word = ''
    return f'{translation} {translate_word(word, dictionary)}'


print(translate('I drink good red wine, and eat bread.', dicts,
                'English to French'))
print(translate('Je bois du vin rough.', dicts,
                'French to English'))
