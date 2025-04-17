import pygame
import sys
from BioBot import *

pygame.init()

WIDTH,HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("simulate")

WHITE = (255,255,255)
BLACK = (0,0,0)

bot = Bot9()

def run():
	bot.draw_rect(pygame, screen, BLACK, (200,10,10), (30,0,200), (0,200,0))

	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill(WHITE)
		bot.draw_rect(pygame, screen, BLACK, (200,10,10), (30,0,200), (50,200,0))
		pygame.display.flip()
		clock.tick(60)

run()
