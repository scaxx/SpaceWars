import pygame
import time
import random #Se llaman todas las funciones necesarias para desarrollar el juego
import users #Importamos el archivo que maneja la lógica de logueo de usuarios

#Se inicializan funciones dentro de pygame
pygame.font.init()
pygame.mixer.init()

#Configuración de la pantalla
width, height = 1200, 800 #Ancho y alto de la pantalla
myScreen = pygame.display.set_mode((width, height)) #Se utilizan las variables definidas anteriormente
pygame.display.set_caption("Space Wars") #Se muestra el nombre del juego

#Configuración de fuentes y fondo
cianNeon = (0, 255, 245) #Color para las letras
cianNeonOscuro = (0, 180, 220) #Color para seleccionado
font = pygame.font.Font("assets/fonts/Silkscreen-Regular.ttf", 35) #Fuente
back = pygame.transform.scale(pygame.image.load("assets/backgrounds/background6.jpeg"), (width, height)) #Fondo
icon = pygame.image.load("assets/icon/icon.png") #Ícono del juego
pygame.display.set_icon(icon) #Se muestra el ícono

#Configuración de música
pygame.mixer.music.load("assets/sound/music.mp3") #Música del juego
pygame.mixer.music.play(-1)

#Efectos de sonido
explosionSound = pygame.mixer.Sound("assets/sound/explosion.mp3") #Explosión
gunshotSound = pygame.mixer.Sound("assets/sound/plasma-gunshot.mp3") #Disparo
coinSound = pygame.mixer.Sound("assets/sound/coin.mp3") #Moneda
shieldSound = pygame.mixer.Sound("assets/sound/shield.mp3") #Escudo
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
coinW = 40 #Tamaño
coinH = 40 #Tamaño
coin = pygame.transform.scale(coin, (coinW, coinH)) #Se crea la moneda

#Configuración de escudo
shield = pygame.image.load("assets/extras/shield.png") #Escudo
shieldW = 150 #Tamaño
shieldH = 90 #Tamaño
shield = pygame.transform.scale(shield, (shieldW, shieldH)) #Se crea la escudo

#Configuración de vida
life = pygame.image.load("assets/extras/life.png") #Vida
lifeW = 40 #Tamaño
lifeH = 40 #Tamaño
life = pygame.transform.scale(life, (lifeW, lifeH)) #Se crea la vida
#Vidas perdidas
emptyLife = pygame.image.load("assets/extras/emptyLife.png") #Vida vacía
emptyLife = pygame.transform.scale(emptyLife, (lifeW, lifeH)) #Se crea la vida vacía

#Configuración de estrella especial
specialStar = pygame.image.load("assets/extras/specialStar.png") #Estrella especial
specialStarW = 40 #Tamaño
specialStarH = 25 #Tamaño
specialStar = pygame.transform.scale(specialStar, (specialStarW, specialStarH)) #Se crea la estrella especial

#Configuración de roca
rock = pygame.image.load("assets/extras/rock.png") #Roca
rockW = 40 #Tamaño
rockH = 40 #Tamaño
rock = pygame.transform.scale(rock, (rockW, rockH)) #Se crea la roca

#Configuración de asteroide
asteroid = pygame.image.load("assets/extras/asteroid.png") #Asteroide
asteroidW = 80 #Tamaño
asteroidH = 80 #Tamaño
asteroid = pygame.transform.scale(asteroid, (asteroidW, asteroidH)) #Se crea el asteroide

#Configuración de explosion de roca/asteroide después de impactar
explosion = pygame.image.load("assets/extras/explosion.png")
explosion1 = pygame.transform.scale(explosion, (asteroidW, asteroidH))
explosion2 = pygame.transform.scale(explosion, (40, 40))

#Configuración de bala
bullet = pygame.image.load("assets/extras/bullet.png") #Bala
bulletW = 15 #Tamaño
bulletH = 15 #Tamaño
bullet = pygame.transform.scale(bullet, (bulletW, bulletH)) #Se crea la bala

#Velocidad: General, balas, monedas y asteroides
speed = 6 #Velocidad general
asteroidSpeed = 8 #Velocidad asteroides
shieldSpeed = 7 #Velocidad escudos
coinSpeed = 7 #Velocidad monedas
bulletSpeed = 11 #Velocidad balas

#Masks
playerMask = pygame.mask.from_surface(player)
coinMask = pygame.mask.from_surface(coin)
rockMask = pygame.mask.from_surface(rock)
asteroidMask = pygame.mask.from_surface(asteroid)
shieldMask = pygame.mask.from_surface(shield)
bulletMask = pygame.mask.from_surface(bullet)

#Función: Menu
def menu():
    run = True #El juego está corriendo, se muestra el menú

    while run:
        myScreen.blit(back, (0, 0))

        #Detecta la posición del mouse
        mousePos = pygame.mouse.get_pos()

        #Renderiza los botones
        title = font.render("Welcome to Space Wars!", True, cianNeon)
        
        playB = font.render("Play", True, cianNeon)
        newPlayerB = font.render("New Player", True, cianNeon)
        optionsB = font.render("Options", True, cianNeon)
        quitB = font.render("Quit", True, cianNeon)

        titleRect = title.get_rect(center=(width/2, height/2))
        playRect = playB.get_rect(center=(width/2, height/2))
        newPlayerRect = newPlayerB.get_rect(center=(width/2, height/2 + 100))
        optionsRect = optionsB.get_rect(center=(width/2, height/2 + 200))
        quitRect = quitB.get_rect(center=(width/2, height/2 + 300))

        #Define los colores de los botones
        playColor = cianNeonOscuro if playRect.collidepoint(mousePos) else cianNeon
        newPlayerColor = cianNeonOscuro if newPlayerRect.collidepoint(mousePos) else cianNeon
        optionsColor = cianNeonOscuro if optionsRect.collidepoint(mousePos) else cianNeon
        quitColor = cianNeonOscuro if quitRect.collidepoint(mousePos) else cianNeon

        #Re-renderiza los botones con los colores actualizados
        playB = font.render("Play", True, playColor)
        newPlayerB = font.render("New Player", True, newPlayerColor)
        optionsB = font.render("Options", True, optionsColor)
        quitB = font.render("Quit", True, quitColor)

        #Dibuja los botones
        myScreen.blit(title, titleRect)
        myScreen.blit(playB, playRect)
        myScreen.blit(newPlayerB, newPlayerRect)
        myScreen.blit(optionsB, optionsRect)
        myScreen.blit(quitB, quitRect)

        pygame.display.update()

        #Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playRect.collidepoint(event.pos):
                    selected.play()
                    run = False
                elif newPlayerRect.collidepoint(event.pos):
                    selected.play()
                    newPlayerMenu()
                elif optionsRect.collidepoint(event.pos):
                    selected.play()
                    optionsMenu()
                elif quitRect.collidepoint(event.pos):
                    selected.play()
                    pygame.quit()
                    quit()

        pygame.time.delay(500)

