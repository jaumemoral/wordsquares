from collections import defaultdict


class WordSquare:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find(self):
        self.show(self.search([], 0))

    def search(self, square, n):
        if len(square) == self.y:
            return square
        else:
            paraula = 0
            while paraula < len(words[self.x]):
                square.append(words[self.x][paraula])
                if (self.anem_be(square)):
                    print "anem be!" + str(n)
                    self.show(square)
                    return self.search(square, n + 1)
                else:
                    square.pop()
                    paraula += 1
            square.pop()
            print "Final!" + str(n)
            return square

    def anem_be(self, square):
        for i in range(0, self.x):
            part = ""
            for j in range(0, len(square)):
                part += square[j][i]
            if not self.existeix(part, words[self.x]):
                return False
        return True

    def existeix(self, part, words):
        for word in words:
            if word.startswith(part):
                print "Part:" + part + " es part de " + word
                return True

    def show(self, square):
        print "Quadrat:" + str(square)
        for l in square:
            print l


if __name__ == '__main__':
    words = defaultdict(list)
    f = open("enable1.txt")
    for line in f:
        line = line.rstrip('\n')
        words[len(line)].append(line)
    f.close()

    w = WordSquare(4, 4)
    w.find()
