import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outllok not so good"
    elif answerNumber == 9:
        return "Very doubtful"
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

## INNA WERSJA 01
## def fortune(answerNumber):
##
## print(fortune(r))

## INNA WERSJA 02
## print(getAnswer(random.randint(1, 9)))


### można było po prostu nazwać funkcję fortune i poten użyć komendy print(fortune(r))
