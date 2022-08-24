import pygame 
import math  
import random 


WIDTH = 900 
HEIGHT = 700
PIXEL = 50  


class Snow(pygame.sprite.Sprite): 
    def __init__(self , size : tuple) -> None:
        super().__init__() 
        self.m0 , self.m = size # size will be like (m , m) , x*m : mass depends on the magnitude of size
        self.v0_x , self.v0_y = 0 ,  self.m 
        self.vx , self.vy = 0 ,  self.m 

        self.vx_delta = 0.01 * random.choice([-1,1]) 
        self.v0x_delta = self.vx_delta 
        self.vy_delta = 0.05  * self.vx 
        self.v0y_delta = self.v0_y

        self.image = pygame.image.load("snowfall/img/snowflake1.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image , size) 
        self.rect = self.image.get_rect()  


    def movement(self):   
        

        self.rect.x += self.vx 
        self.rect.y += self.vy  

        self.vx += self.vx_delta 
        self.vy += self.vy_delta
        
        if abs(self.vx) > self.vy : 
              
             
            self.v0x_delta *= -1 
            self.vx_delta = self.v0_x
            self.vy = self.v0_y  
            self.vx = self.v0_x 

        if self.rect.y + PIXEL >=  HEIGHT : 
            self.rect.y -= HEIGHT + 1000 
            self.rect.x = random.randint(0 , (WIDTH - PIXEL))  

        if self.rect.x <= PIXEL or self.rect.x + PIXEL >= WIDTH : 
            self.v0x_delta *= -1 
            self.vx_delta = self.v0x_delta 
            self.rect.x = PIXEL + 10 



    def show(self , window : pygame.Surface): 
        window.blit(self.image ,self.rect)  
        pygame.display.update() 


if __name__ == "__main__": 

    pygame.init() 
    window = pygame.display.set_mode((WIDTH , HEIGHT)) 
    snow_img = pygame.image.load("snowfall/img/snowflake1.png")
    pygame.display.set_icon(snow_img)  
    pygame.display.set_caption("Let it snoww  , let it snoww , let it snowwwww")   
    all_sprites_list = pygame.sprite.Group() 
    clock = pygame.time.Clock()

    for i in range(40): 
        number = random.randint(20,75)  
        snow_size = (number , number)
        snowflake = Snow(snow_size)  
        snowflake.rect.x = random.randint(0 , WIDTH - PIXEL)  
        snowflake.rect.y = random.randint(0 , WIDTH//10) 
        all_sprites_list.add(snowflake)  

    window.fill((255,255,255))
    running = True  
    while running : 

        for e in pygame.event.get(): 

            if e.type == pygame.QUIT: 
                running = False 
                pygame.quit() 
                raise SystemExit   

        for snow in all_sprites_list.sprites() : 
            snow.movement() 

        window.fill((120,0,255))
        all_sprites_list.draw(window)
        clock.tick(6)
        pygame.display.update()

             

        

        
