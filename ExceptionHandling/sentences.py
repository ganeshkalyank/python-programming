class InvalidSentenceException(Exception):
    pass

sentences = []

valid=True

while len(sentences)!=5 or not valid:
    try:
        sentence = input("Enter sentence: ")
        if not sentence.isalpha():
            raise InvalidSentenceException()
        sentences.append(sentence)
    except InvalidSentenceException:
        print("Invalid! Please try again.")

for sentence in sentences:
    print(sentence)
