import pygame
from pygame.sprite import Sprite
from settings import Settings


class Button(Sprite):
    """Button class"""
    def __init__(self, game_settings: Settings, screen: pygame.surface.Surface,
                 actual_image: str = '0', image_name: str = 'default',
                 hover_image_name: str = 'hover_default', x_pos: int = 0, y_pos: int = 0,
                 x: int = 0, y: int = 0):
        """Init button and set its pos"""
        super(Button, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Button events
        self.image_name = image_name
        self.hover_image_name = hover_image_name

        self.image = pygame.image.load(f'images/{self.image_name}.png').convert()
        self.actual_image = actual_image
        self.is_hover = False
        self.is_revealed = False
        self.rect = self.image.get_rect()

        # Button start pos
        self.coords = (x_pos, y_pos)

        # Button rescale
        self.rescale()

    def change_image(self, file_name: str) -> None:
        """
            Зміна зображення кнопки
        """
        self.image = pygame.image.load(f'images/{file_name}.png').convert()
        self.image_name = file_name
        self.hover_image_name = f'hover_{self.image_name}'
        self.is_hover = False
        self.rescale()

    def rescale(self):
        self.image = pygame.transform.scale(self.image, (32, 32)).convert()
        self.rect.width = 32
        self.rect.height = 32

    def hover(self) -> None:
        """
            Метод, що починає анімовувати ефект наведення
        """
        if not self.is_hover:
            self.is_hover = True
            self.image = pygame.image.load(f'images/{self.hover_image_name}.png').convert()
            self.rescale()

    def stop_hover(self) -> None:
        """
            Метод, що дозволяє перестати анімовувати ефект наведення
        """
        if self.is_hover:
            self.is_hover = False
            self.image = pygame.image.load(f'images/{self.image_name}.png').convert()
            self.rescale()

    def on_click(self) -> None:
        """
            Метод, що змінює зображення кнопки після натиснення
        """
        self.change_image(self.actual_image)

    def get_coords(self) -> list:
        return self.coords

    def change_actual_image(self, new_image: str) -> None:
        self.actual_image = new_image


class NewGameButton(Sprite):
    def __init__(self, game_settings: Settings, screen: pygame.surface.Surface,
                 image_name: str = 'default', x: int = 0, y: int = 0, scale: float = 4):
        super(NewGameButton, self).__init__()
        """Init button and set its pos"""
        self.screen = screen
        self.game_settings = game_settings
        self.scale = scale
        # Button events
        self.image_name = image_name
        self.hover_image_name = f'hover_{self.image_name}'

        self.image = pygame.image.load(f'images/{self.image_name}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                      (self.image.get_rect().width*self.scale, self.image.get_rect().height*self.scale))
        self.is_hover = False
        self.rect = self.image.get_rect(center=(x,y))

        # Button start pos

    def hover(self) -> None:
        """
            Метод, що починає анімовувати ефект наведення
        """
        if not self.is_hover:
            self.is_hover = True
            self.image = pygame.image.load(f'images/{self.hover_image_name}.png').convert_alpha()
            self.rescale()

    def stop_hover(self) -> None:
        """
            Метод, що дозволяє перестати анімовувати ефект наведення
        """
        if self.is_hover:
            self.is_hover = False
            self.image = pygame.image.load(f'images/{self.image_name}.png').convert_alpha()
            self.rescale()

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def rescale(self):
        self.image = pygame.transform.scale(self.image,
                                      (self.image.get_rect().width * self.scale, self.image.get_rect().height * self.scale))
        self.rect.width = 128*self.scale
        self.rect.height = 64*self.scale
