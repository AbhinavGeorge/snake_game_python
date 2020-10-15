import pygame
import math
import random
import time
from pygame import mixer

pygame.init()
mixer.init()
x_size = 500
y_size = 500
caption = "snake game"
# setting up the window
black = (0,0,0)
x = pygame.display.set_mode((x_size, y_size))
caption_real = pygame.display.set_caption(caption)

font_style = pygame.font.SysFont(None, 20, False, True, None)
def msg(msg, color, x_msg, y_msg):
    message = font_style.render(msg, True, color)
    x.blit(message, [x_msg, y_msg])

high_score = []

def main():
    # variables
    red = (255, 0, 0)
    blue = (0, 0, 255)
    x_change = 0
    y_change = 0
    x_snake = 50
    y_snake = 50

    val = 7

    size = 31
    x_apple = random.randint(0, x_size - (size * 1))
    y_apple = random.randint(0, y_size - (size * 1))
    gamme_over = False
    if math.sqrt(((x_snake - x_apple) ** 2) + ((y_snake - y_apple) ** 2)) < 15:
        x_apple = random.randint(0, x_size - (size * 1))
        y_apple = random.randint(0, y_size - (size * 1))
    clock = pygame.time.Clock()
    score = 0
    snk_list = []
    snk_size = 1



    # art
    def draw_apple(width_app, height_apple):
        pygame.draw.rect(x, red, (x_apple, y_apple, width_app, height_apple))

    def draw_snake(x_size_snake, y_size_snake, snk_list, snk_size):
        for blob_x, blob_y in snk_list:
            pygame.draw.rect(x, blue, (blob_x+1, blob_y+1, x_size_snake, y_size_snake))
        if len(snk_list) > snk_size:
            del (snk_list[0])





    def death():
        file1 = open("high_score.txt", "a")
        file1.write(str(score)+"\n")
        file1.close()
        a_file = open("high_score.txt", "r")

        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            stripped_line.line.strip("['")
            stripped_line.line.strip("']")
            list_of_lists.append(line_list)

        a_file.close()
        print(list_of_lists)
        x.fill((0, 0, 0))
        msg("you lose", (255, 0, 0), x_size // 2 - 70, y_size // 2 - 80)
        msg("press enter button to play again", (50, 50, 50), x_size // 2 - 70, y_size // 2 - 50)
        msg("high score : "+str(max(list_of_lists)), (247,148,89), x_size // 2 - 70, y_size // 2 - 10)
        msg("you scored " + str(score), (12, 129, 162), x_size // 2 - 70, y_size - 30)

    # game loop
    running = True
    while running:
        clock.tick(24)
        if gamme_over:
            death()
            for boobs in pygame.event.get():
                if boobs.type == pygame.QUIT:
                    running = False
                if boobs.type == pygame.KEYDOWN:
                    if boobs.key == pygame.K_RETURN:
                        main()

        else:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:

                    if events.key == pygame.K_LEFT:
                        if x_change == val:
                            x_change = val
                        else:
                            x_change = -1 * val
                        y_change = 0

                    if events.key == pygame.K_RIGHT:
                        if x_change == -1 * val:
                            x_change = -1 * val
                        else:
                            x_change = 1 * val
                        y_change = 0

                    if events.key == pygame.K_UP:
                        if y_change == 1 * val:
                            y_change = 1 * val
                        else:
                            y_change = -1 * val
                        x_change = 0
                    if events.key == pygame.K_DOWN:
                        if y_change == -1 * val:
                            y_change = -1 * val
                        else:
                            y_change = 1 * val
                        x_change = 0
                    if events.key == pygame.K_8:
                        score += 10



            # snake eating apple
            if math.sqrt(((x_snake - x_apple) ** 2) + ((y_snake - y_apple) ** 2)) < 13:
                x_apple = random.randint(0, x_size - (size * 1))
                y_apple = random.randint(0, y_size - (size * 1))
                if math.sqrt(((x_snake - x_apple) ** 2) + ((y_snake - y_apple) ** 2)) < 13:
                    x_apple = random.randint(0, x_size - (size * 1))
                    y_apple = random.randint(0, y_size - (size * 1))
                score += 1
                snk_size += 1






            # snake
            x_snake += x_change
            y_snake += y_change
            x.fill((0, 0, 0))
            draw_apple(size, size)
            head = []
            head.append(int(x_snake))
            head.append(int(y_snake))
            snk_list.append(head)
            draw_snake(size, size, snk_list, snk_size)
            msg("score : " + str(score), (12, 129, 162), 0, 0)

            if head in snk_list[:-1]:
                gamme_over = True


            # snake death
            if x_snake >= x_size:
                gamme_over = True

            if y_snake >= 500 :
                gamme_over =True

            if x_snake <= 0:
                gamme_over = True

            if y_snake <= 0:
                gamme_over = True


        pygame.display.update()

    pygame.quit()
    quit()
def welcome():

    run = True
    while run:
        x.fill((238,50,49))
        msg("HI!!!", black, 230, 200)
        msg("WELCOME TO SNAKE", black, 190, 230)
        msg("PRESS SPACE TO PLAY", black, 170, 260)
        for but in pygame.event.get():
            if but.type == pygame.QUIT:
                run = False
            if but.type == pygame.KEYDOWN:
                if but.key == pygame.K_SPACE:
                    main()
        pygame.display.update()
    pygame.quit()

welcome()

