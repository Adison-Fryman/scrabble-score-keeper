letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
command = ''
# combining the two lists 'letters' and 'points' into one dictionary.
point_per_letter = dict(zip(letters, points))


# test line
# print(point_per_letter['A'])

def word_points(word):
    points = 0
    for letter in word.upper():
        if letter.upper() not in letters:
            print(letter + ' is not in the alphabet')
        else:
            points += point_per_letter[letter]
    return points


# test the above function
# print(word_points('broWnie')) should give 15

def calc_score():
    for player, word_list in current_game.items():
        current_score = 0
        for word in word_list:
            current_score += word_points(word)
            current_scores[player] = current_score

def scores_check():
    try:
        high_score = max(current_scores, key=current_scores.get)
        high_scores = []
        for name,score in current_scores.items():
            if score ==current_scores[high_score]:
                high_scores+=[name]

        print( 'The highest score/s belong to:')
        print(high_scores)
        print(current_scores)

    except ValueError:
     print('Everyones score is set at zero, lets start the game.')
    take_a_turn()


def take_a_turn():

    player_name = (input('please type the players name and hit enter: ')).title()
    if player_name == 'xxx'.title():
        command = input('''
        To check the score enter S,
        To take a turn enter T,
        To view the word list enter W,
        To End game enter E:  ''')
        game(command)
    player_word = input('please type the players word as it appears on the board and hit enter: ').upper()
    if current_game.get(player_name) == None:
        current_game[player_name] = [player_word]
    else:
        current_game[player_name] += [player_word]
    calc_score()


    if len(current_scores) > 4:
            print('You can not add another player to the game, sorry.')
            print('The last player added will be removed!')
            current_scores.popitem()
            current_game.popitem()
            print(current_game)
            print('The players still in the game are:')
            print(current_scores)


def game(command):
    command.upper()
    while True:
        if command.upper() == 'S':
            scores_check()
            command = 'T'
        elif command.upper() == 'T':
            take_a_turn()
        elif command.upper() == 'W':
            print(current_game)
            take_a_turn()
        elif command.upper() == 'E':
            exit()
        else:
            print(''' 
            HEY-That is not a valid entry!
            To start game enter S,
            To take a turn enter T,
            To End game enter E 
            ''')
            command = input('Try again here:  ')


current_game = {}
#current_game ={'Adison': ['HOT'], 'Chris': ['HOT'], 'Fayden': ['NOT'], 'Willow ': ['YES']}
current_scores = {}
print('''
    Hello, Welcome to the scrabble score keeper!
 
 This application will keep track of the scores of up to 4 players,
 and also a list of their words. If you need to exit taking turns
 simply enter 'xxx' in for the name when prompted.
 ''')

command = input('To check the score enter S, To take a turn enter T, To view the word list enter W, To End game enter E:  ')
game(command)


