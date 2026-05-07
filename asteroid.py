import random
from circleshape import *
from constants import *
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.speed_mod = 1.0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt * self.speed_mod
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return 10
        elif self.radius == ASTEROID_MAX_RADIUS:
            size = 30
        else:
            size = 20

        log_event("asteroid_split")
        random_angle_value = random.uniform(20,50)
        first_vector = self.velocity.rotate(random_angle_value)
        second_vector = self.velocity.rotate(random_angle_value * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position, self.position, new_radius)
        new_asteroid_1.velocity = first_vector * 1.2

        new_asteroid_2 = Asteroid(self.position, self.position, new_radius)
        new_asteroid_2.velocity = second_vector * 1.2

        return size






