import pygame
from pygame.locals import *
pygame.init()

white = (255,255,255)
level1 = True
enemy1Bool = True
enemy2Bool = True
enemy3Bool = True
ballSpeed = 0
ballY = (430)
paddle1X = (640/2)
keepGoing = True
numEnemy = 3
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Jshot")
screen.fill(white)

enemy = pygame.sprite.Sprite()
enemy.image = pygame.image.load("enemy.png").convert()
enemy.rect = enemy.image.get_rect()
enemy.rect.center = (640/2,50)
screen.blit(enemy.image, enemy.rect)

enemy2 = pygame.sprite.Sprite()
enemy2.image = pygame.image.load("enemy.png").convert()
enemy2.rect = enemy2.image.get_rect()
enemy2.rect.center = (80,480/2)
screen.blit(enemy2.image, enemy2.rect)

enemy3 = pygame.sprite.Sprite()
enemy3.image = pygame.image.load("enemy.png").convert()
enemy3.rect = enemy3.image.get_rect()
enemy3.rect.center = (560, 480/2)
screen.blit(enemy3.image, enemy3.rect)

paddle1 = pygame.sprite.Sprite()
paddle1.image = pygame.image.load("paddleB.bmp").convert()
paddle1.rect = paddle1.image.get_rect()
paddle1.rect.center = (paddle1X, 435)
screen.blit(paddle1.image, paddle1.rect)

ball = pygame.sprite.Sprite()
ball.image = pygame.image.load("ballB.bmp")
ball.rect = ball.image.get_rect()
ball.rect.center = (paddle1X,ballY)
screen.blit(ball.image, ball.rect)
pygame.display.update()

while level1 == True:
	while keepGoing == True:
		screen.fill(white)
		if enemy1Bool:
			ballY -= ballSpeed
			enemy.image
			enemy.rect
			enemy.rect.center = (640/2, 50)
			screen.blit(enemy.image, enemy.rect)

			(paddle1X,mouseY) = pygame.mouse.get_pos()
			paddle1.image
			paddle1.rect
			paddle1.rect.center = (paddle1X, 435)
			screen.blit(paddle1.image, paddle1.rect)

			ball.image
			ball.rect
			ball.rect.center = (paddle1X,ballY)
			screen.blit(ball.image, ball.rect)
		
			if ball.rect.colliderect(enemy.rect) == True:
				ballSpeed = 0
				ballY = 430
				enemy1Bool = False
				pygame.display.update()
				numEnemy -= 1

			if numEnemy == 0:
				keepGoing = False

			for event in pygame.event.get():
				if pygame.mouse.get_pressed() == (1,0,0):
					ballSpeed = 8
					ballY = 430

				if event.type == KEYDOWN:
					if event.key == K_f:
						screen = pygame.display.set_mode((640,480),FULLSCREEN)
					if event.key == K_d:
						screen = pygame.display.set_mode((640,480))

				if event.type == QUIT:
					enemy1Bool = False
					enemy2Bool = False
					enemy3Bool = False
					keepGoing = False
					level1 = False

		if enemy2Bool:
			ballY -= ballSpeed
			enemy2.image
			enemy2.rect
			enemy2.rect.center = (80,480/2)
			screen.blit(enemy2.image, enemy2.rect)

			(paddle1X,mouseY) = pygame.mouse.get_pos()
			paddle1.image
			paddle1.rect
			paddle1.rect.center = (paddle1X, 435)
			screen.blit(paddle1.image, paddle1.rect)

			ball.image
			ball.rect
			ball.rect.center = (paddle1X,ballY)
			screen.blit(ball.image, ball.rect)
		
			if ball.rect.colliderect(enemy2.rect) == True:
				ballSpeed = 0
				ballY = 430
				enemy2Bool = False
				pygame.display.update()
				numEnemy -= 1

			if numEnemy == 0:
				keepGoing = False

			for event in pygame.event.get():
				if pygame.mouse.get_pressed() == (1,0,0):
					ballY = 430
					ballSpeed = 8

				if event.type == KEYDOWN:
					if event.key == K_f:
						screen = pygame.display.set_mode((640,480),FULLSCREEN)
					if event.key == K_d:
						screen = pygame.display.set_mode((640,480))

				if event.type == QUIT:
					enemy1Bool = False
					enemy2Bool = False
					enemy3Bool = False
					keepGoing = False
					level1 = False

		if enemy3Bool:
			ballY -= ballSpeed
			enemy3.image
			enemy3.rect
			enemy3.rect.center = (560, 480/2)
			screen.blit(enemy3.image, enemy3.rect)

			(paddle1X,mouseY) = pygame.mouse.get_pos()
			paddle1.image
			paddle1.rect
			paddle1.rect.center = (paddle1X, 435)
			screen.blit(paddle1.image, paddle1.rect)

			ball.image
			ball.rect
			ball.rect.center = (paddle1X,ballY)
			screen.blit(ball.image, ball.rect)
		
			if ball.rect.colliderect(enemy3.rect) == True:
				ballSpeed = 0
				ballY = 430
				enemy3Bool = False
				pygame.display.update()
				numEnemy -= 1

			if numEnemy == 0:
				keepGoing = False

			for event in pygame.event.get():
				if pygame.mouse.get_pressed() == (1,0,0):
					ballSpeed = 8
					ballY = 430

				if event.type == KEYDOWN:
					if event.key == K_f:
						screen = pygame.display.set_mode((640,480),FULLSCREEN)
					if event.key == K_d:
						screen = pygame.display.set_mode((640,480))

				if event.type == QUIT:
					enemy1Bool = False
					enemy2Bool = False
					enemy3Bool = False
					level1 = False
					keepGoing = False

		pygame.display.update()

	if numEnemy == 0:
		screen.fill(white)
		font = pygame.font.Font(None, 100)
		text = font.render("You Won", 1, (0, 0, 0))
		textpos = text.get_rect()
		textpos.centerx = screen.get_rect().centerx
		textpos.centery = screen.get_rect().centery
		screen.blit(text, textpos)
		pygame.display.update()

		for event in pygame.event.get():
				if pygame.mouse.get_pressed() == (0,0,1):
					keepGoing = True
					enemy1Bool = True
					enemy2Bool = True
					enemy3Bool = True
					numEnemy = 3


				if event.type == KEYDOWN:
					if event.key == K_f:
						screen = pygame.display.set_mode((640,480),FULLSCREEN)
					if event.key == K_d:
						screen = pygame.display.set_mode((640,480))

				if event.type == QUIT:
					level1 = False

	if numEnemy > 0:
		screen.fill(white)
		font = pygame.font.Font(None, 100)
		text = font.render("You Lose", 1, (0, 0, 0))
		textpos = text.get_rect()
		textpos.centerx = screen.get_rect().centerx
		textpos.centery = screen.get_rect().centery
		screen.blit(text, textpos)
		pygame.display.update()
