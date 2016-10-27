import pygame
import random
#from city_scroller.py import Building
from city_scroller import Scroller as Scroller

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)



class RunnerGame(pygame.sprite.Sprite):

	def __init__ (self, image, width, height):
		self.image = pygame.image.load(image)
		super().__init__()
		self.width = width
		self.height = height
		#self.color = color
		#self.image= pygame.Surface([width,height])
		#self.image.fill(color)
		self.rect = self.image.get_rect()
		#self.rect.x=screenWidth
	def update(self):
		self.rect.x -= 3
		if self.rect.x <= 0:
			self.rect.x = SCREEN_WIDTH+50
			self.rect.y = (random.randint(1,800))
		

#class pygame.sprite.Group():
#	def __init__(self):
#		goodspritelist=[]

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)


sprite_list = pygame.sprite.Group()
goodspritelist = pygame.sprite.Group()
badspritelist = pygame.sprite.Group()

player = RunnerGame("chimp.png", 15, 15)
sprite_list.add(player)


for i in range(100):
	goodsprite=RunnerGame("banana.png", 15, 10)
	goodsprite.rect.x = random.randint(1,SCREEN_WIDTH+50)
	goodsprite.rect.y = random.randint(1, SCREEN_HEIGHT)

	goodspritelist.add(goodsprite)
	sprite_list.add(goodsprite)

for w in range(50):
	badsprite=RunnerGame("leppy.png", 10, 15)
	badsprite.rect.x = random.randint(1,SCREEN_WIDTH+50)
	badsprite.rect.y = random.randint(1, SCREEN_HEIGHT)

	badspritelist.add(badsprite)
	sprite_list.add(badsprite)


	
#(self, width, height, base, color, speed)
front_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 0), FRONT_SCROLLER_COLOR, 3)
front_scroller.add_buildings()
middle_scroller = Scroller(SCREEN_WIDTH, 375, (SCREEN_HEIGHT - 100), MIDDLE_SCROLLER_COLOR, 2)
middle_scroller.add_buildings()
back_scroller = Scroller(SCREEN_WIDTH, 500, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
back_scroller.add_buildings()

done = False
score = 0
#build = Building(0, 800, 40, 60, WHITE)
#create = Scroller(10, 10, 20, RED, 20)
# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
	screen.fill(BACKGROUND_COLOR)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    

    # --- Drawing code should go here

	#buildList.append(build)
	back_scroller.draw_buildings(screen)
	back_scroller.move_buildings()
	middle_scroller.draw_buildings(screen)
	middle_scroller.move_buildings()
	front_scroller.draw_buildings(screen)
	front_scroller.move_buildings()
	#self.rect.move=(xpos)
	#xposList = []
	#xposList.append(xpos)
	xpos = pygame.mouse.get_pos()
	player.rect.x = xpos[0] - 20
	player.rect.y = xpos[1]

	sprite_list.draw(screen)
	sprite_list.update()

	blocks_hit_list = pygame.sprite.spritecollide(player, goodspritelist, True)
	for block in blocks_hit_list:
		score +=1
	blocks_hit_list= pygame.sprite.spritecollide(player,badspritelist,True)
	for block in blocks_hit_list:
		score-= 2
		screen.fill(RED)

		

	font = pygame.font.Font(None, 25)
	text = font.render("Score: " + str(score), 1, (WHITE))
	screen.blit(text, (50,50))

	# blocks_badhit_list = pygame.sprite.spritecollide(player, badspritelist, True):
	# 	font = pygame.font.Font(None, 40)
	# 	text = font.render("Game Over", 1, (WHITE))
	# 	screen.blit(text, (300,400))

    # --- Go ahead and update the screen with what we've drawn.
	
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE