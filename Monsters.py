import pygame

class monsters(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.anim_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")

        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")

        self.rect.center = self.hitbox.center

    def collision(self,direction):
        # Donc si un sprite du bestiau rentre en collision avec celui d'un obstacle
        # si il va vers la droite, on le renvoie vers la gauche, et vice versa
        if direction == "horizontal":
            for sprite in self.obstacle_sprites :
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right 
        
        if direction =="vertical":
            for sprite in self.obstacle_sprites :
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom