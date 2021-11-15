firstLetters = dict({
    "є": "ye",
    "ї": "yi",
    "й": "y",
    "ю": "yu",
    "я": "ya"
})

letters = dict({
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "е": "e",
    "є": "ie",
    "ж": "zh",
    "з": "z",
    "и": "y",
    "і": "i",
    "ї": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ю": "iu",
    "я": "ia"
})


def vectorizer(file):
    textRaw = open(file, "r").read().lower()
    maxSentenceLength = 0

    sentences = textRaw.split(sep=". ")
    sentencesMatrix = list()
    for sentence in sentences:
        vectorizedSentence = vectorizeSentence(sentence)
        sentencesMatrix.append(vectorizedSentence)
        if maxSentenceLength < len(vectorizedSentence):
            maxSentenceLength = len(vectorizedSentence)
    normolizedMatrix = normolizeMatrix(sentencesMatrix, maxSentenceLength)
    printMatrix(normolizedMatrix)

def printMatrix(matrix):
    for sentence in matrix:
        for word in sentence:
            print('{:4}'.format(word), end="")
        print("")

def normolizeMatrix(sentencesMatrix, maxSentenceLength: int):
    normolizedMatrix = list()
    for sentence in sentencesMatrix:
        normolizedMatrix.append(sentence + ([0] * (maxSentenceLength - len(sentence))))
    return normolizedMatrix

def vectorizeSentence(sentence: str):
    words = sentence.split(sep=" ")
    sentenceRow = list()
    for word in words:
        wordSum = vectorizeWord(word)
        if wordSum > 0:
            sentenceRow.append(wordSum)
    return sentenceRow

def vectorizeWord(word: str):
    sum = 0
    transliteratedWord = transliterateWord(word)
    for letter in transliteratedWord:
        sum += ord(letter) - 96
    return sum

def transliterateWord(word: str):
    resultWord = ""
    for letterIndex in range(len(word)):
        # Exception Letters
        if (letterIndex < len(word) - 1 and word[letterIndex] == "з"):
            if word[letterIndex + 1] == "г":
                resultWord += "zgh"
                letterIndex += 1
                continue

        if letterIndex == 0 and (word[0] in firstLetters.keys()):
            resultWord += firstLetters[word[0]]
            continue
        if (word[letterIndex] in letters.keys()):
            resultWord += letters[word[letterIndex]]
    return resultWord


vectorizer("data.txt")
