import UserException

class Story:
    story_line = ""

    def __init__(self):
        self.story_line = """Hello! My name is Kalyan.
I am studying B.Tech. CSE 3rd Year.
I live in Andhra Pradesh, India.
I am a Enemy Full Stack Developer by profession.
"""

    def check(self):
        lines = self.story_line.split("\n")
        count = 0
        for line in lines:
            if any(char.isdigit() for char in line):
                count += 1
        if count < 3:
            raise UserException.InvalidInputException()
        return True
    
    def count(self):
        self.d = {}
        word_count = 0
        alphabet_count = 0
        digit_count = 0
        line_count = 0
        lines = self.story_line.split("\n")
        for line in lines:
            word_count += len(line.split(" "))
            alphabet_count += len([char for char in line if char.isalpha()])
            digit_count += len([char for char in line if char.isdigit()])
            line_count += 1
        self.d['words'] = word_count
        self.d['lines'] = line_count
        self.d['alphabets'] = alphabet_count
        self.d['digits'] = digit_count
    
    def update(self):
        words = self.story_line.split()
        print(words)
        for word in words:
            if word[0] in ["a","e","i","o","u","A","E","I","O","U"]:
                print(word)
                self.story_line = self.story_line.replace(word+" ","",1)
    
    def convert(self):
        # converted = ""
        # for char in self.story_line:
        #     if char.islower():
        #         char = char.upper()
        #     if char.isupper():
        #         char = char.lower()
        #     converted += char
        # self.story_line = converted
        self.story_line = self.story_line.swapcase()

    def extract(self):
        words = self.story_line.split()
        required_words = []
        for word in words:
            if word[0] == "E":
                required_words.append(word)
        print(required_words)
    
    def print(self):
        required_story = ""
        for char in self.story_line:
            if char.isalpha():
                required_story+=char
        print(required_story)
        f = open("text.txt", "w")
        f.write(required_story)

def main():
    s = Story()
    s.print()

if __name__ == "__main__":
    main()