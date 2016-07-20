from collections import defaultdict
import time


class WordSquare:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = []
        self.create_indexes()

    def create_indexes(self):
        print "Reading words and creanting  indexes..."
        self.words = []
        self.prefixes = defaultdict(int)
        f = open("enable1.txt")

        # Only words of "width" letters
        # Only prefixes of "height" letters
        for line in f:
            line = line.rstrip('\n')
            if len(line) == self.width:
                self.words.append(line)
            if len(line) == self.height:
                for i in range(1, len(line) + 1):
                    self.prefixes[line[:i]] += 1
        f.close()

    def find(self):
        print "Solving..."
        if self.search(0):
            print "Solution:"
            self.show()
        else:
            print "No solution"

    def search(self, n):
        if n == self.height:
            return True
        else:
            for word in self.words:
                self.square.append(word)
                if (self.square_possible(n)):
                    self.show()
                    if self.search(n + 1):
                        return True
                    # Backtrack!
                self.square.pop()
            return False

    def square_possible(self, level):
        for i in range(0, self.width):
            part = ""
            for j in range(0, len(self.square)):
                part += self.square[j][i]
            if self.prefixes.get(part, 0) == 0:
                return False
        return True

    def show(self):
        print
        for l in self.square:
            print l


if __name__ == '__main__':
    begin = time.time()
    w = WordSquare(5, 4)
    w.find()
    end = time.time()
    print "Time elapsed: %dsec" % (end - begin)
