import pygame
import pygame as pg
import sys
from Blocks import Blocks
from ESCwiindows import PopupWindow
import random





# initial Pygame
pg.init()
clock = pygame.time.Clock()

# BGM
pg.mixer.init()     #bgm
pygame.mixer.music.load("01 Main Theme - May Be Happy.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# set screen size
screen_width = 800
screen_height = 750
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Tetris Game")

# colour defined
white = (255, 255, 255)
black = (0, 0, 0)


# Game title
font = pg.font.Font(None, 64)
title_text = font.render("Tetris Game", True, black)
title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 5))

# Year and course code: 2023-7805ICT
font = pg.font.Font(None, 24)
course_text = font.render("2023      7805ICT - Software Design",True,black)
course_rect = course_text.get_rect(center=(screen_width // 2-230, screen_height // 3))

# list of students
font = pg.font.Font(None, 24)
student_text = font.render("Derek   Talia   Pouya",True,black)
student_rect = student_text.get_rect(center=(screen_width // 2-230, screen_height // 3+30))


# Option Buttons
font = pg.font.Font(None, 40)
play_button = font.render("Play", True, black)
play_rect = play_button.get_rect(center=(screen_width // 2, screen_height // 2))

font = pg.font.Font(None, 36)
score_button = font.render("Score", True, black)
score_rect = score_button.get_rect(center=(screen_width // 2, screen_height // 2+60))

options_button = font.render("Configure", True, black)
options_rect = options_button.get_rect(center=(screen_width // 2, screen_height // 2 + 120))

quit_button = font.render("Exit", True, black)
quit_rect = quit_button.get_rect(center=(screen_width // 2, screen_height // 2 + 180))

# game loop
bgmPause = False
running = True
configure_page = False
score_page = False
play_page = False
startUpPage = True
show_popup = False
paused = False

while running:
    if not pygame.mixer.music.get_busy() and not bgmPause:
        pygame.mixer.music.load("01 Main Theme - May Be Happy.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_m:
            if bgmPause:
                bgmPause = False
            else:
                bgmPause = True
        elif bgmPause:  # BGM pause
            pg.mixer_music.pause()
        elif not bgmPause:
            pygame.mixer_music.unpause()
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if startUpPage:
                if score_rect.collidepoint(mouse_pos):
                    score_page = True
                    startUpPage = False
                elif play_rect.collidepoint(mouse_pos):
                    play_page = True
                    s = Blocks.block_size  # size ratio
                    frame_speed = 0
                    speedUp = False
                    pg.init()
                    pg.mixer_music.fadeout(200)
                    pg.mixer.music.load("36 Dot Nurie Stage 1 - I Love Psg !!!.mp3")
                    pg.mixer.music.set_volume(0.2)
                    pg.mixer.music.play()

                    # GAME filed
                    while play_page:
                        popup = PopupWindow()
                        if bgmPause:
                            pg.mixer_music.pause()
                        elif not bgmPause:
                            pg.mixer_music.unpause()
                            if not pygame.mixer.music.get_busy():      # BGM loop
                                pg.mixer_music.play()

                        if not Blocks.select_Block:
                            Blocks.select_Block = Blocks.Next_Block
                            Blocks.Next_Block = list(random.choice(Blocks.blocks))
                        elif not Blocks.Next_Block:
                            Blocks.Next_Block = list(random.choice(Blocks.blocks))

                        screen.fill(color=(124, 115, 192))  # RPG backgound colour choise

                        for event in pg.event.get():
                            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                                if bgmPause:
                                    bgmPause = False
                                else:
                                    bgmPause = True
                            if event.type == pg.QUIT:  # quit if quit pressed
                                play_page = False
                                pg.mixer_music.fadeout(800)
                                pg.mixer.music.load("01 Main Theme - May Be Happy.mp3")
                                #pg.quit()  # out
                                #sys.exit()

                            # POPUP window
                            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:# if button ESC pressed
                                show_popup = True
                            elif event.type == pygame.MOUSEBUTTONDOWN and show_popup:   # if window popup
                                result = popup.handle_event(event)
                                if result == "YES":
                                    show_popup = False
                                    play_page = False
                                    pg.mixer_music.fadeout(800)
                                    pg.mixer.music.load("01 Main Theme - May Be Happy.mp3")
                                elif result == "NO":
                                    show_popup = False
                                    paused = False

                        clock.tick(60)
                        # show popup window

                        if not paused:
                            if frame_speed >= 80:
                                Blocks.block_down_move(Blocks)
                                frame_speed = 0
                            elif speedUp:
                                frame_speed += 20
                            else:
                                frame_speed += 1
                        Blocks.draw_block(Blocks, screen)
                        pg.display.set_caption("Scores: " + str(Blocks.score[0]))
                        print(Blocks.score)



                        pg.draw.rect(screen, (140, 130, 195), (250 * s, 0, 383 * s, 500 * s))

                        # Team nunmber
                        font = pg.font.Font(None, 36)
                        gamesTeam_text = font.render("Team Number: 2", True, black)
                        gamesTeam_rect = gamesTeam_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 120))
                        screen.blit(gamesTeam_text, gamesTeam_rect)


                        # Current score of the session.
                        font = pg.font.Font(None, 36)
                        gamesScore_text = font.render(f"Score: {str(Blocks.score[0])}", True, black)
                        gamesScore_rect = score_button.get_rect(center=(screen_width // 2+160, screen_height // 5 + 60))
                        screen.blit(gamesScore_text, gamesScore_rect)

                        # Number of lines eliminated in the session
                        font = pg.font.Font(None, 36)
                        gamesLines_text = font.render(f"{str(Blocks.complete_row_counts)} lines eliminated", True, black)
                        gamesLines_rect = gamesLines_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 180))
                        screen.blit(gamesLines_text, gamesLines_rect)

                        # Current level
                        font = pg.font.Font(None, 36)
                        gamesLevel_text = font.render("Current level: 2", True,
                                                      black)
                        gamesLevel_rect = gamesLevel_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 240))
                        screen.blit(gamesLevel_text, gamesLevel_rect)

                        # Extended or normal game
                        font = pg.font.Font(None, 36)
                        gamesExtend_text = font.render("Extend: OFF", True,
                                                     black)
                        gamesExtend_rect = gamesExtend_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 300))
                        screen.blit(gamesExtend_text, gamesExtend_rect)

                        # Game Mode
                        font = pg.font.Font(None, 36)
                        gamesMode_text = font.render("Player Mode", True,
                                                      black)
                        gamesMode_rect = gamesMode_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 ))
                        screen.blit(gamesMode_text, gamesMode_rect)

                        # Next Block
                        font = pg.font.Font(None, 36)
                        nextBlock_text = font.render("Next Block", True,
                                                     black)
                        nextBlock_rect = nextBlock_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 360))
                        screen.blit(nextBlock_text, nextBlock_rect)

                        for row, col in Blocks.Next_Block:  # loop the next blocks we chosen
                            row += 4
                            col += 15
                            # xy transport, each block should be 25*25
                            point = [col * 25, 500 - row * 25]

                            pygame.draw.rect(screen, (232, 156, 153),  # 232,255,206
                                             (point[0] * Blocks.block_size, point[1] * Blocks.block_size,
                                              23 * Blocks.block_size, 23 * Blocks.block_size))
                        if show_popup:
                            popup.draw(screen)
                            paused = True

                        pg.display.flip()  # refresh

                        if Blocks.gameOver:
                            play_page = False
                elif options_rect.collidepoint(mouse_pos):
                    configure_page = True
                    startUpPage = False
                elif quit_rect.collidepoint(mouse_pos):
                    running = False
           

    screen.fill(white)
    if configure_page:  # in Configure
        # Configure buttons
        font = pg.font.Font(None, 48)
        configure_text = font.render("Configure", True, black)
        configure_rect = configure_text.get_rect(center=(screen_width // 2, screen_height // 7))

        font = pg.font.Font(None, 36)
        fsize_button = font.render("Field Size: [375*750]", True, black)
        fsize_rect = fsize_button.get_rect(center=(screen_width // 2, screen_height // 5 + 60))

        gameLevel_button = font.render("Game Level: [2]", True, black)
        gameLevel_rect = gameLevel_button.get_rect(center=(screen_width // 2, screen_height // 5 + 120))

        extend_button = font.render("Extend: [CLOSE]", True, black)
        extend_rect = extend_button.get_rect(center=(screen_width // 2, screen_height // 5 + 180))

        mode_button = font.render("Mode: [Player]", True, black)
        mode_rect = mode_button.get_rect(center=(screen_width // 2, screen_height // 5 + 240))

        close_button = font.render("Close", True, black)
        close_rect = close_button.get_rect(center=(screen_width // 2+260, screen_height // 1.5 +160))

        screen.blit(configure_text,configure_rect)
        screen.blit(fsize_button, fsize_rect)
        screen.blit(gameLevel_button, gameLevel_rect)
        screen.blit(extend_button, extend_rect)
        screen.blit(mode_button, mode_rect)
        screen.blit(close_button, close_rect)
    elif score_page:    # in Top 10
        font = pg.font.Font(None, 48)
        top_text = font.render("Top 10 Score", True, black)
        top_rect = top_text.get_rect(center=(screen_width // 2, screen_height // 7))

        font = pg.font.Font(None, 30)
        close_button = font.render("Close", True, black)
        close_rect = close_button.get_rect(center=(screen_width // 2+260, screen_height // 1.5 +160))

        # create top 10 data here:
        top10data = [['Tom',12300],['Issac',10800],['Tyler',10600],['Aimee',10000],['Ryan',9500],['Kaufman',3100],
                     ['Ye',1600],['Jacob',1300],['Lucas',1200],['Zhu',100]]
        rank = 1
        font = pg.font.Font(None, 28)
        for eachPlayer,eachScores in top10data:
            player_text = font.render(f"{rank}. {eachPlayer} :   {eachScores}", True, black)
            player_rect = title_text.get_rect(center=(screen_width // 2+20, screen_height // 6+rank*45))
            rank += 1
            screen.blit(player_text, player_rect)


        screen.blit(close_button, close_rect)
        screen.blit(top_text, top_rect)


    else:  # if no other page, just start up page
        screen.blit(title_text, title_rect)
        screen.blit(course_text, course_rect)
        screen.blit(student_text, student_rect)
        screen.blit(play_button, play_rect)
        screen.blit(score_button, score_rect)
        screen.blit(options_button, options_rect)
        screen.blit(quit_button, quit_rect)
        pg.display.flip()
    pg.display.flip()

pg.quit()
sys.exit()