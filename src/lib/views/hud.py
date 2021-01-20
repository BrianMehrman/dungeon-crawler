class Hud:
    def __init__(self, actor):
        """
        Manages the drawing UI elements for the target actor. Any actor can become the target of
        the Hud just like the world viewer
        """
        self.actor = actor


    def update(self):
        """
        draws the UI elements. This will just draw over what is there. Make sure
        to draw this last
        """