#Función: Menú para crear nuevo jugador
def newPlayerMenu():

    pygame.display.set_caption("Create New Player")

    #Iniciamos la variable donde se guardará el nombre (temporalmente)
    newPlayer = ""
    finished = False

    usersData = users.loadUsers() #Obtengo el diccionario de jugadores

    while finished == False:

        #Título principal
        enterNewPlayer = font.render("Enter new player name", True, cianNeon)
        enterNewPlayerRect = enterNewPlayer.get_rect(center=(width/2, height/2))
        myScreen.blit(enterNewPlayer, enterNewPlayerRect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    newPlayer = newPlayer[:-1]
                
                elif event.key == pygame.K_RETURN:

                    if newPlayer != "" and not users.userExists(newPlayer, usersData):

                        finished = True
                        newUserCreated = font.render("New user created successfully :)")
                        newUserCreatedRect = newUserCreated.get_rect(center=(width/2, height/2 + 100))
                        myScreen.blit(newUserCreated, newUserCreatedRect)

                    elif newPlayer != "" and users.userExists(newPlayer, usersData):

                        userInUseMessage = font.render("Username already in use :(")
                        userInUseMessageRect = userInUseMessage.get_rect(center=(width/2, height/2 + 100))
                        myScreen.blit(userInUseMessage, userInUseMessageRect)

                else:

                    #Lo que el usuario escribe
                    userInput = font.render(newPlayer, True, cianNeon)
                    userInputRect = userInput.get_rect(center=(width/2, height/2))
                    myScreen.blit(userInput, userInputRect)

                    newPlayer += event.unicode

    users.createUser(newPlayer, usersData)
    users.saveUsers(usersData)

    return newPlayer


#Función: Menú de opciones   
def optionsMenu():
    #Define variables globales
    global musicMuted, effectsMuted
    #Se muestra el menú de opciones
    run = True

    while run:
        myScreen.blit(back, (0, 0))
        #Detecta la posición del mouse
        mousePos = pygame.mouse.get_pos()

        #Renderiza las opciones
        title = font.render("Options", True, cianNeon)
        muteMusic = font.render(f"Music: {'ON' if not musicMuted else 'OFF'}", True, cianNeon if not musicMuted else cianNeonOscuro)
        muteEffects = font.render(f"Effects: {'ON' if not effectsMuted else 'OFF'}", True, cianNeon if not effectsMuted else cianNeonOscuro)
        goBack = font.render("Back to Menu", True, cianNeon)

        titleRect = title.get_rect(center=(width/2, height/4))
        muteMusicRect = muteMusic.get_rect(center=(width/2, height/2))
        muteEffectsRect = muteEffects.get_rect(center=(width/2, height/2 + 100))
        goBackRect = goBack.get_rect(center=(width/2, height/2 + 200))

        #Determina el color del botón
        goBackColor = cianNeonOscuro if goBackRect.collidepoint(mousePos) else cianNeon

        #Re-renderiza los botones con los colores actualizados
        goBack = font.render("Back to Menu", True, goBackColor)

        myScreen.blit(title, titleRect)
        myScreen.blit(muteMusic, muteMusicRect)
        myScreen.blit(muteEffects, muteEffectsRect)
        myScreen.blit(goBack, goBackRect)

        pygame.display.update()

        #Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if muteMusicRect.collidepoint(event.pos):
                    musicMuted = not musicMuted
                    pygame.mixer.music.set_volume(0 if musicMuted else 0.3)
                    selected.play()
                elif muteEffectsRect.collidepoint(event.pos):
                    effectsMuted = not effectsMuted
                    selected.set_volume(0 if effectsMuted else 0.3)
                    explosionSound.set_volume(0 if effectsMuted else 0.3)
                    gunshotSound.set_volume(0 if effectsMuted else 0.3)
                    coinSound.set_volume(0 if effectsMuted else 0.3)
                    selected.play()
                elif goBackRect.collidepoint(event.pos):
                    selected.play()
                    run = False
                    break

        pygame.time.delay(100)

#Función: Dibujar objetos en la pantalla
def draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, rocks, asteroids, coins, coinsCollected, shieldActive, lives, bullets, shields):
    myScreen.blit(back, (0, 0))

    #Dibujar tiempo
    timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, cianNeon)
    myScreen.blit(timeRecord, (10, 10))

    #Dibujar puntos
    pointsRecord = font.render(f"Points: {points}", 1, cianNeon)
    myScreen.blit(pointsRecord, (timeRecord.get_width() + 50, 10))

    #Dibujar botón home
    myScreen.blit(homeButton, (homeButtonX, buttonY))
    
    #Dibujar botones sonido y mute
    if musicMuted:
        myScreen.blit(soundButton, (homeButtonX - buttonWidth - 10, buttonY))
    else:
        myScreen.blit(muteButton, (homeButtonX - buttonWidth - 10, buttonY))

    #Dibujar monedas
    for coinObj in coins:
        myScreen.blit(coinObj["image"], coinObj["position"])

    coinIconX = timeRecord.get_width() + pointsRecord.get_width() + 80
    myScreen.blit(coin, (coinIconX, 15))

    coinRecord = font.render(f"{coinsCollected}", 1, cianNeon)
    myScreen.blit(coinRecord, (coinIconX + coinW + 10, 10))

    #Dibujar vidas
    livesBaseX = coinIconX + coinW + 10 + coinRecord.get_width() + 50
    for l in range(3):
        lifeIconX = livesBaseX + l * (lifeW + 15)
        if l < lives:
            myScreen.blit(life, (lifeIconX, 15))
        else:
            myScreen.blit(emptyLife, (lifeIconX, 15))

    #Dibujar rocas
    for rockObj in rocks:
        if rockObj["state"] == "normal":
            myScreen.blit(rockObj["image"], rockObj["position"])
        elif rockObj["state"] == "explosion":
            myScreen.blit(explosion2, rockObj["position"])

    #Dibujar asteroides
    for asteroidObj in asteroids:
        if asteroidObj["state"] == "normal":
            myScreen.blit(asteroidObj["image"], asteroidObj["position"])
        elif asteroidObj["state"] == "explosion" or asteroidObj["state"] == "collision":
            myScreen.blit(explosion1, asteroidObj["position"])

    #Dibujar escudos
    for shieldObj in shields:
        myScreen.blit(shieldObj["image"], shieldObj["position"])

    #Dibujar balas
    for bulletPosition in bullets:
        myScreen.blit(bullet, bulletPosition)

    #Dibujar jugador
    if playerState == "normal":
        player.set_alpha(255)
        myScreen.blit(player, playerPosition)
    elif playerState == "hit":
        player.set_alpha(125)
        myScreen.blit(player, playerPosition)
    elif playerState == "collision":
        myScreen.blit(explosion1, playerPosition)

    #Dibujar el escudo sobre la nave
    if shieldActive:
        shield.set_alpha(125)
        shieldX = playerPosition[0] - (shieldW - playerW) // 2
        shieldY = playerPosition[1] - (shieldH - playerH) // 2
        myScreen.blit(shield, (shieldX, shieldY))
    else:
        shield.set_alpha(255)

    
    pygame.display.update()

