import pygame
from Settings import *
from Support import *
from math import sin

class monsters(pygame.sprite.Sprite):
    def __init__(self, groups, monster_name, position, obstacle_sprites, damage_player, trigger_death_particles, add_exp):
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

        #intéraction avec le perso
        self.can_attack = True
        self.attack_cooldown = 300 # potentiellement placer en dico des monstres pour en créer des plus agressifs que d'autres
        self.attack_time = None
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_exp = add_exp 

        # frame d'invulnérabilité
        self.vulnerable = True
        self.hit_time = None 
        self.invincibylity_duration = 300

        self.death_sound = pygame.mixer.Sound("../audio/death.wav")
        self.hit_sound = pygame.mixer.Sound("../audio/death.wav")
        self.attack_sound = pygame.mixer.Sound(monster_info["attack_sound"])
        self.death_sound.set_volume(0.2)
        self.hit_sound.set_volume(0.2)
        self.attack_sound.set_volume(0.3)

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
        if distance <= self.attack_radius and self.can_attack:
            if self.status != "attack":
                self.frame_index = 0
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status ="idle"

    def actions(self,player):
        if self.status =="attack":
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack, self.attack_type)
            self.attack_sound.play()
        elif self.status=="move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
        
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status =="attack":
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.pygame.Surface.set_alpha(alpha)
        else :
            self.image.pygame.Surface.set_alpha(255)

    def attacking_cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if self.vulnerable:
            if current_time - self.hit_time >= self.invincibylity_duration:
                self.vulnerable = True

    def get_damage(self,player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == "weapon":
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_spell_damage
            self.hit_time = pygame.time.get_ticks() 
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()
            self.trigger_death_particles(self.rect.center,self.monster_name)
            self.add_exp()
            self.death_sound.play()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.attacking_cooldown()
        self.check_death()
        
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
    
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255

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