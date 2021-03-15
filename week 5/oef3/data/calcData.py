import json

slow = {
    "Droog": 8,
    "Nat": 5,
}


class CalcData:
    def __init__(self, snelheid=0, reactie=0, wegdek="D", ):
        self.snelheid = snelheid
        self.reactie = reactie
        self.wegdek = wegdek
        self.dist = 0

    def calcStopAfstand(self):
        self.convert()
        self.dist * self.reactie + ((self.snelheid * self.snelheid) / (2 * slow[self.wegdek]))

    def convert(self):
        self.snelheid = float(self.snelheid) / 3.6

    def get_dist(self):
        return self.dist