#Función: Actualizar rocas
def updateRocks(rocks, speed, height, playerPosition, playerMask, rockMask, playerState, shieldActive, lives, hitTime, currentTime):
    for rockObj in rocks[:]:
        if rockObj["state"] == "normal":
            rockObj["position"][1] += speed

            if rockObj["position"][1] > height:
                rocks.remove(rockObj)
            else:
                over = (rockObj["position"][0] - playerPosition[0], rockObj["position"][1] - playerPosition[1])
                if playerMask.overlap(rockMask, over) and playerState == "normal" and shieldActive == False:
                    rockObj["state"] = "explosion"
                    lives -= 1
                    if lives == 0:
                        playerState = "collision"
                    else:
                        playerState = "hit"
                        hitTime = currentTime
                    rockObj["destroyTime"] = currentTime
                    explosionSound.play()
                    break
        elif rockObj["state"] == "explosion":
            if currentTime - rockObj["destroyTime"] > 1000:
                rocks.remove(rockObj)

    return playerState, lives, hitTime

#Función: Actualizar asteroides
def updateAsteroids(asteroids, asteroidSpeed, height, playerPosition, playerMask, asteroidMask, playerState, shieldActive, lives, hitTime, currentTime):
    for asteroidObj in asteroids[:]:
        if asteroidObj["state"] == "normal":
            asteroidObj["position"][1] += asteroidSpeed

            if asteroidObj["position"][1] > height:
                asteroids.remove(asteroidObj)
            else:
                over = (asteroidObj["position"][0] - playerPosition[0], asteroidObj["position"][1] - playerPosition[1])
                if playerMask.overlap(asteroidMask, over) and playerState == "normal" and shieldActive == False:
                    asteroidObj["state"] = "collision"
                    lives -= 1
                    if lives == 0:
                        playerState = "collision"
                    else:
                        playerState = "hit"
                        hitTime = currentTime
                    asteroidObj["destroyTime"] = currentTime
                    explosionSound.play()
                    break
        elif asteroidObj["state"] == "explosion" or asteroidObj["state"] == "collision":
            if currentTime - asteroidObj["destroyTime"] > 1000:
                asteroids.remove(asteroidObj)

    return playerState, lives, hitTime

