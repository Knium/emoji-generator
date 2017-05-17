import argparse

parser = argparse.ArgumentParser(description='Generating Emoji for Suit')

parser.add_argument('-n', '--name',
    type=str, help='Name of Img, if it is not given, Emoji sentence will be it.')
parser.add_argument('-s', '--sentence',
    type=str, help='Sentence of emoji image you wanna generate.')
parser.add_argument('-e', '--extension',
    type=str, help='Extention of Image, you can use \'jpeg\', \'png\' ... ')
parser.add_argument('-c', '--color', type=str,
    help='Color of Emoji. Choose one from [R, G, B]'
)

args = parser.parse_args()
