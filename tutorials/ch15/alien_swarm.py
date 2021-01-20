from alien import Alien

class AlienSwarm():

    def __init__(self, num_aliens, x=24, y=0):
        self.swarm = []

        for n in range(num_aliens):
            alien = Alien(x, y)
            self.swarm.append(alien)
            x += alien.get_width()
            if x > 260:
                x = 0
                y += alien.get_height()

    def debug_print(self):
        for a in self.swarm:
            print("x=%d, y=%d" %(a.x, a.y))
    
    def is_hit(self, x, y):
        alien_to_remove = None

        for a in self.swarm:
            print("Checking Alien at (%d, %d)" % (a.x, a.y))

            if x >= a.x and x <= a.x + a.get_width() and y >= a.y and y <= a.y + a.get_height():
                print(" It's a hit! Alien is going down!")

                alien_to_remove = a

                break
        
        if alien_to_remove != None:
            self.swarm.remove(alien_to_remove)

            return True

        return False


if __name__ == '__main__':
    swarm = AlienSwarm(50)
    swarm.debug_print()