class Card(object):
    def __init__(self, title = "Dark Magician", type = "Monster"):
        """Contains the attributes of the card."""
        self.title = title
        self.short_title = self.create_short_title(title)
        self.attack = 2500
        self.defence = 2100
        self.type = type
        self.description = "I am a card."
        self.defence_mode = False
        self.face_down = True

    def create_short_title(self, title):
        """Creates a shortened title for displaying on the board."""
        length = len(title)
        # If it's a long title, shorten it
        if length >= 10:
            return "[{0}]".format(title[0:10])
        # If it's short, add whitespace
        else:
            start = "["
            end = ""
            # Work out how much whitespace is needed
            white_space = 10 - length
            white_iter = int(white_space / 2)
            # If it's an even amount, add the same to each side
            if white_space % 2 == 0:
                for i in range(white_iter):
                    start += " "
                    end += " "
                end += "]"
                return start + title + end
            # Else have one more blank char to the left
            else:
                for i in range(white_iter):
                    start += " "
                    end += " "
                end += " ]"
                return start + title + end