from alien_swarm import AlienSwarm

class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player():
    def __init__(self):
        self.bullets = [Bullet(24, 8)]
        self.score = 0

    def get_bullets(self):
        return self.bullets
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

class Collision():

    def __init__(self, player, swarm):
        self.player = player
        self.swarm = swarm

    def check_collisions(self):
        bullet_kill = []

        for b in player.get_bullets():
            if swarm.is_hit(b.x, b.y):
                bullet_kill.append(b)
                continue

        for b in bullet_kill:
            self.player.score += 10
            print("Score: %d" % self.player.score)
            self.player.remove_bullet(b)


if __name__ == "__main__":
    swarm = AlienSwarm(5)
    player = Player()
    collision = Collision(player, swarm)
    collision.check_collisions()