#Función: Actualizar monedas
def updateCoins(coins, coinSpeed, height, playerPosition, playerMask, coinMask, coinsCollected):
    for coinObj in coins[:]:
        coinObj["position"][1] += coinSpeed

        if coinObj["position"][1] > height:
            coins.remove(coinObj)
        else:
            over = (coinObj["position"][0] - playerPosition[0], coinObj["position"][1] - playerPosition[1])
            if playerMask.overlap(coinMask, over):
                coinsCollected += 1
                coinSound.play()
                coins.remove(coinObj)

    return coinsCollected

#Función: Actualizar balas
def updateBullets(bullets, bulletSpeed, bulletMask, asteroidMask, asteroids, currentTime, points):
    for bullet in bullets[:]:
        bullet[1] -= bulletSpeed

        if bullet[1] < 0:
            bullets.remove(bullet)
        else:
            for asteroidObj in asteroids[:]:
                if asteroidObj["state"] == "normal":
                    over = (asteroidObj["position"][0] - bullet[0], asteroidObj["position"][1] - bullet[1])
                    if bulletMask.overlap(asteroidMask, over):
                        bullets.remove(bullet)
                        asteroidObj["state"] = "explosion"
                        asteroidObj["destroyTime"] = currentTime
                        explosionSound.play()
                        points += 5
                        break

    return points

#Función: Actualizar escudos
def updateShields(shields, shieldSpeed, shieldActive, shieldTime, shieldMask, currentTime, height, playerPosition, playerMask):
    for shieldObj in shields[:]:
        shieldObj["position"][1] += shieldSpeed

        if shieldObj["position"][1] > height:
            shields.remove(shieldObj)
        else:
            over = (shieldObj["position"][0] - playerPosition[0], shieldObj["position"][1] - playerPosition[1])
            if playerMask.overlap(shieldMask, over):
                shieldActive = True
                shieldTime = currentTime
                shieldSound.play()
                shields.remove(shieldObj)

    return shieldActive, shieldTime

#Función: Agregar rocas
def spawnRocks(rockCount, rockAdd, width, rockW, rockH, rocks):
    if rockCount > rockAdd:
        numRocks = random.randint(1, 3)

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

    return rockCount, rockAdd

#Función: Agregar asteroides y monedas
def spawnAsteroidsAndCoins(asteroidCount, asteroidAdd, width, asteroidW, asteroidH, asteroidsSpawned, asteroids, coinW, coinH, coins):
    if asteroidCount > asteroidAdd:
        asteroidX = random.randint(0, width - asteroidW)
        asteroidY = -asteroidH
        asteroids.append({
            "position": [asteroidX, asteroidY],
            "image": asteroid,
            "state": "normal",
            "destroyTime": None
        })
        asteroidsSpawned += 1
        if asteroidsSpawned % 5 == 0 and asteroidsSpawned != 0:
            coinX = random.randint(0, width - coinW)
            coinY = -coinH
            coins.append({
                "position": [coinX, coinY],
                "image": coin,
                "state": "normal",
                "destroyTime": None
            })

        asteroidAdd = random.uniform(3000, 5000)
        asteroidCount = 0

    return asteroidCount, asteroidAdd, asteroidsSpawned

