from pydoc import ModuleScanner
import sys
import pygame
import random
from module import *
import defe
import time
import os

        
        # new_img = pygame.transform.flip(self.images[0], True, False)
        
        # newimg = pygame.transform.resize(new_img, (100, 100))

hole_list=[(50, 50), (50, 100), (50, 150), (50, 200), (50, 250), (50, 300), (50, 350), (50, 400), (50, 450), (50, 500), (50, 550), (50, 600), (50, 650), (50, 700), (100, 50), (100, 100), 
(100, 150), (100, 200), (100, 250), (100, 300), (100, 350), (100, 400), (100, 450), (100, 500), (100, 550), (100, 600), (100, 650), (100, 700), (150, 50), (150, 100), (150, 150), (150, 200), (150, 250), (150, 300), (150, 350), (150, 400), (150, 450), (150, 500), (150, 550), (150, 600), (150, 650), (150, 700), (200, 50), (200, 100), (200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450), (200, 500), (200, 550), (200, 600), (200, 650), (200, 700), (250, 50), (250, 100), (250, 150), (250, 200), (250, 
250), (250, 300), (250, 350), (250, 400), (250, 450), (250, 500), (250, 550), (250, 600), (250, 650), (250, 700), (300, 50), (300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400), (300, 450), (300, 500), (300, 550), (300, 600), (300, 650), (300, 700), (350, 50), (350, 100), (350, 150), (350, 200), (350, 250), (350, 300), (350, 350), (350, 400), (350, 450), (350, 500), (350, 550), (350, 600), (350, 650), (350, 700), (400, 50), (400, 100), (400, 150), (400, 200), (400, 250), (400, 300), (400, 350), 
(400, 400), (400, 450), (400, 500), (400, 550), (400, 600), (400, 650), (400, 700), (450, 50), (450, 100), (450, 150), (450, 200), (450, 250), (450, 300), (450, 350), (450, 400), (450, 450), (450, 500), (450, 550), (450, 600), (450, 650), (450, 700), (500, 50), (500, 100), (500, 150), (500, 200), (500, 250), (500, 300), (500, 350), (500, 400), (500, 450), (500, 500), (500, 550), (500, 600), (500, 650), (500, 700), (550, 50), (550, 100), (550, 150), (550, 200), (550, 250), (550, 300), (550, 350), (550, 400), (550, 450), (550, 
500), (550, 550), (550, 600), (550, 650), (550, 700), (600, 50), (600, 100), (600, 150), (600, 200), (600, 250), (600, 300), (600, 350), (600, 400), (600, 450), (600, 500), (600, 550), (600, 600), (600, 650), (600, 700), (650, 50), (650, 100), (650, 150), (650, 200), (650, 250), (650, 300), (650, 350), (650, 400), (650, 450), (650, 500), (650, 550), (650, 600), (650, 650), (650, 700), (700, 50), (700, 100), (700, 150), (700, 200), (700, 250), (700, 300), (700, 350), (700, 400), (700, 450), (700, 500), (700, 550), (700, 600), 
(700, 650), (700, 700), (750, 50), (750, 100), (750, 150), (750, 200), (750, 250), (750, 300), (750, 350), (750, 400), (750, 450), (750, 500), (750, 550), (750, 600), (750, 650), (750, 700), (800, 50), (800, 100), (800, 150), (800, 200), (800, 250), (800, 300), (800, 350), (800, 400), (800, 450), (800, 500), (800, 550), (800, 600), (800, 650), (800, 700), (850, 50), (850, 100), (850, 150), (850, 200), (850, 250), (850, 300), (850, 350), (850, 400), (850, 450), (850, 500), (850, 550), (850, 600), (850, 650), (850, 700), (900, 
50), (900, 100), (900, 150), (900, 200), (900, 250), (900, 300), (900, 350), (900, 400), (900, 450), (900, 500), (900, 550), (900, 600), (900, 650), (900, 700), (950, 50), (950, 100), (950, 150), (950, 200), (950, 250), (950, 300), (950, 350), (950, 400), (950, 450), (950, 500), (950, 550), (950, 600), (950, 650), (950, 700), (1000, 50), (1000, 100), (1000, 150), (1000, 200), (1000, 250), (1000, 300), (1000, 350), (1000, 400), (1000, 450), (1000, 500), (1000, 550), (1000, 600), (1000, 650), (1000, 700), (1050, 50), (1050, 100), (1050, 150), (1050, 200), (1050, 250), (1050, 300), (1050, 350), (1050, 400), (1050, 450), (1050, 500), (1050, 550), (1050, 600), (1050, 650), (1050, 700), (1100, 50), (1100, 100), (1100, 150), (1100, 200), (1100, 250), (1100, 300), (1100, 350), (1100, 400), (1100, 450), (1100, 500), (1100, 550), (1100, 600), (1100, 650), (1100, 700)]

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        #base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def initGame():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1200,800),0,32)
    pygame.display.set_caption('给千千的打青蛙游戏')
    return screen

def startInterface(screen, begin_image_path):
    begin_yuan_image = pygame.image.load(begin_image_path)
    begin_image = begin_yuan_image
    font = pygame.font.SysFont("arial", 64)
    begin_text = font.render('Click anywhere to get started ', True, (0,0,0))
    begin_rect = begin_text.get_rect()
    begin_rect.left, begin_rect.top = (1200 - begin_rect.width) / 2, 400
    while True:
        pygame.mouse.set_visible(True)
        time.sleep(0.1)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mouse_pos[0] in list(range(0, 1200)) and mouse_pos[1] in list(range(200, 600)):
                    return True
        screen.blit(begin_image, (0, 0))
        screen.blit(begin_text, begin_rect)
        pygame.display.update()
        
