import pygame
import time
<<<<<<< HEAD
import random #Se llaman todas las funciones necesarias para desarrollar el juego

#Se inicializan funciones dentro de pygame
pygame.font.init()
pygame.mixer.init()

#Configuración de la pantalla
width, height = 1200, 800 #Ancho y alto de la pantalla
myScreen = pygame.display.set_mode((width, height)) #Se utilizan las variables definidas anteriormente
pygame.display.set_caption("Space Wars") #Se muestra el nombre del juego

#Configuración de fuentes y fondo
font = pygame.font.Font("assets/fonts/Silkscreen-Bold.ttf", 35) #Fuente
back = pygame.transform.scale(pygame.image.load("assets/background.jpeg"), (width, height)) #Fondo
icon = pygame.image.load("assets/extras/asteroid.png") #Ícono del juego
pygame.display.set_icon(icon) #Se muestra el ícono

#Configuración de música
pygame.mixer.music.load("assets/sound/music.mp3") #Música del juego
pygame.mixer.music.play(-1)

#Efectos de sonido
explosionSound = pygame.mixer.Sound("assets/sound/explosion.mp3") #Explosión
gunshotSound = pygame.mixer.Sound("assets/sound/plasma-gunshot.mp3") #Disparo
selected = pygame.mixer.Sound("assets/sound/selected.mp3") #Seleccionado

#Mutear música y efectos
musicMuted = False
effectsMuted = False

#Botones
buttonWidth, buttonHeight = 50, 50 #Tamaño de los botones
homeButton = pygame.transform.scale(pygame.image.load("assets/buttons/home.png"), (buttonWidth, buttonHeight)) 
muteButton = pygame.transform.scale(pygame.image.load("assets/buttons/mute.png"), (buttonWidth, buttonHeight)) 
soundButton = pygame.transform.scale(pygame.image.load("assets/buttons/sound.png"), (buttonWidth, buttonHeight))
#Cálculos para colocar botones de muteo/desmuteo/home
buttonX = 10  #Margen izquierdo
buttonY = 10  #Margen arriba
homeButtonX = width - buttonX - buttonWidth 

#Configuración de jugador
player = pygame.image.load("assets/ships/spaceship2.png") #Nave
playerW = 70 #Tamaño
playerH = 70 #Tamaño
player = pygame.transform.scale(player, (playerW, playerH)) #Se crea el jugador

#Configuración de moneda
coin = pygame.image.load("assets/extras/coin.png") #Moneda
coinW = 50 #Tamaño
coinH = 25 #Tamaño
coin = pygame.transform.scale(coin, (coinW, coinH)) #Se crea la moneda

#Configuración de escudo
shield = pygame.image.load("assets/extras/shield.png") #Escudo
shieldW = 40 #Tamaño
shieldH = 40 #Tamaño
shield = pygame.transform.scale(shield, (shieldW, shieldH)) #Se crea la escudo

#Configuración de vida
life = pygame.image.load("assets/extras/life.png") #Vida
lifeW = 25 #Tamaño
lifeH = 25 #Tamaño
life = pygame.transform.scale(life, (lifeW, lifeH)) #Se crea la vida

#Configuración de estrella especial
specialStar = pygame.image.load("assets/extras/specialStar.png") #Estrella especial
specialStarW = 25 #Tamaño
specialStarH = 25 #Tamaño
specialStar = pygame.transform.scale(specialStar, (specialStarW, specialStarH)) #Se crea la estrella especial

#Configuración de roca
rock = pygame.image.load("assets/extras/rock.png") #Roca
rockW = 15 #Tamaño
rockH = 15 #Tamaño
rock = pygame.transform.scale(rock, (rockW, rockH)) #Se crea la roca

#Configuración de asteroide
asteroid = pygame.image.load("assets/extras/asteroid.png") #Asteroide
asteroidW = 80 #Tamaño
asteroidH = 80 #Tamaño
asteroid = pygame.transform.scale(asteroid, (asteroidW, asteroidH)) #Se crea el asteroide

