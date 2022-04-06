from util.button import Button
from util.references import References


class StartButton(Button):
    def onClick(self, mX, mY, scr):
        self.references.__init__()
        self.references.game_started = True
