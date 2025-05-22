from threading import Thread


class RendezvousDEchange:
    def __init__(self):
        self.k = 0
        self.numbers = [None] * 2
        self.flag = False

    def echanger(self, E):
        while (True):
            if self.numbers[0] == None:
                self.numbers[0] = E
            elif self.numbers[1] == None:
                self.numbers[1] = E

            if self.numbers[1] != None:
                temp = self.numbers[0]
                self.numbers[0] = self.numbers[1]
                self.numbers[1] = temp
                self.flag = True
                return self.numbers[1]
            else:
                while not self.flag:
                    pass
                return self.numbers[0]
