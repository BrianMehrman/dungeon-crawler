class HeroController:
    def __init__(self):

        """
        This will attach the users controller to this actor. The last player
        controller actived takes presedence. Like a Freaky Friday mind swap.
        """

        pass

    def update(self, entity, delta_time):

        if entity.timer < 0

        keys = pygame.key.get_pressed()

        if (keys[K_RIGHT] and entity_data.direction != 1):
            entity_data.direction = 0
        elif (keys[K_LEFT] and entity_data.direction != 0):
            entity_data.direction = 1
        elif (keys[K_UP] and entity_data.direction != 3):
            entity_data.direction = 2
        elif (keys[K_DOWN] and entity_data.direction != 2):
            entity_data.direction = 3
