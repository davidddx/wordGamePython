import random

wordDictionary = {
    "english": "language",
    "kangaroo": "animal",
    "super mario bros": "video game",
}

def getword():
    keys = wordDictionary.keys();
    keys = list(keys);
    word = random.choice(keys);
    return word;


def game(word):
    print('Welcome. This is a word guessing game.');
    print('\n');
    category = wordDictionary[word];
    GuessesLeft = 6;
    CorrectLettersGuessed = [];
    WrongLettersGuessed = [];

    if ' ' in word:
        CorrectLettersGuessed.append(' ');

    while True:
        print("Category: ", category);


        playerhaswon = True;

        for letter in word:
            if letter in CorrectLettersGuessed:
                print(letter, end=' ');
            else:
                print('_', end=' ');
                playerhaswon = False;
        print('\n');

        if playerhaswon:  # winner
            break;

        print('wrong letters guessed: ', end=' ');
        for letter in WrongLettersGuessed:
            print(letter, end=' ');

        print('\n');

        print('Guesses Left: ', GuessesLeft);

        letterguessed = input('Guess a lowercase letter by typing it in and pressing enter: ');

        if letterguessed in word:
            CorrectLettersGuessed.append(letterguessed);
        else:
            WrongLettersGuessed.append(letterguessed);
            GuessesLeft = GuessesLeft - 1;

        if GuessesLeft == 0:
            break;

        # end of while loop

    print('\n');
    if playerhaswon:
        print('Congratulations! You have won');
    else:
        print('Sorry. You have lost. The word was: ', word);
    print('\n');
    print('Thank you for playing.')


if __name__ == '__main__':
    word = getword();
    game(word);

