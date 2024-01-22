# Pearl Natalia
# Lava Game

# --- PROGRAM DETAILS ---
import pygame, sys, random

pygame.init()
pygame.display.set_mode()

# .convert_alpha() allows images to adjust when display console  = resized
# link to source: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha
background = pygame.image.load('images/LavaBackground.png').convert_alpha()
backgroundSize = background.get_size()

# Window
w, h = 750, 650
windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Lava Attack!')

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# --- INTRO SCREEN ---
def intro():
	intro = True
	Clock = pygame.time.Clock()
	# Coordinates of moving background
	bX, bY, bX1 = 0, 0, 0 - w

	while intro:
		# Key controls
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				sys.exit()
			if keys[pygame.K_s]:
				intro = False
				redrawGameWindow()
			if keys[pygame.K_i]:
				intro = False
				instructionScreen()

		# Displaying continuous loop of a background
		screen.blit(background, (bX, bY))
		screen.blit(background, (bX1, bY))

		# Moving the background
		bX += 5
		bX1 += 5

		# Looping background back onto screen
		if bX > w:
			bX = -w
		if bX1 > w:
			bX1 = -w

		# Creating titles/descriptions
		font2 = pygame.font.SysFont('Myriad Pro', 40)
		title = pygame.image.load('images/gameTitle.png').convert_alpha()
		description0 = font2.render("Press 's' to start game.", 1, (WHITE))
		description1 = font2.render("Press 'esc' to exit game.", 1, (WHITE))
		description2 = font2.render("Press 'i' for instructions to the game.", 1,
		                            (WHITE))

		descriptions = []
		descriptions.append(description0)
		descriptions.append(description1)
		descriptions.append(description2)

		# Sizing of titles/descriptions
		titleSize = title.get_size()

		descriptionSize = [0] * 3
		for i in range(len(descriptionSize)):
			descriptionSize[i] = descriptions[i].get_size()

		# Placing titles/descriptions
		xTitle = w / 2 - titleSize[0] / 2
		yTitle = h / 2 - titleSize[1] / 2 - 80

		x = [0] * 3
		for i in range(len(x)):
			x[i] = w / 2 - descriptionSize[i][0] / 2

		y = [0] * 3
		lineSpace = 200
		for i in range(len(y)):
			y[i] = yTitle + lineSpace
			lineSpace += 40

		# Displaying titles/descriptions
		screen.blit(title, (xTitle, yTitle))
		for i in range(len(x)):
			screen.blit(descriptions[i], (x[i], y[i]))

		pygame.display.update()
		Clock.tick(20)


# --- INSTRUCTIONS SCREEN ---
def instructionScreen():
	instructionsScreen = True
	Clock = pygame.time.Clock()

	# Key controls
	while instructionsScreen:
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				sys.exit()
			if keys[pygame.K_s]:
				instructionsScreen = False
				redrawGameWindow()

		# Loading images
		screen.fill((BLACK))
		volcano = pygame.image.load('images/volcano.png').convert_alpha()
		lavaFloor = pygame.image.load('images/lavaFloor.png').convert_alpha()

		# Creating the instructions
		font2 = pygame.font.SysFont('Myriad Pro', 35)
		instructionsTitle = pygame.image.load(
		 'images/instructionsTitle.png').convert_alpha()
		instructions0 = font2.render('Move around to collect all the coins.', 0.5,
		                             (WHITE))
		instructions1 = font2.render('Do not fall in the lava!', 0.5, (WHITE))
		instructions2 = font2.render('Watch out for the falling volcanic rocks!',
		                             0.5, (WHITE))
		instructions3 = font2.render("Use the keys to move the character.", 0.5,
		                             (WHITE))
		instructions4 = font2.render("Press 's' to start the game.", 0.5, (WHITE))

		instructions = []
		instructions.append(instructions0)
		instructions.append(instructions1)
		instructions.append(instructions2)
		instructions.append(instructions3)
		instructions.append(instructions4)
		instructions.append(instructionsTitle)

		# Getting instruction sizes
		instructionsSize = [0] * 6
		for i in range(len(instructionsSize)):
			instructionsSize[i] = instructions[i].get_size()

		# Placing instructions onto screen
		xTitle = w / 2 - (instructionsSize[5][0]) / 2 + 20
		yTitle = 100
		x0 = w / 2 - (instructionsSize[0][0]) / 2
		y0 = yTitle + 160

		x = [0] * 5
		x[0] = x0
		for i in range(1, 5):
			x[i] = w / 2 - (instructionsSize[i][0]) / 2

		y = [0] * 5
		y[0] = y0
		for i in range(1, 5):
			y[i] = y[i - 1] + 30

		# Displaying instructions onto screen
		screen.blit(volcano, (535, 435))
		screen.blit(lavaFloor, (-50, h - 65))
		screen.blit(instructionsTitle, (xTitle, yTitle))
		screen.blit(instructions0, (x0, y0))
		for i in range(1, 5):
			screen.blit(instructions[i], (x[i], y[i]))

		pygame.display.update()
		Clock.tick()


