htmlText = """<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"""

"""Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html"""


def FirstTry():
    # print(htmlText)
    currentTag = ""
    tagType = -1
    for char in htmlText:
        if char == "<":
            # starting
            currentTag = ""
            tagType = "Start :"

        elif char == ">":
            # ending
            print(f"{tagType} {currentTag}")
            currentTag = ""

        elif char == "/":
            # ending tag
            currentTag = ""
            tagType = "End :"

        elif char == " ":
            print(f"{tagType} {currentTag}")
            currentTag = ""
            tagType = "->"

        else:
            currentTag += char


def SecondTry():
    startIndex = 0
    while startIndex < len(htmlText):
        startIndex = htmlText.find(startIndex, "<")
        endIndex = htmlText.find(startIndex, ">")
        htmlSub = htmlText[startIndex:endIndex]
        allItems = htmlSub.split(" ")
        if len(allItems) == 1:
            # only one tag
            pass


# FirstTry()


def score_Stuart(string):
    vowels = ["A", "E", "I", "O", "U"]
    for i in 
    return -1


def score_Kevin(string):
    vowels = ["A", "E", "I", "O", "U"]
    return -1


def minion_game(string):
    kevin = score_Kevin(string)
    stuart = score_Stuart(string)
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print(f"Stuart {stuart}")


minion_game("BANANA")
