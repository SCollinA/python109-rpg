# parties
class Party:
    MAX_LENGTH = 3
    def __init__(self, party):
        self.party = party

    def alive(self):
        for character in self.party:
            if character.health > 0:
                return True
        return False

    def print_status(self):
        for character in self.party:
            character.print_status()