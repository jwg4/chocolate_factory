import random

from chocolate import Bar

class Zone(object):

    def __init__(self, start_x, start_y, hand_off):
        self.chocolates = []
        self.start_x = start_x
        self.start_y = start_y
        self.hand_off = hand_off
        
    def add_choc(self, choc):
        choc.set_position(self.start_x, self.start_y)
        self.chocolates.append(choc)

    def remove_choc(self, choc=None):
        if choc is None:
            choc = self.chocolates[0]
        self.chocolates.remove(choc)
        self.hand_off.add_choc(choc)

    def draw(self, window):
        for choc in self.chocolates:
            choc.draw(window)


class Conveyor(Zone):
    def __init__(self, start_x, start_y, direction, hand_off):
        super(Conveyor, self).__init__(start_x, start_y, hand_off)
        self.direction = direction

    def update(self):
        for choc in self.chocolates:
            position = choc.get_position()
            if (position[0] - self.start_x) * self.direction > 400:
                self.remove_choc(choc)
            else:
                choc.set_position(position[0] + self.direction, position[1])

class DropZone(Zone):
    def __init__(self, character, position, start_x, start_y, hand_off):
        self.character = character
        self.position = position
        self.catching = [ set() for x in range(10) ]
        self.dropping = list()
        super(DropZone, self).__init__(start_x, start_y, hand_off)

    def add_choc(self, choc):
        if self.character.position == self.position:
            self.catching[9].add(choc)
        else:
            self.dropping.append(choc)
        super(DropZone, self).add_choc(choc)

    def update(self):
        for choc in self.catching[0]:
            self.remove_choc(choc)
        self.catching = self.catching[1:] + [set()]
        for choc in self.dropping:
            position = choc.get_position()
            choc.set_position(position[0], position[1] + 1)

class LoadingBay(Zone):
    def __init__(self):
        super(LoadingBay, self).__init__(100, 100, None)

    def update(self):
        pass

class StartMachine(Zone):
    countdown = 0

    def __init__(self, handoff):
        super(StartMachine, self).__init__(1000, 400, handoff)

    def update(self):
        if not self.chocolates:
            self.add_choc(Bar())
            self.countdown = 100 * random.randint(0, 12) + 200
        elif self.countdown == 0:
            self.remove_choc()
        else:
            self.countdown = self.countdown - 1
            self.chocolates[0].set_position(900 + self.countdown, 400)
