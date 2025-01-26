import pygame

class Player:
    def __init__(self):
        self.idle_image = pygame.image.load('assets/player.png').convert_alpha()
        original_width, original_height = self.idle_image.get_size()

        new_width = 100
        new_height = int(original_height * (new_width / original_width))

        self.idle_image = pygame.transform.scale(self.idle_image, (new_width, new_height))
        self.original_image = self.idle_image
        self.rect = self.idle_image.get_rect(midbottom=(100, 300))
        self.velocity_y = 0  
        self.gravity = 0.8 
        self.jump_power = -15  
        self.speed = 5 
        self.facing_left = False
        self.on_ground = False  

    def jump(self):
        if self.on_ground:  
            self.velocity_y = self.jump_power  
            self.on_ground = False  

    def apply_gravity(self, platforms):
        self.velocity_y += self.gravity  
        self.rect.y += self.velocity_y  
        self.on_ground = False  

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0: 
                    self.rect.bottom = platform.rect.top  
                    self.velocity_y = 0 
                    self.on_ground = True  
                elif self.velocity_y < 0:  
                    self.rect.top = platform.rect.bottom  
                    self.velocity_y = 0  

        if self.rect.bottom > 600:  
            self.rect.bottom = 600
            self.on_ground = True
            self.velocity_y = 0

    def move(self, keys):
        """Handle horizontal movement."""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed  
            if not self.facing_left:
                self.idle_image = pygame.transform.flip(self.original_image, True, False)
                self.facing_left = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed  
            if self.facing_left:
                self.idle_image = self.original_image
                self.facing_left = False

    def draw(self, screen):
        """Draw player sprite on the screen."""
        screen.blit(self.idle_image, self.rect)

    def update(self, keys, screen, platforms):
        """Update player state each frame."""
        if keys[pygame.K_SPACE]:
            self.jump()

        self.apply_gravity(platforms) 
        self.move(keys)  
        self.draw(screen) 