# --- WIN SCREEN ---
def winScreen():
	winScreen = True
	Clock = pygame.time.Clock()
	print('Press esc to escape.')

	# coordinates of moving background
	bX, bY, bX1 = 0, 0, 0 - w

	# Key controls
	while winScreen:
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				sys.exit()

		# Moving the background across the screen
		bX += 7
		bX1 += 7

		# Displaying a continuous loop of a background
		sky = pygame.image.load('images/sky.png').convert_alpha()
		screen.blit(sky, (bX, bY))
		screen.blit(sky, (bX1, bY))

		# Looping background back onto screen
		if bX > w:
			bX = -w
		if bX1 > w:
			bX1 = -w

		# Win message/sizing
		title = pygame.image.load('images/winTitle.png').convert_alpha()
		titleSize = title.get_size()
		xTitle = w / 2 - titleSize[0] / 2
		yTitle = h / 2 - titleSize[1] / 2 + 30

		# Displaying titles/descriptions
		screen.blit(title, (xTitle, yTitle))

		pygame.display.update()
		Clock.tick(30)


# --- LOSE SCREEN ---
def loseScreen():
	print('Press esc to escape.')

	while loseScreen:
		# Key controls
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				sys.exit()

		# Displaying losing message
		gameOver = pygame.image.load('images/gameOver.png')
		screen.blit(gameOver, (0, 0))
		pygame.display.update()


# --- PLATFORM DETECTION FUNCTION ---
def platform_detect(marioX, marioY, marioW, marioH, platX, platY, platW, platH,
                    vY):

	# Reducing dimensions of mario image incase mario image has white space
	marioX += 5
	marioW -= 5

	# Determining if mario is on a platform
	if (marioX > platX and marioX + marioW < platX + platW) or (
	  marioX < platX
	  and marioX + marioW > platX) or (marioX < platX + platW
	                                   and marioX + marioW > platX + platW):
		if marioY + marioH >= platY and vY > 0:
			return True
	else:
		return False