#Configuración de explosion de roca/asteroide después de impactar
=======
import random

pygame.font.init()
pygame.mixer.init()

#Screen - config
width, height = 1200, 800
myScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Wars")

#Fonts and background - config
font = pygame.font.Font("assets/fonts/Silkscreen-Bold.ttf", 35)
back = pygame.transform.scale(pygame.image.load("assets/background.jpeg"), (width, height))
icon = pygame.image.load("assets/extras/asteroid.png")
pygame.display.set_icon(icon)

#Music
pygame.mixer.music.load("assets/sound/music.mp3")
pygame.mixer.music.play(-1)

#Sound effects
explosionSound = pygame.mixer.Sound("assets/sound/explosion.mp3")
gunshotSound = pygame.mixer.Sound("assets/sound/plasma-gunshot.mp3")
selected = pygame.mixer.Sound("assets/sound/selected.mp3")

#Muting
musicMuted = False
effectsMuted = False

#Buttons
buttonWidth, buttonHeight = 50, 50
homeButton = pygame.transform.scale(pygame.image.load("assets/buttons/home.png"), (buttonWidth, buttonHeight))
muteButton = pygame.transform.scale(pygame.image.load("assets/buttons/mute.png"), (buttonWidth, buttonHeight))
soundButton = pygame.transform.scale(pygame.image.load("assets/buttons/sound.png"), (buttonWidth, buttonHeight))

#Player - config
player = pygame.image.load("assets/ships/spaceship2.png")
playerW = 70
playerH = 70
player = pygame.transform.scale(player, (playerW, playerH))

#Stars - config
star = pygame.image.load("assets/extras/star.png")
starW = 15
starH = 15
star = pygame.transform.scale(star, (starW, starH))

#Asteroids - config
asteroid = pygame.image.load("assets/extras/asteroid.png")
asteroidW = 80
asteroidH = 80
asteroid = pygame.transform.scale(asteroid, (asteroidW, asteroidH))

#Explosion - config (asteroid/star - after collision)
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
explosion = pygame.image.load("assets/extras/explosion.png")
explosion1 = pygame.transform.scale(explosion, (asteroidW, asteroidH))
explosion2 = pygame.transform.scale(explosion, (40, 40))

<<<<<<< HEAD
#Configuración de bala
bullet = pygame.image.load("assets/extras/bullet.png") #Bala
bulletW = 15 #Tamaño
bulletH = 15 #Tamaño
bullet = pygame.transform.scale(bullet, (bulletW, bulletH)) #Se crea la bala

#Velocidad: General, balas, monedas y asteroides
speed = 10 #Velocidad general
asteroidSpeed = 8 #Velocidad asteroides
coinSpeed = 15 #Velocidad monedas
bulletSpeed = 13 #Velocidad balas

#Masks
playerMask = pygame.mask.from_surface(player)
coinMask = pygame.mask.from_surface(coin)
rockMask = pygame.mask.from_surface(rock)
asteroidMask = pygame.mask.from_surface(asteroid)
bulletMask = pygame.mask.from_surface(bullet)

#Función: Menu
def menu():
    run = True #El juego está corriendo, se muestra el menú
=======
#Bullets - config
bullet = pygame.image.load("assets/extras/bullet.png")
bulletW = 15
bulletH = 15
bullet = pygame.transform.scale(bullet, (bulletW, bulletH))

#General, asteroids and bullets - speed
speed = 10
asteroidSpeed = 8
bulletSpeed = 13

#Masks
playerMask = pygame.mask.from_surface(player)
starMask = pygame.mask.from_surface(star)
asteroidMask = pygame.mask.from_surface(asteroid)
bulletMask = pygame.mask.from_surface(bullet)

#Function - Menu
def menu():
    run = True
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262

    while run:
        myScreen.blit(back, (0, 0))

