x = 'abcdefghijklmnopqrstuvwxyz'
def pangrams(sen):
    if x not in sen:
        print('Not a Pangram')
    else:
        print('Pangram')
pangrams('The quick brown fox jumps over the lazy dog')