# --- GAME SCREEN ---
def redrawGameWindow():

	# Background and floor
	background = pygame.image.load('images/LavaBackground.png').convert_alpha()
	backgroundX, backgroundY = 0, 0

	floor = pygame.image.load('images/Floor.png').convert_alpha()
	floorSize = floor.get_size()
	floorSizeH = floorSize[1]
	floorX, floorY = 0, h - floorSizeH + 15

	# Mario image
	mario = pygame.image.load('mario/pic1.png').convert_alpha()
	nextLeftPic = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	nextRightPic = [4, 4, 4, 4, 5, 6, 7, 5, 4, 4, 4, 4]
	marioSize = mario.get_size()
	marioW = marioSize[0]
	marioH = marioSize[1]
	GROUND_LEVEL = h - marioH

	# Mario's movement
	RUN_SPEED = 7
	JUMP_SPEED = -23
	GRAVITY = 2.5

	# Platforms
	platform = [0] * 4
	for i in range(4):
		platform[i] = pygame.image.load('images/platform' + str(i) +
		                                '.png').convert_alpha()

	platform_list = [
	 platform[1], platform[0], platform[3], platform[2], platform[1], platform[0],
	 platform[0], platform[0], platform[3], platform[0], platform[2]
	]

	# Platform sizes
	PW = [0] * 11
	PH = [0] * 11
	for i in range(len(PW)):
		platformSize = platform_list[i].get_size()
		PW[i] = platformSize[0]
		PH[i] = platformSize[1]

	# Platform placements
	PX = [0] * 11
	PY = [0] * 11

	PX[0], PY[0] = 325, GROUND_LEVEL - 200
	PX[1], PY[1] = 500, GROUND_LEVEL - 50
	PX[2], PY[2] = 690, GROUND_LEVEL - 230
	PX[3], PY[3] = 970, GROUND_LEVEL - 10
	PX[4], PY[4] = 1250, GROUND_LEVEL - 200
	PX[5], PY[5] = 1180, GROUND_LEVEL - 120
	PX[6], PY[6] = 590, GROUND_LEVEL - 140
	PX[7], PY[7] = 940, GROUND_LEVEL - 200
	PX[8], PY[8] = 1400, GROUND_LEVEL - 30
	PX[9], PY[9] = 1360, GROUND_LEVEL - 125
	PX[10], PY[10] = 1500, GROUND_LEVEL - 320

	# Marios placement
	marioX = w / 2 - 50
	marioY = PY[0] - 250
	marioVx, marioVy = 0, 0
	marioPicNum = 4
	marioDir = "right"
	marioPic = [0] * 12

	# Loading sprint mario images
	for i in range(len(marioPic)):
		marioPic[i] = pygame.image.load('mario/pic' + str(i) +
		                                '.png').convert_alpha()

	# Coin image and size
	coin = pygame.image.load('images/coin.png').convert_alpha()
	coinSize = coin.get_size()
	CW = coinSize[0]
	CH = coinSize[1]

	# COIN PLACEMENT
	CX = [0] * 37
	CY = [0] * 37

	CX[0] = PX[0] + ((PW[0] - (CW * 2)) / 3)
	CY[0] = PY[0] - CH - 10
	CX[1] = PX[0] + (2 * ((PW[0] - (CW * 2)) / 3)) + CW
	CY[1] = PY[0] - CH - 10
	CX[2] = PX[1] + PW[1] / 2 - CW / 2
	CY[2] = PY[1] - CH - 10
	CX[3] = PX[6] + PW[6] / 2 - CW / 2
	CY[3] = PY[6] - CH - 10
	CX[4] = PX[2] + ((PW[2] - (CW * 4)) / 5)
	CY[4] = PY[2] - CH - 10
	CX[5] = PX[2] + (2 * ((PW[2] - (CW * 4)) / 5)) + CW
	CY[5] = PY[2] - CH - 10
	CX[6] = PX[2] + (3 * ((PW[2] - (CW * 4)) / 5)) + (2 * CW)
	CY[6] = PY[2] - CH - 10
	CX[7] = PX[2] + (4 * ((PW[2] - (CW * 4)) / 5)) + (3 * CW)
	CY[7] = PY[2] - CH - 10
	CX[8] = PX[3] + ((PW[3] - (CW * 3)) / 4)
	CY[8] = PY[3] - CH - 10
	CX[9] = PX[3] + (2 * ((PW[3] - (CW * 3)) / 4)) + CW
	CY[9] = PY[3] - CH - 10
	CX[10] = PX[3] + (3 * ((PW[3] - (CW * 3)) / 4)) + (2 * CW)
	CY[10] = PY[3] - CH - 10
	CX[11] = PX[5] + PW[5] / 2 - CW / 2
	CY[11] = PY[5] - CH - 10
	CX[12] = PX[9] + PW[9] / 2 - CW / 2
	CY[12] = PY[9] - CH - 10
	CX[13] = PX[4] + ((PW[4] - (CW * 2)) / 3)
	CY[13] = PY[4] - CH - 10
	CX[14] = PX[4] + (2 * ((PW[4] - (CW * 2)) / 3)) + CW
	CY[14] = PY[4] - CH - 10
	CX[15] = PX[7] + PW[7] / 2 - CW / 2
	CY[15] = PY[7] - CH - 10
	CX[16] = PX[10] + ((PW[10] - (CW * 3)) / 4)
	CY[16] = PY[10] - CH - 10
	CX[17] = PX[10] + (2 * ((PW[10] - (CW * 3)) / 4)) + CW
	CY[17] = PY[10] - CH - 10
	CX[18] = PX[10] + (3 * ((PW[10] - (CW * 3)) / 4)) + (2 * CW)
	CY[18] = PY[10] - CH - 10
	CX[19] = PX[8] + ((PW[8] - (CW * 4)) / 5)
	CY[19] = PY[8] - CH - 10
	CX[20] = PX[8] + (2 * ((PW[8] - (CW * 4)) / 5)) + CW
	CY[20] = PY[8] - CH - 10
	CX[21] = PX[8] + (3 * ((PW[8] - (CW * 4)) / 5)) + (2 * CW)
	CY[21] = PY[8] - CH - 10
	CX[22] = PX[8] + (4 * ((PW[8] - (CW * 4)) / 5)) + (3 * CW)
	CY[22] = PY[8] - CH - 10
	CX[23] = 500 - CW - 10
	CY[23] = 140
	CX[24] = 500
	CY[24] = 100
	CX[25] = 500 + CW + 20
	CY[25] = 80
	CX[26] = 500 + (CW * 2) + 40
	CY[26] = 100
	CX[27] = 500 + (CW * 3) + 50
	CY[27] = 140
	CX[28] = 500 + (CW * 3) + 78
	CY[28] = 177
	CX[29] = 920 - (CW * 2) - 40
	CY[29] = 150
	CX[30] = 920 - CW - 20
	CY[30] = 110
	CX[31] = 920
	CY[31] = 90
	CX[32] = 920 + CW + 20
	CY[32] = 110
	CX[33] = 920 + (CW * 2) + 40
	CY[33] = 150
	CX[34] = 920 + (CW * 3) + 60
	CY[34] = 190
	CX[35] = 920 + (CW * 4) + 70
	CY[35] = 240
	CX[36] = 920 + (CW * 5) + 75
	CY[36] = 300

	# Falling rocks image and size
	rock = pygame.image.load('images/rock.png').convert_alpha()
	rockSize = rock.get_size()
	RW, RH = rockSize[0], rockSize[1]

	# Falling rocks placement
	RX = [0] * 3
	for i in range(3):
		RX[i] = random.randrange(PX[0], PX[10] + PW[10], 50)

	RY = [-100, -300, -200]
	RYoriginal = (-100, -300, -200)

	# Program details
	clock = pygame.time.Clock()
	FPS = 20
	inPlay = True
	onPlat = False
	score = 0

	# Main game loop
	while inPlay:

		# Displaying images
		screen.fill((0, 0, 0))
		screen.blit(background, (backgroundX, backgroundY))

		# Displaying coins collected
		font2 = pygame.font.SysFont('Myriad Pro', 35)
		scoreTitle = font2.render('COINS: ' + str(score), 1, WHITE)
		screen.blit(scoreTitle, (20, 20))

		# Displaying platforms + coins + falling rocks
		for i in range(len(PX)):
			screen.blit(platform_list[i], (PX[i], PY[i]))
		for i in range(len(CX)):
			screen.blit(coin, (CX[i], CY[i]))
		screen.blit(marioPic[marioPicNum], (marioX, marioY))
		for i in range(len(RX)):
			screen.blit(rock, (RX[i], RY[i]))
		screen.blit(floor, (floorX, floorY))

		# Moving the falling rocks down the screen
		for i in range(len(RX)):
			RY[i] += 5

		# Displaying a new rock if falling rock moves off screen
		for i in range(len(RX)):
			if RY[i] > h:
				RX[i] = random.randrange(PX[0], PX[10] + PW[10], 50)
				RY[i] = RYoriginal[i]

		# Keyboard movement
		pygame.event.get()
		keys = pygame.key.get_pressed()

		# Other screens:
		# Escape button
		if keys[pygame.K_ESCAPE]:
			inPlay = False

		# Winning screen
		if score == 37:
			# 'pygame.time.wait()' freezes screen for a specific amt of time
			# Value = time in milliseconds
			# Link to source: https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame
			pygame.time.wait(500)
			inPlay = False
			winScreen()

		# Losing screen
		if marioY + marioH >= h:
			pygame.time.wait(500)
			loseScreen()

		# Left movement
		# If left key is pressed and mario isn't touching left boundry
		if keys[pygame.K_LEFT] and backgroundX <= 0:
			walk = 0

			# Mario can't move forward if platform is in the way
			for i in range(len(PX)):
				if marioX != PX[i] + PW[i]:
					walk += 1

			if walk == 11:
				marioVx = -RUN_SPEED
				marioDir = "left"

				# Moving the background, floor, platforms, coins, & falling rocks
				backgroundX += RUN_SPEED * 2
				floorX += RUN_SPEED * 2
				for i in range(len(PX)):
					PX[i] += RUN_SPEED * 2
				for i in range(len(CX)):
					CX[i] += RUN_SPEED * 2
				for i in range(len(RX)):
					RX[i] += RUN_SPEED * 2
				if onPlat:
					marioPicNum = nextLeftPic[marioPicNum]

			else:
				marioVx = 0

		# Right movement
		# If right key is pressed and mario isn't touching right boundry
		elif keys[pygame.K_RIGHT] and backgroundX >= w - backgroundSize[0]:
			walk = 0

			# Mario can't move forward if platform is in the way
			for i in range(len(PX)):
				if marioX + marioW != PX[i]:
					walk += 1

			if walk == 11:
				marioVx = RUN_SPEED
				marioDir = "right"

				# Moving the background, floor, platforms, coins, & falling rocks
				backgroundX -= RUN_SPEED * 2
				floorX -= RUN_SPEED * 2
				for i in range(len(PX)):
					PX[i] -= RUN_SPEED * 2
				for i in range(len(CX)):
					CX[i] -= RUN_SPEED * 2
				for i in range(len(RX)):
					RX[i] -= RUN_SPEED * 2
				if onPlat == True:
					marioPicNum = nextRightPic[marioPicNum]

			else:
				marioVx = 0

		# Standing still
		else:
			marioVx = 0
			if marioDir == "left":
				marioPicNum = 0
			elif marioDir == "right":
				marioPicNum = 4

		# Up movement
		# If up key is pressed and mario is on a platform
		if keys[pygame.K_UP] and onPlat == True:
			marioVy = JUMP_SPEED
			if marioDir == "left":
				marioPicNum = 8
			elif marioDir == "right":
				marioPicNum = 9

		# Down movement
		# If doen key is pressed
		if keys[pygame.K_DOWN]:
			marioVx = 0
			marioVy = -JUMP_SPEED
			if marioDir == "left":
				marioPicNum = 10
			elif marioDir == "right":
				marioPicNum = 11

		# Updating mario's velocity and coordinates
		marioVy += GRAVITY
		marioX += marioVx
		marioY += marioVy

		# Keeping mario within screen
		if marioX <= PX[0]:
			marioX = PX[0]
		if marioX + marioW >= PX[10] + PW[10]:
			marioX = PX[10] + PW[10] - marioW
		if marioY + marioH > h:
			marioY = h - marioH
			marioVy = 0
		if marioX != w / 2 - 50:
			marioX = w / 2 - 50

		# Detecting if mario is on a platform with the 'platform_detect' function
		plat0 = platform_detect(marioX, marioY, marioW, marioH, PX[0], PY[0], PW[0],
		                        PH[0], marioVy)
		plat1 = platform_detect(marioX, marioY, marioW, marioH, PX[1], PY[1], PW[1],
		                        PH[1], marioVy)
		plat2 = platform_detect(marioX, marioY, marioW, marioH, PX[2], PY[2], PW[2],
		                        PH[2], marioVy)
		plat3 = platform_detect(marioX, marioY, marioW, marioH, PX[3], PY[3], PW[3],
		                        PH[3], marioVy)
		plat4 = platform_detect(marioX, marioY, marioW, marioH, PX[4], PY[4], PW[4],
		                        PH[4], marioVy)
		plat5 = platform_detect(marioX, marioY, marioW, marioH, PX[5], PY[5], PW[5],
		                        PH[5], marioVy)
		plat6 = platform_detect(marioX, marioY, marioW, marioH, PX[6], PY[6], PW[6],
		                        PH[6], marioVy)
		plat7 = platform_detect(marioX, marioY, marioW, marioH, PX[7], PY[7], PW[7],
		                        PH[7], marioVy)
		plat8 = platform_detect(marioX, marioY, marioW, marioH, PX[8], PY[8], PW[8],
		                        PH[8], marioVy)
		plat9 = platform_detect(marioX, marioY, marioW, marioH, PX[9], PY[9], PW[9],
		                        PH[9], marioVy)
		plat10 = platform_detect(marioX, marioY, marioW, marioH, PX[10], PY[10],
		                         PW[10], PH[10], marioVy)

		# Detereming which platform mario is on
		# Updating mario's y-coordinate accordingly
		if plat0:
			marioY = PY[0] - marioH
			marioVy = 0
			onPlat = True
		elif plat1:
			marioY = PY[1] - marioH
			marioVy = 0
			onPlat = True
		elif plat2:
			marioY = PY[2] - marioH
			marioVy = 0
			onPlat = True
		elif plat3:
			marioY = PY[3] - marioH
			marioVy = 0
			onPlat = True
		elif plat4:
			marioY = PY[4] - marioH
			marioVy = 0
			onPlat = True
		elif plat5:
			marioY = PY[5] - marioH
			marioVy = 0
			onPlat = True
		elif plat6:
			marioY = PY[6] - marioH
			marioVy = 0
			onPlat = True
		elif plat7:
			marioY = PY[7] - marioH
			marioVy = 0
			onPlat = True
		elif plat8:
			marioY = PY[8] - marioH
			marioVy = 0
			onPlat = True
		elif plat9:
			marioY = PY[9] - marioH
			marioVy = 0
			onPlat = True
		elif plat10:
			marioY = PY[10] - marioH
			marioVy = 0
			onPlat = True
		else:
			onPlat = False

		# Determening if mario collects a coin
		for i in range(len(CX)):
			coinCollide = pygame.Rect(CX[i], CY[i], CW, CH)
			marioCollide = pygame.Rect(marioX, marioY, marioW, marioH)

			# Checking if mario touches a coin
			if marioCollide.colliderect(coinCollide):
				# Moving coin off screen to make it 'disappear'
				CX[i] = -1000
				CY[i] = -1000

				# Updating 'coins collected' score
				score += 1
				print('+1 Coin!')

		# Checking if mario collides with the falling rocks
		for i in range(len(RX)):
			rockCollide = pygame.Rect(RX[i], RY[i], RW, RH)
			marioCollide = pygame.Rect(marioX, marioY, marioW, marioH)

			# Ending the game if collision is detected
			if rockCollide.colliderect(marioCollide):
				pygame.time.delay(500)
				inPlay = False
				loseScreen()

		# Updating screen
		pygame.display.update()
		clock.tick(FPS)


# Calling the first function (intro screen)
# Other functions will subsequently be called
intro()
