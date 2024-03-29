import pygame
import random

#초기화 #중요!
pygame.init() 

score = 0
#FPS
clock = pygame.time.Clock()

#화면 크기 설정
screenWidth = 360 #가로크기
screenHeight = 480 #세로크기

screen = pygame.display.set_mode((screenWidth,screenHeight))  #가로, 세로

#배경이미지
background = pygame.image.load("C:\\Users\\이민석\\Desktop\\example\\pygame_basic\\background1.png")

#캐릭터
character = pygame.image.load("C:\\Users\\이민석\\Desktop\\example\\pygame_basic\\rabbit.png")
characterSize = character.get_rect().size  #img크기 불러옴
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (screenWidth / 2) - (characterWidth / 2)
characterYpos = screenHeight - characterHeight

#이동할 좌표
toX = 0
toY = 0

#이동속도
characterSpeed = 0.6

#난수 생성 - 똥 생성용
randomNumber = 30
poSpeed = 10

#적
enemy = pygame.image.load("C:\\Users\\이민석\\Desktop\\example\\pygame_basic\\carrot.png")
enemySize = enemy.get_rect().size
enemyWidth = enemySize[0]
enemyHeight = enemySize[1]
enemyXpos = 200
enemyYpos = 100

#Title
pygame.display.set_caption("MS GAME")

#폰트 정의
game_font = pygame.font.Font(None,30) #폰트, 크기

#게임 플레이 총 시간
totalTime = 20
startTicks = pygame.time.get_ticks()

#Event
running = True
while running:  #실행창
    dt = clock.tick(30)
    #print("fps: " + str(clock.get_fps()))
    
    for event in pygame.event.get(): #어떤 이벤트 발생했는지 판단함
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= characterSpeed
            if event.key == pygame.K_RIGHT:
                toX += characterSpeed
            if event.key == pygame.K_UP:
                toY -= characterSpeed
            if event.key == pygame.K_DOWN:
                toY += characterSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0 
    
    #캐릭터 이동 & 프레임맞추기
    characterXpos += toX * dt
    characterYpos += toY * dt
    
    
    #경계 설정-가로
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > screenWidth - characterWidth:
        characterXpos = screenWidth - characterWidth
    #경계 설정-세로
    if characterYpos < 0:
        characterYpos = 0
    elif characterYpos > screenHeight - characterHeight:
        characterYpos = screenHeight - characterHeight
    
    
    randomNumber = random.randrange(1,200)
    randomNumber2 = random.randrange(1,340)
    
    if enemyYpos > 480:
        enemyYpos = randomNumber
        enemyXpos = randomNumber2
        score += 1
        poSpeed += 2
    
    enemyYpos += poSpeed
        
    #충돌
    characterRect = character.get_rect()
    characterRect.left = characterXpos
    characterRect.top = characterYpos
    
    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXpos
    enemyRect.top = enemyYpos
    
    if characterRect.colliderect(enemyRect):
        print("충돌")
        running = False
            
    #타이머
    elapsedTime = (pygame.time.get_ticks()) / 1000
    #경과시간이 ms 이므로 초단위로 표시
    if totalTime - elapsedTime < 0:
        print("시간초과")
        running = False
    timer = game_font.render(str(int(totalTime - elapsedTime)), True, (255,255,255))
    # 출력할 글자, 색상
    scoree = game_font.render(str(score), True, (200,200,200))
    
    
    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) 
    screen.blit(character, (characterXpos , characterYpos))
    screen.blit(enemy, (enemyXpos , enemyYpos))
    screen.blit(timer, (10,10))
    screen.blit(scoree, (10,30))
    pygame.display.update() #화면 새로고침

pygame.time.delay(2000) # 2초 동안 대기
pygame.quit()    #pygame 종료