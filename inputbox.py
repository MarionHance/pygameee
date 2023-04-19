import pygame as pg

class InputBox:

    def __init__(self, x, y, w, h, text='ENTER NAME',mscreen=None):
        self.rect = pg.Rect(x, y, w, h)
        self.color__inactive = pg.Color('red1')
        self.color_active = pg.Color('white')
        self.color = self.color__inactive
        self.text = text 
        self.font = pg.font.SysFont('Verdana', 18, 0)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.fait = False
        self.screen = mscreen

    def handle_event(self, event): 
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                if self.text == "ENTER NAME":
                    self.text = ""
                self.txt_surface = self.font.render(self.text, True, self.color)
                self.draw(self.screen)
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color__inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.fait = True
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
                self.draw(self.screen)
    
    def update(self):
        width = max(180, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)
        
    
            






