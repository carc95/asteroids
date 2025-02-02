from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):        
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()                    
            
        else:
            random_angle = random.uniform(20,50)
            velocity_clk = self.velocity.rotate(random_angle)
            velocity_anti_clk = self.velocity.rotate(-random_angle)
            old_radius = self.radius 
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity_clk * 1.2
            asteroid2.velocity = velocity_anti_clk * 1.2
            self.kill()


        
        

    

    