#Función: Agregar escudos
def spawnShields(shieldCount, shieldAdd, width, shieldW, shieldH, shields):
    if shieldCount > shieldAdd:
        if random.random() < 0.15:
            shieldX = random.randint(0, width - shieldW)
            shieldY = -shieldH
            shields.append({
                "position": [shieldX, shieldY],
                "image": shield,
                "state": "normal",
                "destroyTime": None
            })
        shieldCount = 0

    return shieldCount

#Función: Menú Game Over
def menuGameOver(playerHit, font, width, height, elapsedTime, points, coinsCollected):
    if playerHit:
        gameOver = font.render("Game Over", 2, cianNeon)
        myScreen.blit(gameOver, (width / 2 - gameOver.get_width() / 2, height / 2 - gameOver.get_height() / 2))
        timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, cianNeon)
        myScreen.blit(timeRecord, (width / 2 - timeRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 50))
        pointsRecord = font.render(f"Points: {points}", 1, cianNeon)
        myScreen.blit(pointsRecord, (width / 2 - pointsRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 100))
        coinsRecord = font.render(f"Coins Collected: {coinsCollected}", 1, cianNeon)
        myScreen.blit(coinsRecord, (width / 2 - coinsRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 150))
        pygame.display.update()
        pygame.time.delay(3000)

        return True

    return False

#Función: Manejo del estado del jugador
def handlePlayerState(playerHit, playerState, currentTime, hitTime):
    if playerState == "hit":
        if currentTime - hitTime > 3000:
            playerState = "normal"
    elif playerState == "collision":
        playerHit = True

    return playerHit, playerState

#Función: Manejo de eventos
def handleEvents(run, homeButtonX, buttonY, buttonWidth, musicMuted, effectsMuted):
    goHome = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if homeButton.get_rect(topleft = (homeButtonX, buttonY)).collidepoint(mousePos):
                selected.play()
                goHome = True

            if muteButton.get_rect(topleft = (homeButtonX - buttonWidth - 10, buttonY)).collidepoint(mousePos):
                if musicMuted:
                    musicMuted = False
                    effectsMuted = False
                    pygame.mixer.music.set_volume(0.1)
                    selected.set_volume(0.2)
                    coinSound.set_volume(0.3)
                    shieldSound.set_volume(0.3)
                    explosionSound.set_volume(0.2)
                    gunshotSound.set_volume(0.2)
                    selected.play()
                else:
                    musicMuted = True
                    effectsMuted = True
                    pygame.mixer.music.set_volume(0)
                    selected.set_volume(0)
                    coinSound.set_volume(0)
                    shieldSound.set_volume(0)
                    explosionSound.set_volume(0)
                    gunshotSound.set_volume(0)
                    selected.play()

    return run, goHome, musicMuted, effectsMuted

#Función: Controladores
def handleControllers(playerPosition, speed, width, height, playerW, playerH, currentTime, lastShootTime, shootInterval, bullets, bulletW, bulletH):
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and playerPosition[0] - speed >= 0:
        playerPosition[0] -= speed

    if(keys[pygame.K_RIGHT] or keys[pygame.K_d]) and playerPosition[0] + speed <= width - playerW:
        playerPosition[0] += speed

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and playerPosition[1] - speed >= 0:
        playerPosition[1] -= speed

    if(keys[pygame.K_DOWN] or keys[pygame.K_s]) and playerPosition[1] + speed <= height - playerH:
        playerPosition[1] += speed

    if keys[pygame.K_SPACE] and currentTime - lastShootTime > shootInterval:
        gunshotSound.play()
        bulletX = playerPosition[0] + playerW // 2 - bulletW // 2
        bulletY = playerPosition[1] - bulletH
        bullets.append([bulletX, bulletY])
        lastShootTime = currentTime

    return lastShootTime

