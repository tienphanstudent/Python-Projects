# Tien Phan
# Scrabble - Python dictionary practice

# definitions
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCaseLetters = []
for i in range(len(letters)):
    lowerCaseLetters += letters[i].lower()


points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {i:j for i, j in zip(letters, points)}
lowercase_to_points = {i:j for i, j in zip(lowerCaseLetters, points)}
letter_to_points.update(lowercase_to_points)
letter_to_points[""] = 0
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "WordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":
    ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
brownie_points = "BROWNIE"
player_to_points = {}

def score_word(word):
    point_total = 0
    for i in word:
        point_total += letter_to_points[i]
    return point_total

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


def play_word(player, word):
    player_to_words[player].append(word)


# testers

# play_word("player1", "YAYTHISWORKS")
# play_word("player1", "YaYtHiSwOrKs")
# print(player_to_words)
# update_point_totals()
# print(player_to_points)
# print(score_word(brownie_points))
# print(brownie_points)
# print(letter_to_points)