<<<<<<< HEAD
        #Detecta la posición del mouse
        mousePos = pygame.mouse.get_pos()

        #Renderiza los botones
=======
        #Detect mouse position
        mousePos = pygame.mouse.get_pos()

        #Render buttons
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        title = font.render("Welcome to Space Wars!", True, "white")
        
        playB = font.render("Play", True, "white")
        optionsB = font.render("Options", True, "white")
        quitB = font.render("Quit", True, "white")

        titleRect = title.get_rect(center=(width/2, height/4))
        playRect = playB.get_rect(center=(width/2, height/2))
        optionsRect = optionsB.get_rect(center=(width/2, height/2 + 100))
        quitRect = quitB.get_rect(center=(width/2, height/2 + 200))

<<<<<<< HEAD
        #Define los colores de los botones
=======
        #Define button colors
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        playColor = "gray" if playRect.collidepoint(mousePos) else "white"
        optionsColor = "gray" if optionsRect.collidepoint(mousePos) else "white"
        quitColor = "gray" if quitRect.collidepoint(mousePos) else "white"

<<<<<<< HEAD
        #Re-renderiza los botones con los colores actualizados
=======
        #Re-render buttons with the updated colors
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        playB = font.render("Play", True, playColor)
        optionsB = font.render("Options", True, optionsColor)
        quitB = font.render("Quit", True, quitColor)

<<<<<<< HEAD
        #Dibuja los botones
=======
        #Draw buttons
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        myScreen.blit(title, titleRect)
        myScreen.blit(playB, playRect)
        myScreen.blit(optionsB, optionsRect)
        myScreen.blit(quitB, quitRect)

        pygame.display.update()

<<<<<<< HEAD
        #Manejo de eventos
=======
        #Event handling
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playRect.collidepoint(event.pos):
                    selected.play()
                    run = False
                elif optionsRect.collidepoint(event.pos):
                    selected.play()
                    optionsMenu()
                elif quitRect.collidepoint(event.pos):
                    selected.play()
                    pygame.quit()
                    quit()

<<<<<<< HEAD
        pygame.time.delay(500)

#Función: Menú de opciones   
def optionsMenu():
    #Define variables globales
    global musicMuted, effectsMuted
    #Se muestra el menú de opciones
=======
        pygame.time.delay(100)

#Function - Options menu     
def optionsMenu():
    #Define global variables
    global musicMuted, effectsMuted
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    run = True

    while run:
        myScreen.blit(back, (0, 0))
<<<<<<< HEAD
        #Detecta la posición del mouse
        mousePos = pygame.mouse.get_pos()

        #Renderiza las opciones
=======
        #Detect mouse position
        mousePos = pygame.mouse.get_pos()

        #Render options
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        title = font.render("Options", True, "white")
        muteMusic = font.render(f"Music: {'ON' if not musicMuted else 'OFF'}", True, "white" if not musicMuted else "gray")
        muteEffects = font.render(f"Effects: {'ON' if not effectsMuted else 'OFF'}", True, "white" if not effectsMuted else "gray")
        goBack = font.render("Back to Menu", True, "white")

        titleRect = title.get_rect(center=(width/2, height/4))
        muteMusicRect = muteMusic.get_rect(center=(width/2, height/2))
        muteEffectsRect = muteEffects.get_rect(center=(width/2, height/2 + 100))
        goBackRect = goBack.get_rect(center=(width/2, height/2 + 200))

<<<<<<< HEAD
        #Determina el color del botón
        goBackColor = "gray" if goBackRect.collidepoint(mousePos) else "white"

        #Re-renderiza los botones con los colores actualizados
=======
        #Determine button color
        goBackColor = "gray" if goBackRect.collidepoint(mousePos) else "white"

        #Re-render button with the updated color
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        goBack = font.render("Back to Menu", True, goBackColor)

        myScreen.blit(title, titleRect)
        myScreen.blit(muteMusic, muteMusicRect)
        myScreen.blit(muteEffects, muteEffectsRect)
        myScreen.blit(goBack, goBackRect)

        pygame.display.update()

