class Player:

    # checkout the string function that retunrs a string
    # prefixing a variable with underscore(_) means its supposed to be hidden
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 2
        self._score = 2000

    def _get_lives(self):
        return self._lives

    def _set_lives(self, livesv):
        self._lives = livesv

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            self._score += 1000 * (level - self._level)
            self._level = level
        else:
            print("level cannot be less than zero")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

#another way to use property
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        self._score = score

    def __str__(self):
        return "Name:{0.name},Lives:{0.lives},Level:{0.level},_score:{0.score}".format(self)
