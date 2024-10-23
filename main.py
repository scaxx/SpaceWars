import pygame
import time
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
explosion = pygame.image.load("assets/extras/explosion.png")
explosion1 = pygame.transform.scale(explosion, (asteroidW, asteroidH))
explosion2 = pygame.transform.scale(explosion, (40, 40))

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

    while run:
        myScreen.blit(back, (0, 0))

        #Detect mouse position
        mousePos = pygame.mouse.get_pos()

        #Render buttons
        title = font.render("Welcome to Space Wars!", True, "white")
        
        playB = font.render("Play", True, "white")
        optionsB = font.render("Options", True, "white")
        quitB = font.render("Quit", True, "white")

        titleRect = title.get_rect(center=(width/2, height/4))
        playRect = playB.get_rect(center=(width/2, height/2))
        optionsRect = optionsB.get_rect(center=(width/2, height/2 + 100))
        quitRect = quitB.get_rect(center=(width/2, height/2 + 200))

        #Define button colors
        playColor = "gray" if playRect.collidepoint(mousePos) else "white"
        optionsColor = "gray" if optionsRect.collidepoint(mousePos) else "white"
        quitColor = "gray" if quitRect.collidepoint(mousePos) else "white"

        #Re-render buttons with the updated colors
        playB = font.render("Play", True, playColor)
        optionsB = font.render("Options", True, optionsColor)
        quitB = font.render("Quit", True, quitColor)

        #Draw buttons
        myScreen.blit(title, titleRect)
        myScreen.blit(playB, playRect)
        myScreen.blit(optionsB, optionsRect)
        myScreen.blit(quitB, quitRect)

        pygame.display.update()

        #Event handling
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

        pygame.time.delay(100)

#Function - Options menu     
def optionsMenu():
    #Define global variables
    global musicMuted, effectsMuted
    run = True

    while run:
        myScreen.blit(back, (0, 0))
        #Detect mouse position
        mousePos = pygame.mouse.get_pos()

        #Render options
        title = font.render("Options", True, "white")
        muteMusic = font.render(f"Music: {'ON' if not musicMuted else 'OFF'}", True, "white" if not musicMuted else "gray")
        muteEffects = font.render(f"Effects: {'ON' if not effectsMuted else 'OFF'}", True, "white" if not effectsMuted else "gray")
        goBack = font.render("Back to Menu", True, "white")

        titleRect = title.get_rect(center=(width/2, height/4))
        muteMusicRect = muteMusic.get_rect(center=(width/2, height/2))
        muteEffectsRect = muteEffects.get_rect(center=(width/2, height/2 + 100))
        goBackRect = goBack.get_rect(center=(width/2, height/2 + 200))

        #Determine button color
        goBackColor = "gray" if goBackRect.collidepoint(mousePos) else "white"

        #Re-render button with the updated color
        goBack = font.render("Back to Menu", True, goBackColor)

        myScreen.blit(title, titleRect)
        myScreen.blit(muteMusic, muteMusicRect)
        myScreen.blit(muteEffects, muteEffectsRect)
        myScreen.blit(goBack, goBackRect)

        pygame.display.update()

        #Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if muteMusicRect.collidepoint(event.pos):
                    musicMuted = not musicMuted
                    pygame.mixer.music.set_volume(0 if musicMuted else 0.5)
                    selected.play()
                elif muteEffectsRect.collidepoint(event.pos):
                    effectsMuted = not effectsMuted
                    selected.set_volume(0 if effectsMuted else 1)
                    explosionSound.set_volume(0 if effectsMuted else 1)
                    gunshotSound.set_volume(0 if effectsMuted else 1)
                    selected.play()
                elif goBackRect.collidepoint(event.pos):
                    selected.play()
                    run = False
                    break

        pygame.time.delay(100)

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
    if musicMuted:
        myScreen.blit(soundButton, (homeButtonX - buttonWidth - 10, buttonY))
    else:
        myScreen.blit(muteButton, (homeButtonX - buttonWidth - 10, buttonY))

    #Draw stars
    for starObj in stars:
        if starObj["state"] == "normal":
            myScreen.blit(starObj["image"], starObj["position"])
        elif starObj["state"] == "explosion":
            myScreen.blit(explosion2, starObj["position"])

    #Draw asteroids
    for asteroidObj in asteroids:
        if asteroidObj["state"] == "normal":
            myScreen.blit(asteroidObj["image"], asteroidObj["position"])
        elif asteroidObj["state"] == "explosion" or asteroidObj["state"] == "collision":
            myScreen.blit(explosion1, asteroidObj["position"])

    #Draw bullets
    for bulletPosition in bullets:
        myScreen.blit(bullet, bulletPosition)

    #Draw player
    if playerState == "normal":
        myScreen.blit(player, playerPosition)
    elif playerState == "collision":
        myScreen.blit(explosion1, playerPosition)
    
    pygame.display.update()

#Function - Main game
def main():
    #To modify global variables
    global musicMuted, effectsMuted

    run = True
    playerHit = False

    playerState = "normal"
    playerPosition = [width // 2 - playerW, height - playerH - 10]

    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    points = 0

    starAdd = 1000
    starCount = 0
    stars = []

    asteroidAdd = random.uniform(3000, 5000)
    asteroidCount = 0
    asteroids = []

    bullets = []
    shootInterval = 1000 
    lastShootTime = 0

    while run:
        currentTime = pygame.time.get_ticks()
        starCount += clock.tick(60)
        asteroidCount += clock.tick(60)
        elapsedTime = time.time() - startTime

        if playerState == "collision":
            pygame.time.delay(2000)
            myScreen.blit(back, (0, 0))
            playerHit = True

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
        if asteroidCount > asteroidAdd:
            asteroidX = random.randint(0, width - asteroidW)
            asteroidY = -asteroidH
            asteroids.append({
                "position": [asteroidX, asteroidY],
                "image": asteroid,
                "state": "normal",
                "destroyTime": None
            })
            asteroidAdd = random.uniform(3000, 5000)
            asteroidCount = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
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

        #Update positions - bullets / Collision with asteroids - verify
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
                            
        #Collision - verify
        if playerHit:
            gameOver = font.render("Game Over", 2, "white")
            myScreen.blit(gameOver, (width / 2 - gameOver.get_width() / 2, height / 2 - gameOver.get_height() / 2))
            timeRecord = font.render(f"Time: {round(elapsedTime)} s", 1, "white")
            myScreen.blit(timeRecord, (width / 2 - timeRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 50))
            pointsRecord = font.render(f"Points: {points}", 1, "white")
            myScreen.blit(pointsRecord, (width / 2 - pointsRecord.get_width() / 2, height / 2 - gameOver.get_height() / 2 + 100))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.time.delay(3000)
            menu()
            break

        draw(player, playerPosition, playerState, elapsedTime, soundButton, muteButton, homeButton, points, stars, asteroids, bullets)

if __name__ == "__main__":
    menu()
    main()