#Función: Manejo de escudo
def handleShields(shieldActive, shieldTime, currentTime):
    if shieldActive:
        if currentTime - shieldTime > 5000:
            shieldActive = False
    return shieldActive

#Functión: Juego principal
def main():
    #Para modificar variables globales
    global musicMuted, effectsMuted

    #El juego está corriendo y el jugador no ha sido golpeado
    run = True
    goHome = False
    playerHit = False
    playerState = "normal"
    playerPosition = [width // 2 - playerW, height - playerH - 10]

    #Se setean los contadores
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    points = 0

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
    coinsCollected = 0
    coins = []

    #Manejo de vidas
    lives = 3
    hitTime = None

    #Manejo de escudo
    shieldActive = False
    shieldTime = None
    shieldAdd = 5000
    shieldCount = 0
    shields = []
    
    #Manejo de balas
    shootInterval = 1000 
    lastShootTime = 0
    bullets = []

    #Comienza el juego
    while run:

        #Se maneja el tiempo y el contador de asteroides
        elapsedMS = clock.tick(60)
        currentTime = pygame.time.get_ticks()
        rockCount += elapsedMS
        asteroidCount += elapsedMS
        shieldCount += elapsedMS
        elapsedTime = time.time() - startTime

        #Se agregan rocas
        rockCount, rockAdd = spawnRocks(rockCount, rockAdd, width, rockW, rockH, rocks)

        #Se agregan asteroides y monedas
        asteroidCount, asteroidAdd, asteroidsSpawned = spawnAsteroidsAndCoins(asteroidCount, asteroidAdd, width, asteroidW, asteroidH, asteroidsSpawned, asteroids, coinW, coinH, coins)

        #Se agregan escudos
        shieldCount = spawnShields(shieldCount, shieldAdd, width, shieldW, shieldH, shields)

        #Manejo de eventos
        run, goHome, musicMuted, effectsMuted = handleEvents(run, homeButtonX, buttonY, buttonWidth, musicMuted, effectsMuted)
        if goHome:
            return

        #Controladores de juego
        lastShootTime = handleControllers(playerPosition, speed, width, height, playerW, playerH, currentTime, lastShootTime, shootInterval, bullets, bulletW, bulletH)

        #Se actualizan las posiciones de las rocas
        playerState, lives, hitTime = updateRocks(rocks, speed, height, playerPosition, playerMask, rockMask, playerState, shieldActive, lives, hitTime, currentTime)
        
        #Se actualizan las posiciones de los asteroides
        playerState, lives, hitTime = updateAsteroids(asteroids, asteroidSpeed, height, playerPosition, playerMask, asteroidMask, playerState, shieldActive, lives, hitTime, currentTime)

        #Se actualizan las posiciones de las monedas
        coinsCollected = updateCoins(coins, coinSpeed, height, playerPosition, playerMask, coinMask, coinsCollected)

        #Se actualizan las posiciones de las balas / Explosión con asteroides
        points = updateBullets(bullets, bulletSpeed, bulletMask, asteroidMask, asteroids, currentTime, points)

        #Se actualizan las posiciones de los escudos
        shieldActive, shieldTime = updateShields(shields, shieldSpeed, shieldActive, shieldTime, shieldMask, currentTime, height, playerPosition, playerMask)

        #Manejo de estado del jugador
        playerHit, playerState = handlePlayerState(playerHit, playerState, currentTime, hitTime)

        #Manejo de escudos
        shieldActive = handleShields(shieldActive, shieldTime, currentTime)
        
        #Dibujamos
        draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, rocks, asteroids, coins, coinsCollected, shieldActive, lives, bullets, shields)

        #Si el jugador pierde
        if playerHit:
            pygame.time.delay(1000)
            myScreen.blit(back, (0, 0))
            #El jugador pierde el juego, se despliega el menú de Game Over
            if menuGameOver(playerHit, font, width, height, elapsedTime, points, coinsCollected):
                return        

if __name__ == "__main__":
    while True:
        menu()
        main()