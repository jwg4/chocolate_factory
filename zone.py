class Zone(object):
    chocolates = []

    def __init__(self, start_x, start_y, hand_off):
        self.start_x = start_x
        self.start_y = start_y
        self.hand_off = hand_off
        
    def add_choc(self, choc):
        choc.set_position(self.start_x, self.start_y)
        chocolates.add(choc)

    def draw(self, window):
        for choc in self.chocolates:
            choc.draw(window)


class Conveyor(Zone):
    def __init__(self, start_x, start_y, direction, hand_off):
        super(Conveyor, self).__init__(start_x, start_y, hand_off)
        self.direction = direction
