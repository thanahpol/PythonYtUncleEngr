# main.py

import pygame
import math
import random
#from pygame import mixer

# initial setup
pygame.init()

# adjust screen
Width = 800
Height = 600

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Uncle vs Covid-19') # set game name
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('D:/Python/_PyGame/hillandale800600.png')

#############Uncle#############
# player
psize = 128

pimg = pygame.image.load('D:/Python/_PyGame/doctor128.png')
px = 100
py = Height - psize
pxchange = 0

def Player(x,y):
	screen.blit(pimg,(x,y))

#############Enermy#############
# enermy
esize = 64
eimg = pygame.image.load('D:/Python/_PyGame/coronavirus64.png')
ex = 50
ey = 0
eychange = 1

def Enermy(x,y):
	screen.blit(eimg,(x,y))

#############MULTI Enermy#############
exlist = []
eylist = []
ey_change_list = []
allenemy = 5

for i in range(allenemy):
	exlist.append(random.randint(50,Width-esize-50))
	eylist.append(random.randint(0,100))
	ey_change_list.append(random.randint(1,5))

#############VACCINE##############
# mask
msize = 32
mimg = pygame.image.load('D:/Python/_PyGame/vaccine32.png')
mx = 100
my = Height - psize
mychange = 50
mstate = 'ready'

def fire_vaccine(x,y):
	global mstate
	mstate = 'fire'
	screen.blit(mimg,(x,y))

#############COLLISION##############
def isCollision (ecx,ecy,mcx,mcy):
	distance = math.sqrt(math.pow(ecx-mcx,2)+math.pow(ecy-mcy,2))
	print (distance)
	if distance < 48:
		return True
	else:
		return False

#############SCORE##############
allscore = 0
font = pygame.font.Font('D:/Python/_PyGame/angsana.ttc',30)

def showscore():
	score = font.render('score: {}' .format(allscore), True,(255,255,255))
	screen.blit(score,(30,30))

#############SOUND#############
pygame.mixer.music.load('D:/Python/_PyGame/theme.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound('D:/Python/_PyGame/virusalert.wav')
sound.play()

#############GAME OVER#############
fontover = pygame.font.Font('D:/Python/_PyGame/angsana.ttc',80)
fontover2 = pygame.font.Font('D:/Python/_PyGame/angsana.ttc',50)
playsound = False
gameover = False

def Game_Over():
	global playsound
	global gameover
	overtext = fontover.render('Game Over !!!', True,(255,0,0))
	screen.blit(overtext,(250,225))
	overtext2 = fontover2.render('Press [N] for New Game', True,(255,255,255))
	screen.blit(overtext2,(240,300))
	if playsound  == False:
		gsound = pygame.mixer.Sound('D:/Python/_PyGame/game_over.wav')
		gsound.play()
		playsound = True
	#if gameover == False:
	#	gameover = True

#############GAME LOOP#############
running = True # starting the program

clock = pygame.time.Clock()
FPS = 120

while running:
	#clock.tick(FPS)
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		# checking pygame is running?
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pxchange = -20
			if event.key == pygame.K_RIGHT:
				pxchange = 20

			if event.key == pygame.K_SPACE:
				if mstate == 'ready':
					sound = pygame.mixer.Sound('D:/Python/_PyGame/laser.wav')
					sound.play()
					mx = px
					fire_vaccine(mx,my)

			if event.key == pygame.K_n:
				#gameover = False
				playsound = False
				allscore = 0
				for i in range(allenemy):
					exlist.append(random.randint(50,Width-esize-50))
					eylist.append(random.randint(0,100))


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				pxchange = 0

	#############RUN PLAYER############
	# px, py at the starting point
	Player(px,py)
	# Move player
	
	if px <= 0:
		px = 0
		px += pxchange
	elif px >= Width - psize:
		px = Width - psize
		pxchange = -1
		px += pxchange
	else:
		px += pxchange
	
	#############RUN ENERMY SINGLE############
	'''for i in range(5):
		Enermy(ex + (i + 100),ey)
		ey += eychange
	
	Enermy(ex,ey)
	ey += eychange
	'''

	#############RUN MULTI ENERMY############
	for i in range(allenemy):

		if eylist[i] > Height - esize and gameover == False:
			for i in range(allenemy):
				eylist[i] = 1000
			Game_Over()
			break
		'''
		if Game_Over == True:
			overtext = fontover.render('Game Over !!!', True,(255,0,0))
			screen.blit(overtext,(250,250))
		'''

		eylist[i] += ey_change_list[i]
		collisionmulti = isCollision(exlist[i],eylist[i],mx,my)
		if collisionmulti:
			my = Height - psize
			mstate = 'ready' 
			eylist[i] = 0
			exlist[i] = random.randint(0,Width-esize)
			allscore += 1

			sound = pygame.mixer.Sound('D:/Python/_PyGame/broken.wav')
			sound.play()

		Enermy(exlist[i], eylist[i])

	#############RUN VACCINE############
	if mstate == 'fire':
		fire_vaccine(mx,my)
		my -= mychange

	if my <= 0:
		my = Height - psize
		mstate = 'ready'

	collision = isCollision(ex,ey,mx,my)
	if collision:
		my = Height - psize
		mstate = 'ready' 
		ey = 0
		ex = random.randint(50,Width-esize)
		allscore += 1
		ey_change_list[i] += 1

	showscore()
	print(px)
	pygame.display.update()
	pygame.display.flip()
	pygame.event.pump()
	screen.fill((0,0,0))
	clock.tick(FPS)

