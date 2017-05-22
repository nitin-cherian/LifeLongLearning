# poetry.py

"""
Write a script poetry.py that will generate a poem based on randomly chosen words and
a pre-determined structure. When you are done, you will be able to generate poetic
masterpieces such as the following in mere milliseconds:

A furry horse
A furry horse curdles within the fragrant mango
extravagantly, the horse slurps
the mango meows beneath a balding extrovert

All of the poems will have this same general structure, inspired by Clifford Pickover:
{A/An} {adjective1} {noun1}
{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {preposition2} a {adjective3} {noun3}

Your script should include a function makePoem() that returns a multi-line string
representing a complete poem. The main section of the code should simply print
makePoem() to display a single poem. In order to get there, use the following steps as a
guide:

1. First, you'll need a vocabulary from which to create the poem. Create several lists,
each containing words pertaining to one part of speech (more or less); i.e., create
separate lists for nouns, verbs, adjectives, adverbs, and prepositions. You will need
to include at least three different nouns, three verbs, three adjectives, two
prepositions and one adverb. You can use the sample word lists below, but feel free
to add your own:
Nouns: "fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert",
"gorilla"
Verbs: "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"
Adjectives: "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"
Prepositions: "against", "after", "into", "beneath", "upon", "for", "in", "like", "over",
"within"
Adverbs: "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"

2. Choose random words from the appropriate list using the random.choice() function,
storing each choice in a new string. Select three nouns, three verbs, three
adjectives, one adverb, and two prepositions. Make sure that none of the words are
repeated. (Hint: Use a while loop to repeat the selection process until you get a new
word.)

3. Plug the words you selected into the structure above to create a poem string by
using the format() string method

4. Bonus: Make sure that the "A" in the title and the first line is adjusted to become an
"An" automatically if the first adjective begins with a vowel.
"""
import random


NOUNS = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
VERBS = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
ADJECTIVES = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
PREPOSITIONS = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
ADVERBS = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]


def get_words(part, num):
    """
    For a given part of speech, return a list of num unique words.
    :param part: part of speech
    :param num: number of words in the part of speech to be returned
    :return: list of words
    """

    if num > len(part):
        raise ValueError('Too many words asked than available for part {}'.format(part))

    nouns = [random.choice(part) for n in range(num)]

    while len(set(nouns)) != num:
        nouns = [random.choice(part) for n in range(num)]

    return nouns


def make_poem():
    """
    Prints a poem from randomly generated words
    :return: A poem of randomly generated words
    """

    noun1, noun2, noun3 = get_words(NOUNS, 3)
    verb1, verb2, verb3 = get_words(VERBS, 3)
    adjective1, adjective2, adjective3 = get_words(ADJECTIVES, 3)
    preposition1, preposition2 = get_words(PREPOSITIONS, 2)
    adverb1, = get_words(ADVERBS, 1)

    return """
    A {adjective1} {noun1}
    
    A {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
    {adverb1}, the {noun1} {verb2}
    the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
    """.format(noun1=noun1, noun2=noun2, noun3=noun3,
               verb1=verb1, verb2=verb2, verb3=verb3,
               adjective1=adjective1, adjective2=adjective2, adjective3=adjective3,
               preposition1=preposition1, preposition2=preposition2,
               adverb1=adverb1)


def main():
    print(make_poem())

if __name__ == '__main__':
    main()
