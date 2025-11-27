from pygame import *
class GameSprite(sprite.Sprite):
	def __init__(self, pic, x_pos, y_pos,width, height, speed):
		super().__init__()
		self.image = transform.scale(image.load(pic),(width,height))
		self.rect = self.image.get_rect()
		self.rect.x = x_pos
		self.rect.y = y_pos 
		self.basic_x = x_pos
		self.basic_y = y_pos
		self.speed = speed
	def update(self,window):
		window.blit(self.image, (self.rect.x, self.rect.y))

class GameRectangle():
	def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.fill_color = color
	def update(self,window):
		self.rect = Rect(self.x, self.y, self.width, self.height)
		draw.rect(window, self.fill_color, self.rect)