<<<<<<< HEAD
        #Manejo de eventos
=======
        #Event handling
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if muteMusicRect.collidepoint(event.pos):
                    musicMuted = not musicMuted
<<<<<<< HEAD
                    pygame.mixer.music.set_volume(0 if musicMuted else 0.3)
                    selected.play()
                elif muteEffectsRect.collidepoint(event.pos):
                    effectsMuted = not effectsMuted
                    selected.set_volume(0 if effectsMuted else 0.3)
                    explosionSound.set_volume(0 if effectsMuted else 0.3)
                    gunshotSound.set_volume(0 if effectsMuted else 0.3)
                    #coinSound.set_volume(0 if effectsMuted else 0.3)
=======
                    pygame.mixer.music.set_volume(0 if musicMuted else 0.5)
                    selected.play()
                elif muteEffectsRect.collidepoint(event.pos):
                    effectsMuted = not effectsMuted
                    selected.set_volume(0 if effectsMuted else 1)
                    explosionSound.set_volume(0 if effectsMuted else 1)
                    gunshotSound.set_volume(0 if effectsMuted else 1)
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
                    selected.play()
                elif goBackRect.collidepoint(event.pos):
                    selected.play()
                    run = False
                    break

        pygame.time.delay(100)

<<<<<<< HEAD
#Función: Dibujar objetos en la pantalla
def draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, rocks, asteroids, coins, coinsCollected, bullets):
    myScreen.blit(back, (0, 0))

    #Dibujar tiempo
    timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, "white")
    myScreen.blit(timeRecord, (10, 10))

    #Dibujar puntos
    pointsRecord = font.render(f"Points: {points}", 1, "white")
    myScreen.blit(pointsRecord, (timeRecord.get_width() + 50, 10))

    #Dibujar botón home
    myScreen.blit(homeButton, (homeButtonX, buttonY))
    
    #Dibujar botones sonido y mute
=======
#Function - Draw objects in screen
def draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, stars, asteroids, bullets):
    myScreen.blit(back, (0, 0))

    #Draw time
    timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, "white")
    myScreen.blit(timeRecord, (10, 10))

    #Draw points
    pointsRecord = font.render(f"Points: {points}", 1, "white")
    myScreen.blit(pointsRecord, (timeRecord.get_width() + 50, 10))

    buttonX = 10  #Left margin
    buttonY = 10  #Top margin
    homeButtonX = width - buttonX - buttonWidth

    #Draw home button
    myScreen.blit(homeButton, (homeButtonX, buttonY))
    
    #Draw sound and mute button
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    if musicMuted:
        myScreen.blit(soundButton, (homeButtonX - buttonWidth - 10, buttonY))
    else:
        myScreen.blit(muteButton, (homeButtonX - buttonWidth - 10, buttonY))

<<<<<<< HEAD
    #Dibujar vidas y escudo

    #Dibujar rocas
    for rockObj in rocks:
        if rockObj["state"] == "normal":
            myScreen.blit(rockObj["image"], rockObj["position"])
        elif rockObj["state"] == "explosion":
            myScreen.blit(explosion2, rockObj["position"])

    #Dibujar asteroides
=======
    #Draw stars
    for starObj in stars:
        if starObj["state"] == "normal":
            myScreen.blit(starObj["image"], starObj["position"])
        elif starObj["state"] == "explosion":
            myScreen.blit(explosion2, starObj["position"])

    #Draw asteroids
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    for asteroidObj in asteroids:
        if asteroidObj["state"] == "normal":
            myScreen.blit(asteroidObj["image"], asteroidObj["position"])
        elif asteroidObj["state"] == "explosion" or asteroidObj["state"] == "collision":
            myScreen.blit(explosion1, asteroidObj["position"])

