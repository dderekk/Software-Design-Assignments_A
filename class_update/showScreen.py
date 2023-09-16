import pygame
import pygame as pg
import sys
from blockControl import Blocks
from escapeWindow import PopupWindow
from inputScoreData import enterData
from music import Music
from configurePage import ConfigurePage
from scorePage import ScorePage
from startUpPage import StartUpPage
from gamePlayPage import gamePlayPage
from TetrisAI import TetrisAI
import random





# initial Pygame
pg.init()
clock = pygame.time.Clock()

# initiallize BGM
bgm_manager = Music()

# set screen size
screen_width = 800
screen_height = 750
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Tetris Game")

# colour defined
white = (255, 255, 255)
black = (0, 0, 0)

# initialize pages
configureP = ConfigurePage(screen)
scoreP = ScorePage(screen)
startP = StartUpPage(screen)
gameP = gamePlayPage(screen)

# game loop
bgm_manager.is_paused = False
configureP.is_active = False
scoreP.is_active = False
gameP.is_active = False
startP.is_active = True
running = True
show_popup = False
paused = False
gameLevel = 1
nameResult = None
#AI
player_control = True
AI_enable = False

def reset_game():
    # Reinitialize the Blocks class

    global gameLevel,paused,show_popup,nameResult
    Blocks.__init__(Blocks)
    bgm_manager.is_paused = False
    configureP.is_active = False
    scoreP.is_active = False
    gameP.is_active = False
    startP.is_active = True

    show_popup = False
    paused = False
    gameLevel = 1
    nameResult = None

while running:
    if not pygame.mixer.music.get_busy() and not bgm_manager.is_paused:
        bgm_manager.play()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_m:
            bgm_manager.pause_or_resume()
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if startP.is_active:
                if startP.score_rect.collidepoint(mouse_pos):
                    scoreP.activate()
                    startP.deactivate()
                elif startP.play_rect.collidepoint(mouse_pos):
                    reset_game()
                    gameP.activate()
                    paused = False
                    s = Blocks.block_size  # size ratio
                    frame_speed = 0
                    speedUp = False
                    pg.init()
                    bgm_manager.fadeout(200)
                    bgm_manager.changeMusic2()

                    # GAME filed
                    while gameP.is_active:
                        popup = PopupWindow()
                        enterName = enterData()
                        if not pygame.mixer.music.get_busy() and not bgm_manager.is_paused:
                            bgm_manager.play()
                        if not Blocks.select_Block:
                            Blocks.select_Block = Blocks.Next_Block
                            Blocks.Next_Block = list(random.choice(Blocks.blocks))
                        elif not Blocks.Next_Block:
                            Blocks.Next_Block = list(random.choice(Blocks.blocks))

                        screen.fill(color=(124, 115, 192))  # RPG backgound colour choise

                        for event in pg.event.get():
                            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                                bgm_manager.pause_or_resume()
                            if event.type == pg.QUIT:  # quit if quit pressed
                                gameP.deactivate()
                                bgm_manager.fadeout(800)
                                bgm_manager.changeMusic1()

                            # POPUP window
                            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:# if button ESC pressed
                                show_popup = True
                            elif event.type == pygame.MOUSEBUTTONDOWN and show_popup:   # if window popup
                                result = popup.handle_event(event)
                                if result == "YES":
                                    show_popup = False
                                    gameP.deactivate()
                                    bgm_manager.fadeout(800)
                                    bgm_manager.changeMusic1()
                                elif result == "NO":
                                    show_popup = False
                                    paused = False

                            elif not paused:    # if didnt paused the game

                                # Game logic for player control
                                if player_control:
                                    if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:  # if button ← pressed
                                        Blocks.movement(Blocks, -1)
                                        bgm_manager.movingeffect1()
                                    elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:  # if button → pressed
                                        Blocks.movement(Blocks, 1)
                                        bgm_manager.movingeffect1()
                                    elif event.type == pg.KEYDOWN and event.key == pg.K_UP:  # if button ↑ pressed
                                        Blocks.rotate(Blocks)
                                        bgm_manager.movingeffect1()
                                    elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:  # if button ↓ pressed
                                        speedUp = True
                                        bgm_manager.movingeffect1()
                                    elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                                        speedUp = False
                                    elif event.type == pg.KEYDOWN and event.key == pg.K_p:  # if button P pressed
                                        paused = True
                                # Game logoic for AI control:
                                if AI_enable:
                                    pass


                            elif event.type == pg.KEYDOWN and event.key == pg.K_p and paused:
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
                                frame_speed += 2*gameLevel
                        Blocks.draw_block(Blocks, screen)
                        pg.display.set_caption("Scores: " + str(Blocks.score[0]))



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
                        gamesScore_rect = gamesScore_text.get_rect(center=(screen_width // 2+160, screen_height // 5 + 60))
                        screen.blit(gamesScore_text, gamesScore_rect)

                        # Number of lines eliminated in the session
                        font = pg.font.Font(None, 36)
                        gamesLines_text = font.render(f"{str(Blocks.complete_row_counts)} lines eliminated", True, black)
                        gamesLines_rect = gamesLines_text.get_rect(
                            center=(screen_width // 2 + 160, screen_height // 5 + 180))
                        screen.blit(gamesLines_text, gamesLines_rect)

                        # Current level
                        font = pg.font.Font(None, 36)
                        gamesLevel_text = font.render(f"Current level: {gameLevel}", True,
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
                        #score change levels
                        if 0 <= Blocks.score[0]<1000 and gameLevel == 0:
                            gameLevel = 1
                        elif 1000 <= Blocks.score[0]<3000 and gameLevel == 1:
                            gameLevel = 2
                        elif 3000 <= Blocks.score[0]<8000 and gameLevel == 2:
                            gameLevel = 3
                            bgm_manager.changeMusic3()
                        elif 8000 <= Blocks.score[0]<20000 and gameLevel == 3:
                            gameLevel = 4
                        elif 20000<= Blocks.score[0]<50000 and gameLevel == 4:
                            gameLevel = 5
                            bgm_manager.changeMusic4()
                        elif Blocks.score[0] >= 50000:
                            gameLevel = 6
                            bgm_manager.changeMusic5()

                        if Blocks.gameOver:
                            enterName.active = True
                        if enterName.active:
                            enterName.whileloop()
                            reset_game()


                        pg.display.flip()  # refresh

                    pygame.display.update()
                elif startP.options_rect.collidepoint(mouse_pos):
                    configureP.activate()
                    startP.deactivate()
                elif startP.quit_rect.collidepoint(mouse_pos):
                    running = False
            elif configureP.is_active:
                if configureP.mode_rect.collidepoint(mouse_pos):
                    configureP.player_control = not configureP.player_control
                    configureP.AI_enable = not configureP.AI_enable
                if configureP.close_rect.collidepoint(mouse_pos):
                    configureP.deactivate()
                    startP.activate()
            elif scoreP.is_active:
                if scoreP.close_rect.collidepoint(mouse_pos):
                    scoreP.deactivate()
                    startP.activate()

    screen.fill(white)
    if configureP.is_active:
        startP.deactivate()
        # in Configure
        configureP.draw(screen)

    elif scoreP.is_active:
        startP.deactivate()
        # in Top 10
        scoreP.draw(screen)

    else:  # if no other page, just start up page
        startP.draw(screen)
    pg.display.flip()

pg.quit()
sys.exit()