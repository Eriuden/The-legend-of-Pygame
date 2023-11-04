import pygame
from Settings import *
from Support import *

class monsters(pygame.sprite.Sprite):
    def __init__(self, groups, monster_name, position, obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = "ennemy"

        self.import_graphics(monster_name)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index] 
        self.rect = self.image.get_rect(topleft = position)
        self.frame_index = 0
        self.anim_speed = 0.15
        self.direction = pygame.math.Vector2()
        self.hitbox = self.rect.pygame.Rect.inflate(0,-10)
        self.obstacle_sprite = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info["health"]
        self.exp = monster_info["exp"]
        self.speed = monster_info["speed"]
        self.attack = monster_info["damage"]
        self.resistance = monster_info["resistance"]
        self.attack_radius = monster_info["attack_radius"]
        self.notice_radius = monster_info["notice_radius"]
        self.attack_type = monster_info["attack_type"]

    def import_graphics(self,name):
        self.animations = {"idle": [], "move":[], "attack": []}
        main_path = f"../graphics/monsters/{name}"
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self,player):
        ennemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)
        distance = (player_vector - ennemy_vector).magnitude()

        if distance > 0:
            direction = (player_vector - ennemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        #ennemi proche, attaque, si loin mais nous voit, bouge, mais si on est hors de vue pour lui, attends
        if distance <= self.attack_radius:
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status ="idle"

    def actions(self,player):
        if self.status =="attack":
            pass
        elif self.status=="move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    def update(self):
        self.move(self.speed)
        
    def ennemy_update(self, player):
        self.get_status(player)
        self.actions(player)

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