<<<<<<< HEAD
    #Dibujar monedas
    for coinObj in coins:
        myScreen.blit(coinObj["image"], coinObj["position"])

    coinIconX = timeRecord.get_width() + pointsRecord.get_width() + 80
    myScreen.blit(coin, (coinIconX, 25))

    coinRecord = font.render(f"{coinsCollected}", 1, "white")
    myScreen.blit(coinRecord, (coinIconX + coinW + 10, 10))

    #Dibujar balas
    for bulletPosition in bullets:
        myScreen.blit(bullet, bulletPosition)

    #Dibujar jugador
=======
    #Draw bullets
    for bulletPosition in bullets:
        myScreen.blit(bullet, bulletPosition)

    #Draw player
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    if playerState == "normal":
        myScreen.blit(player, playerPosition)
    elif playerState == "collision":
        myScreen.blit(explosion1, playerPosition)
    
    pygame.display.update()

<<<<<<< HEAD
#Functión: Juego principal
def main():
    #Para modificar variables globales
    global musicMuted, effectsMuted

    #El juego está corriendo y el jugador no ha sido golpeado
    run = True
    playerHit = False
    playerState = "normal"
    playerPosition = [width // 2 - playerW, height - playerH - 10]

    #Se setean los contadores
=======
#Function - Main game
def main():
    #To modify global variables
    global musicMuted, effectsMuted

    run = True
    playerHit = False

    playerState = "normal"
    playerPosition = [width // 2 - playerW, height - playerH - 10]

>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    points = 0

<<<<<<< HEAD
    #Manejo de rocas
    rockAdd = 1000
    rockCount = 0
    rocks = []

    #Manejo de asteroides
    asteroidAdd = random.uniform(3000, 5000)
    asteroidCount = 0
    asteroidsSpawned = 0
    asteroids = []

    #Manejo de monedas
    coins = []
    coinsCollected = 0

    #Manejo de balas
=======
    starAdd = 1000
    starCount = 0
    stars = []

    asteroidAdd = random.uniform(3000, 5000)
    asteroidCount = 0
    asteroids = []

>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
    bullets = []
    shootInterval = 1000 
    lastShootTime = 0

<<<<<<< HEAD
    #Comienza el juego
    while run:

        #Se maneja el tiempo y el contador de asteroides
        currentTime = pygame.time.get_ticks()
        rockCount += clock.tick(60)
        asteroidCount += clock.tick(60)
        elapsedTime = time.time() - startTime

        #Si el jugador pierde
=======
    while run:
        currentTime = pygame.time.get_ticks()
        starCount += clock.tick(60)
        asteroidCount += clock.tick(60)
        elapsedTime = time.time() - startTime

>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        if playerState == "collision":
            pygame.time.delay(2000)
            myScreen.blit(back, (0, 0))
            playerHit = True

<<<<<<< HEAD
        #Se agregan rocas
        if rockCount > rockAdd:
            numRocks = random.randint(1, 8)

            for _ in range(numRocks):
                rockX = random.randint(0, width - rockW)
                rockY = -rockH
                rocks.append({
                    "position": [rockX, rockY], 
                    "image": rock, 
                    "state": "normal", 
                    "destroyTime": None
                })
            rockAdd = max(200, rockAdd - 50)
            rockCount = 0

        #Se agregan asteroides
=======
        #Add stars
        if starCount > starAdd:
            numStars = random.randint(1, 10)

            for _ in range(numStars):
                starX = random.randint(0, width - starW)
                starY = -starH
                stars.append({
                    "position": [starX, starY], 
                    "image": star, 
                    "state": "normal", 
                    "destroyTime": None
                })
            starAdd = max(200, starAdd - 50)
            starCount = 0

        #Add asteroids
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        if asteroidCount > asteroidAdd:
            asteroidX = random.randint(0, width - asteroidW)
            asteroidY = -asteroidH
            asteroids.append({
                "position": [asteroidX, asteroidY],
                "image": asteroid,
                "state": "normal",
                "destroyTime": None
            })
<<<<<<< HEAD
            asteroidsSpawned += 1
            if asteroidsSpawned % 5 == 0 and asteroidsSpawned != 0:
                coinX = random.randint(0, width - coinW)
                coinY = -coinH
                coins.append ({
                    "position": [coinX, coinY],
                    "image": coin,
                    "state": "normal",
                    "destroyTime": None
                })
=======
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
            asteroidAdd = random.uniform(3000, 5000)
            asteroidCount = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
<<<<<<< HEAD
            #Se chequean los clicks del mouse para manejar los eventos
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #Cliquea el botón home
                if homeButton.get_rect(topleft=(homeButtonX, buttonY)).collidepoint(mousePos):
                    selected.play()
                    return
                #Cliquea el botón mutear
                if muteButton.get_rect(topleft=(homeButtonX - buttonWidth - 10, buttonY)).collidepoint(mousePos):
                    if musicMuted:
                        #Desmutear
                        musicMuted = False
                        effectsMuted = False
                        pygame.mixer.music.set_volume(0.3)
                        selected.set_volume(0.3)
                        explosionSound.set_volume(0.3)
                        gunshotSound.set_volume(0.3)
                        #coinSound.set_volume(0.3)
                        selected.play()
                    else:
                        #Mutear
                        musicMuted = True
                        effectsMuted = True
                        pygame.mixer.music.set_volume(0)
                        selected.set_volume(0)
                        explosionSound.set_volume(0)
                        gunshotSound.set_volume(0)
                        #coinSound.set_volume(0)
                        selected.play()

        #Controladores de juego
=======
            # Check for mouse clicks to handle events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #Home button click
                if homeButton.get_rect(topleft=(width - 10 - buttonWidth, 10)).collidepoint(mousePos):
                    selected.play()
                    menu()
                #Mute button click
                if muteButton.get_rect(topleft=(width - 10 - 2 * buttonWidth - 10, 10)).collidepoint(mousePos):
                    musicMuted = not musicMuted
                    effectsMuted = not effectsMuted
                    pygame.mixer.music.set_volume(0 if musicMuted else 0.5)
                    selected.set_volume(0 if effectsMuted else 1)
                    explosionSound.set_volume(0 if effectsMuted else 1)
                    gunshotSound.set_volume(0 if effectsMuted else 1)
                #Unmute button click
                if soundButton.get_rect(topleft=(width - 10 - 2 * buttonWidth - 10, 10)).collidepoint(mousePos):
                    selected.play()
                    pygame.mixer.music.set_volume(0.5)
                    selected.set_volume(1)
                    explosionSound.set_volume(1)
                    gunshotSound.set_volume(1)

        #Game controllers
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and playerPosition[0] - speed >= 0:
            playerPosition[0] -= speed

        if keys[pygame.K_RIGHT] and playerPosition[0] + speed <= width - playerW:
            playerPosition[0] += speed

        if keys[pygame.K_SPACE] and currentTime - lastShootTime > shootInterval:
            gunshotSound.play()
            bulletX = playerPosition[0] + playerW // 2 - bulletW // 2
            bulletY = playerPosition[1] - bulletH
            bullets.append([bulletX, bulletY])
            lastShootTime = currentTime

<<<<<<< HEAD

        #Se actualizan las posiciones de las monedas
        for coinObj in coins[:]:
            coinObj["position"][1] += coinSpeed

            if coinObj["position"][1] > height:
                coins.remove(coinObj)
            else:
                over = (coinObj["position"][1] - playerPosition[0], coinObj["position"][1] - playerPosition[1])
                if playerMask.overlap(coinMask, over):
                    coinsCollected += 1
                    coins.remove(coinObj)
                    #coinSound.play()
            
        #Se actualizan las posiciones de las rocas
        for rockObj in rocks[:]:
            if rockObj["state"] == "normal":
                rockObj["position"][1] += speed

                if rockObj["position"][1] > height:
                    rocks.remove(rockObj)
                else:
                    over = (rockObj["position"][0] - playerPosition[0], rockObj["position"][1] - playerPosition[1])
                    if playerMask.overlap(rockMask, over):
                        rockObj["state"] = "explosion"
                        playerState = "collision"
                        rockObj["destroyTime"] = currentTime
                        explosionSound.play()
                        break
            elif rockObj["state"] == "explosion":
                if currentTime - rockObj["destroyTime"] > 1000:
                    rocks.remove(rockObj)
        
        #Se actualizan las posiciones de los asteroides
=======
        #Update positions - stars
        for starObj in stars[:]:
            if starObj["state"] == "normal":
                starObj["position"][1] += speed

                if starObj["position"][1] > height:
                    stars.remove(starObj)
                else:
                    over = (starObj["position"][0] - playerPosition[0], starObj["position"][1] - playerPosition[1])
                    if playerMask.overlap(starMask, over):
                        starObj["state"] = "explosion"
                        playerState = "collision"
                        starObj["destroyTime"] = currentTime
                        explosionSound.play()
                        break
            elif starObj["state"] == "explosion":
                if currentTime - starObj["destroyTime"] > 1000:
                    stars.remove(starObj)
        
        #Update positions - asteroids
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        for asteroidObj in asteroids[:]:
            if asteroidObj["state"] == "normal":
                asteroidObj["position"][1] += asteroidSpeed
            
                if asteroidObj["position"][1] > height:
                    asteroids.remove(asteroidObj)
                else:
                    over = (asteroidObj["position"][0] - playerPosition[0], asteroidObj["position"][1] - playerPosition[1])
                    if playerMask.overlap(asteroidMask, over):
                        asteroidObj["state"] = "collision"
                        playerState = "collision"
                        asteroidObj["destroyTime"] = currentTime
                        explosionSound.play()
                        break
            elif asteroidObj["state"] == "explosion":
                if currentTime - asteroidObj["destroyTime"] > 1000:
                    asteroids.remove(asteroidObj)

<<<<<<< HEAD
        #Se actualizan las posiciones de las balas / Explosión con asteroides
=======
        #Update positions - bullets / Collision with asteroids - verify
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        for bulletPosition in bullets[:]:
            bulletPosition[1] -= bulletSpeed
            
            if bulletPosition[1] < 0:
                bullets.remove(bulletPosition)
            else:
                for asteroidObj in asteroids[:]:
                    if asteroidObj["state"] == "normal":
                        over = (asteroidObj["position"][0] - bulletPosition[0], asteroidObj["position"][1] - bulletPosition[1])
                        if bulletMask.overlap(asteroidMask, over):
                            bullets.remove(bulletPosition)
                            asteroidObj["state"] = "explosion"
                            asteroidObj["destroyTime"] = currentTime
                            explosionSound.play()
                            points += 5
                            break
                            
<<<<<<< HEAD
        #Explosión de la nave: El jugador pierde el juego
=======
        #Collision - verify
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
        if playerHit:
            gameOver = font.render("Game Over", 2, "white")
            myScreen.blit(gameOver, (width / 2 - gameOver.get_width() / 2, height / 2 - gameOver.get_height() / 2))
            timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, "white")
            myScreen.blit(timeRecord, (width / 2 - timeRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 50))
            pointsRecord = font.render(f"Points: {points}", 1, "white")
            myScreen.blit(pointsRecord, (width / 2 - pointsRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 100))
            pygame.display.update()
<<<<<<< HEAD
            pygame.time.delay(3000)
            return

        draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, rocks, asteroids, coins, coinsCollected, bullets)

if __name__ == "__main__":
    while True:
        menu()
        main()
=======
            pygame.mixer.music.stop()
            pygame.time.delay(3000)
            menu()
            break

        draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, stars, asteroids, bullets)

if __name__ == "__main__":
    menu()
    main()
>>>>>>> ab87ec8202cd3f6bcbd68d9bef93a8d34b5a1262
