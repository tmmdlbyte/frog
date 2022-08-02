import pygame
class Mole(pygame.sprite.Sprite):
    
    def __init__(self, image_normal, image_abnormal, position, **kwargs):

        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.transform.scale(pygame.image.load(image_normal), (101, 103)),

                       pygame.transform.scale(pygame.image.load(image_abnormal), (101, 103))]

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.setPosition(position)

        self.is_hammer = False

    '''设置位置'''

    def setPosition(self, pos):

        self.rect.left= pos[0]
        self.rect.top = pos[1]
    '''设置被击中'''

    def setBeHammered(self):

        self.is_hammer = True
        self.image = self.images[1]

    '''显示在屏幕上'''

    def draw(self, screen):

        # if self.is_hammer: self.image = self.images[1]

        screen.blit(self.image, self.rect)

    '''重置'''

    def reset(self):

        self.image = self.images[0]

        self.is_hammer = False

class Hammer(pygame.sprite.Sprite):
    
    def __init__(self, image_normal, image_abnormal, position, **kwargs):

        pygame.sprite.Sprite.__init__(self)

        self.images = [image_normal, image_abnormal]

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.images[1])

        self.rect.left, self.rect.top = position

        # 用于显示锤击时的特效

        self.hammer_count = 0

        self.hammer_last_time = 4

        self.is_hammering = False

    '''设置位置'''

    def setPosition(self, pos):

        self.rect.centerx, self.rect.centery = pos

    '''设置hammering'''

    def setHammering(self):

        self.is_hammering = True
        self.image = self.images[1]

    '''显示在屏幕上'''

    def draw(self, screen):

        if self.is_hammering:

            self.image = self.images[1]

            self.hammer_count += 1

            if self.hammer_count > self.hammer_last_time:

                self.is_hammering = False

                self.hammer_count = 0

        else:

            self.image = self.images[0]

        screen.blit(self.image, self.rect)
