
filename = "example.txt"


SCORE_LOSS = 0
SCORE_TIE = 3
SCORE_WIN = 6

compare = {
    1: {
        1: SCORE_TIE,
        2: SCORE_WIN,
        3: SCORE_LOSS
    },
    2: {
        1: SCORE_LOSS,
        2: SCORE_TIE,
        3: SCORE_WIN
    },
    3: {
        1: SCORE_WIN,
        2: SCORE_LOSS,
        3: SCORE_TIE
    }
}

play = {
    1: {
        1: 3,
        2: 1,
        3: 2
    },
    2: {
        1: 1,
        2: 2,
        3: 3
    },
    3: {
        1: 2,
        2: 3,
        3: 1
    }
}

def roundScore(round):
    left = ord(round[0]) - ord("A") + 1
    right = ord(round[1]) - ord("X") + 1


    played = play[left][right]
    totalScore = played + compare[left][played]
    return totalScore

rounds = []
with open(filename, "r") as file: 
    rounds = [[letter for letter in line.split()] for line in file.read().split("\n")]


scores = list(map(roundScore, rounds))
totalScore = sum(scores)
print(totalScore)

