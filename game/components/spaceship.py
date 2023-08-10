import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP
class Spaceship:

    def __init__(self, name):
        self.image = pygame.transform.scale(SPACESHIP, (80,90))
        self.name = name
        # TODO: Centramos la nave espacial horizontalmente en la pantalla
        # TODO: Calculamos la posición x restando el ancho de la imagen al ancho de la pantalla
        # TODO: y luego dividimos por 2 para obtener la posición centrada
        self.position_x = (SCREEN_WIDTH - self.image.get_width()) // 2
        # !Centramos la nave espacial verticalmente en la pantalla
        # Calculamos la posición y restando el alto de la imagen al alto de la pantalla
        # y luego dividimos por 2 para obtener la posición centrada.
        self.position_y = (SCREEN_HEIGHT - self.image.get_height()) // 2
        self.speed = 5

    def update(self):
        pass
    
    def moveLeft (self):
        self.position_x -= self.speed

    def movingRight(self):
        self.position_x += self.speed


    def draw(self, screen):
        screen.blit(self.image , (self.position_x, self.position_y + 230))

        