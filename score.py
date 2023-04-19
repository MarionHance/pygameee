import os
import json
import pygame

class Score:
    def __init__(self, score=0, user_name='test'):
        self.updated = False
        self.name_needed = False
        self.name = user_name
        self.old_score = []
        self.new_score = score
        self.existing_files = False
        self.check_files()
        self.load_old_score()
        self.score_rect = (100, 400)

    
    def draw_score(self, number):
        font = pygame.font.SysFont('Verdana', 20, 0)
        font2 = pygame.font.SysFont('Verdana', 30, 1)
        if number == 0:
            score_text = font2.render("BEST SCORES !!!", 1, (255, 255, 255))
            self.score_rect = (65, 410)
        else:
            score_text = font.render(f"{number}°: {self.old_score[number + number-1]} pts for {self.old_score[number + number -2]}", 1, (255, 255, 255))
            self.score_rect = (100, 450 + (20*(number-1)))
        return score_text





    def check_files(self):
        if os.path.exists('score.txt'):
            self.existing_files = True
        
        else:
            self.creating_default()

    def creating_default(self):
        if not self.existing_files:
            default = open("score.txt", "w")
            json.dump(["default", 5, "default", 4, "default", 3, "default", 2, "default", 1], default)
            default.close()
            self.exosting_files = True

    def load_old_score(self):
        if self.existing_files:
            op = open("score.txt", "r")
            self.old_score = json.load(op)
            op.close()
    
    def check_update(self):
        if self.new_score >= self.old_score[9]:
            self.name_needed = True

    def update_score(self):
        if not self.updated:

            fichier = open("score.txt", "w")

            if self.new_score >= self.old_score[1]:
                for i in range(7, -1, -1):
                    self.old_score[i+2] = self.old_score[i]
                self.old_score[0] = self.name
                self.old_score[1] = self.new_score
            elif self.new_score >= self.old_score[3]:
                for i in range (7, 1, -1):
                    self.old_score[i+2] = self.old_score[i]
                self.old_score[2] = self.name
                self.old_score[3] = self.new_score
            elif self.new_score >= self.old_score[3]:
                for i in range (7, 3, -1):
                 self.old_score[i+2] = self.old_score[i]
                self.old_score[4] = self.name
                self.old_score[5] = self.new_score
            elif self.new_score >= self.old_score[3]:
                for i in range (7, 5, -1):
                    self.old_score[i+2] = self.old_score[i]
                self.old_score[6] = self.name
                self.old_score[7] = self.new_score
            elif self.new_score >= self.old_score[9]:
                self.old_score[8] = self.name
                self.old_score[9] = self.new_score

            json.dump(self.old_score, fichier)
            print(self.old_score)
            fichier.close()
            self.name_needed = False
            self.updated =  True

# score = Score(5)
# score.check_files()
# # score.load_old_score()
# # score.check_update()



