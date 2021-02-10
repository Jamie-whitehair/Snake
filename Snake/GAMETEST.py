import pygame
import sys
import random
from pygame.math import Vector2
import traceback
try:
    music = False
    cell_size = 40
    cell_number = 20
    i = open("highscore.txt", "r")
    highscore = i.readline()
    highscore_copy = int(highscore)
    i.close()
    class SNAKE:
        def __init__(self):
            self.body = [Vector2(5,10), Vector2(7,10), Vector2(6,10)]
            self.direction = Vector2(-1,0)
            self.new_block = False


        def draw_snake(self):
            for block in self.body:
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
                pygame.draw.rect(screen, (0,255,0), block_rect)


        def move_snake(self):
            if self.new_block is True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]

        def add_block(self):
            self.new_block = True
            munch.play()

        def reset(self):
            self.body = [Vector2(5,10), Vector2(7,10), Vector2(6,10)]
    class MAIN:
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

        def update(self):
            self.snake.move_snake()
            self.collision()
            self.check_fail()

        def drawings(self):
            self.snake.draw_snake()
            self.fruit.draw_fruit()
            self.draw_score()

        def collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number:
                self.game_over()
            elif  not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()


        def game_over(self):
            self.snake.reset()
            self.body = [Vector2(5,10), Vector2(7,10), Vector2(6,10)]
            death_sfx.play()


        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            if int(score_text) > highscore_copy:
                i = open("highscore.txt", "w")
                i.write(score_text)
                i.close
            score_surface = game_font.render(survive + score_text + " High score: "  + highscore, True, (255,0,0))
            score_x = int(cell_size * cell_number - 180)
            score_y = int(cell_size * cell_number - 30)
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            screen.blit(score_surface, score_rect)




    class FRUIT:

        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            screen.blit(fruit, fruit_rect)
            #pygame.draw.rect(screen,(255,0,0), fruit_rect)

        def randomize(self):
            self.x = random.randint(0,cell_number - 1)
            self.y = random.randint(0,cell_number - 1)
            self.pos = Vector2(self.x,self.y)

    main_game = MAIN()
    survive = "score: "
    pygame.init()
    bg_music = pygame.mixer.Sound("bgmusic.mp3")
    bg_music.play()
    death_sfx = pygame.mixer.Sound("Fail.mp3")
    munch = pygame.mixer.Sound("Crunch.mp3")
    game_font = pygame.font.Font('Daily Hours.ttf', 35)
    bg = pygame.image.load("bg0.jpg")
    icon = pygame.image.load("strawberry.png")
    pygame.display.set_icon(icon)
    fruit = pygame.image.load("strawberry_fruit.png")
    pygame.display.set_caption("Snake!")

    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 140)
    while True:
        music = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
                pygame.quit()
                sys.exit
                False
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == ord('w'):
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == ord('a'):
                    main_game.snake.direction = Vector2(-1,0)
                if event.key == ord('s'):
                    main_game.snake.direction = Vector2(0,1)
                if event.key == ord('d'):
                    main_game.snake.direction = Vector2(1,0)
        screen.blit(bg, [0, 0])
        screen.fill((0,0,0))
        screen.blit(bg, [0, 0])
        main_game.drawings()
        pygame.display.update()
        clock.tick(60)
except Exception:
    traceback.print_exc()







