import pygame
import sys
import math
import time
from enemy import Enemy
from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py
from spaceship import Spaceship
#import the class Spaceship from the file spaceship.py

from screen import *
from affichage import *

#définir une clock
clock = pygame.time.Clock()
FPS = 100

#Initialize Pygame
pygame.init()



game = Game()
settings = Settings()

game.screen.show_screen()
#Boucle de jeu

running = True

while running:

    # draw scrolling background
    if game.is_playing:
        #Scroll background
        game.screen.scrolling(5)
    else:
        #Scroll background
        game.screen.scrolling(2)
    
     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing):
        #déclencher les instructions de la partie
        game.update() 
    elif((not game.is_playing) and game.name_needed):
        while game.name_needed:
            game.entername(game.screen.screen)    
        game.inputbox.active = False
        game.inputbox.fait = False
    #---------settings--------#
    elif((not game.is_playing) and game.are_buttons_settings_shown()):

        game.to_show_settings()
        
    #Show the screen with the difficulties
    elif(not game.is_playing and game.are_buttons_planete_shown()):
        game.show_planetes()


    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and game.are_buttons_difficulty_shown()):
        game.show_game_modes()
       
    #vérifier si notre jeu n'a pas commencé
    else:
        game.show_menu()

        for i in range(0,6):
            game.screen.screen.blit(game.load_score.draw_score(i), game.load_score.score_rect)
    game.show_buttons()
    
    
    #Dessin de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
            

        if event.type == pygame.KEYDOWN and game.is_playing:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            #détecter si la touche ctrl est enclenchée pour lancer notre ult
            if event.key == pygame.K_LCTRL:
                game.player.ultimate(game.ult_event)
            #détecter si la touche alt est enclenchée pour lancer bomb
            if event.key == pygame.K_LALT:
                game.player.smart_bomb()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):


            #vérification pour svaoir si la souris est en collision avec le bouton
            if (game.button_play.button_rect.collidepoint(event.pos) and game.button_play.is_shown):
                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            if(game.buttons_settings[0].button_rect.collidepoint(event.pos) and game.buttons_settings[0].is_shown):
         
                game.to_show_settings()

            elif(game.button_back.button_rect.collidepoint(event.pos) and game.button_back.is_shown):
                if(game.are_buttons_difficulty_shown()):
                    game.show_planetes()
                elif(game.are_buttons_planete_shown() or game.are_buttons_settings_shown()):
                    game.show_menu()
                    
            for i in range(1,6,2):
                if(game.buttons_settings[i].button_rect.collidepoint(event.pos) and game.buttons_settings[i].is_shown):
                    game.reset_show_settings()
                    game.buttons_settings[i+1].is_shown = True

           
            
            for i in range(0,3):
                if (game.buttons_difficulties[i].button_rect.collidepoint(event.pos) and game.buttons_difficulties[i].is_shown):
                    game.create_player(i+1)
                    game.start()
            i = 0     
            if (game.button_space.button_rect.collidepoint(event.pos) and game.are_buttons_planete_shown()):
                game.show_game_modes()
            for planete in game.buttons_planetes:
                
                if (planete.button_rect.collidepoint(event.pos) and game.are_buttons_planete_shown()):
                    game.screen.change_bg(f"PygameAssets/planete{i}map.png")
                    game.show_game_modes()
                i += 1
                #mettre le jeu en monde "lancé"
                

           
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
