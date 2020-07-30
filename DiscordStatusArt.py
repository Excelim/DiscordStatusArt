import pygame
import pyperclip
pygame.init()

x = 0
y = 0
size = 50
array = []

win = pygame.display.set_mode((size*11, size*10))
pygame.display.set_caption('Discord Status Art     Press CTRL to copy art to clipboard!')
pygame.key.set_repeat(1, 10)
ico = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(ico)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                def func():
                    for square in array:
                        if square[0] == x and square[1] == y:
                            array.remove([square[0],square[1]])
                            return
                    array.append([x,y])
                func()
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                copystring = ''
                for yy in range(0, size*10, size):
                    for xx in range(0, size*11, size):
                        if [xx, yy] in array:
                            copystring += '⬜'
                        else:
                            copystring += '⬛'
                    copystring += ' '
                #copystring = copystring[:-1]
                pyperclip.copy(copystring)
                pygame.display.set_caption('Copied!')
                pygame.time.delay(2000)
                pygame.display.set_caption('Discord Status Art     Press CTRL to copy art to clipboard!')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x >= size:
                x -= size 
            if event.key == pygame.K_RIGHT and x < size*10:
                x += size
            if event.key == pygame.K_UP and y >= size:
                y -= size
            if event.key == pygame.K_DOWN and y < size*9:
                y += size
            if event.key == pygame.K_a and x >= size:
                x -= size 
            if event.key == pygame.K_d and x < size*10:
                x += size
            if event.key == pygame.K_w and y >= size:
                y -= size
            if event.key == pygame.K_s and y < size*9:
                y += size
    win.fill((25,25,25))
    for square in array:
        pygame.draw.rect(win, (255, 255, 255), (square[0], square[1], size, size))
    rect1 = pygame.Rect(x, y, size, size)
    rect2 = pygame.Rect(x, y, round(size/1.75), round(size/1.75))
    rect2.center = rect1.center
    pygame.draw.rect(win, (0, 128, 128), rect1, 5)
    pygame.draw.rect(win, (0, 64, 64), rect2, 5)
    pygame.display.update()
    pygame.time.delay(100)
# by Excelim
pygame.quit()