def resetInterface(screen, begin_image_path, score_info):
    begin_yuan_image = pygame.image.load(begin_image_path)
    begin_image = begin_yuan_image
    font = pygame.font.SysFont("arial", 32)
    your_score_text = font.render('Your Score: %s' % score_info['your_score'], True, (30,144,255))
    your_score_rect = your_score_text.get_rect()
    your_score_rect.left, your_score_rect.top = (1200 - your_score_rect.width) / 2, 500
    best_score_text = font.render('Best Score: %s' % score_info['best_score'], True, (30,144,255))
    best_score_rect = best_score_text.get_rect()
    best_score_rect.left, best_score_rect.top = (1200 - best_score_rect.width) / 2, 550
    end_text = font.render('Click anywhere to return to the start screen', True, (30,144,255))
    end_rect = end_text.get_rect()
    end_rect.left, end_rect.top = (1200 - best_score_rect.width) / 2, 600
    while True:
        pygame.mouse.set_visible(True)
        time.sleep(0.1)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mouse_pos[0] in list(range(0, 1200)) and mouse_pos[1] in list(range(0, 400)):
                    return True, True
                if event.button == 1 and mouse_pos[0] in list(range(0, 1200)) and mouse_pos[1] in list(range(400, 800)):
                    return True, False
        screen.blit(begin_image, (0, 0))
        screen.blit(your_score_text, your_score_rect)
        screen.blit(best_score_text, best_score_rect)
        screen.blit(end_text, end_rect)
        pygame.display.update()


def main():
    screen = initGame()
    font = pygame.font.SysFont("arial", 16)
    score_font = pygame.font.SysFont("arial", 48)
    pygame.mixer.music.load(resource_path(os.path.join('res','Happy.wav')))
    pygame.mixer.music.play(-1)
    audios = {
        'count_down': pygame.mixer.Sound(resource_path(os.path.join('res','10s.mp3'))),
        'hammering': pygame.mixer.Sound(resource_path(os.path.join('res','CARTOON8.WAV'))),
        'jump' : pygame.mixer.Sound(resource_path(os.path.join('res','holejump.wav'))) 
    }
    bg_img = pygame.image.load(resource_path(os.path.join('res','poll.png')))
    
    hole_pos = random.choice(hole_list)
    change_hole_event = pygame.USEREVENT 
    pygame.time.set_timer(change_hole_event, 900)
    # 地鼠
    mole = defe.Mole(resource_path(os.path.join('res','normal.png')), resource_path(os.path.join('res','abnoamal.png')), hole_pos)
    # 锤子
    
    new_img = pygame.transform.flip(pygame.image.load(resource_path(os.path.join('res','ham_normal.png'))), True, False)
    newimg = pygame.transform.scale(new_img, (75, 75))
    abnew_img = pygame.transform.flip(pygame.image.load(resource_path(os.path.join('res','ham_abnormal.png'))), True, False)
    abnewimg = pygame.transform.scale(abnew_img, (75, 75))
    hammer = defe.Hammer(newimg, abnewimg,(500,250))
    # 时钟
    clock = pygame.time.Clock()
    # 分数
    your_score = 0
    # Modu = pygame.image.load(r'C:\Users\mi\Desktop\pydemo\R-C.jpg').convert_alpha()
    init_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    flag = False
    isreturntitle = True
    if isreturntitle:
        flag = startInterface(screen, resource_path(os.path.join('res','begin.png')))
    while flag:
        pygame.mouse.set_visible(False)
        time.sleep(0.01)
        time_remain = round((61000 - (pygame.time.get_ticks() - init_time)) / 1000.)
        if time_remain == 40:
            pygame.time.set_timer(change_hole_event, 750)
        elif time_remain == 20:
            pygame.time.set_timer(change_hole_event, 650)
        if time_remain == 10:
            audios['count_down'].play()
        if time_remain < 0:
            flag = False
            break
        if hammer.is_hammering and not mole.is_hammer:
            is_hammer = pygame.sprite.collide_mask(hammer, mole)
            if is_hammer:
                audios['hammering'].play()
                mole.setBeHammered()
                your_score += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == change_hole_event:
                hole_pos = random.choice(hole_list)
                mole.reset()
                audios['jump'].play()
                mole.setPosition(hole_pos)    
            elif event.type == pygame.MOUSEMOTION:
                hammer.setPosition(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hammer.setHammering()
        
        your_score_text = score_font.render('Score: '+str(your_score), True, (66,78,88))
        count_down_text = font.render('Time: '+str(time_remain), True, (0,0,0))
        screen.blit(bg_img, (0, 0))
        screen.blit(count_down_text, (875, 8))
        screen.blit(your_score_text, (875, 750))
        mole.draw(screen)
        hammer.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    try:
        best_score = int(open(r'score.txt').read())
    except:
        best_score = 0   
    if your_score > best_score:
        best_score = your_score
        f = open(r'score.txt', 'w')
        f.write(str(your_score))
        f.close()
    score_info = {}
    score_info['your_score'] = your_score
    score_info['best_score'] = best_score
    # flag = endInterface(screen, r'end.jfif', r'againxian.jpg', score_info)     
    flag, isreturntitle = resetInterface(screen, resource_path(os.path.join('res','endinterface.png')), score_info)
if __name__ == '__main__':
    main()
    while True:
        is_restart = main()
        if not is_restart:
            break    
    
