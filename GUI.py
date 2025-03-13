import pygame
import os
import datetime

# Initialisiere Pygame
pygame.init()

# Farben definieren
HINTERGRUND = (34, 39, 41)
STIFT = (255, 255, 255)
stift_groesse = 4

class Zeichenklasse:
    def __init__(self, bildschirm, farbe, groesse):
        self.bildschirm = bildschirm
        self.farbe = farbe
        self.groesse = groesse
        self.zeichnen = True
        self.letzte_pos = None
        self.liste = []
    
    def starte_zeichnen(self, pos):
        self.zeichnen = True
        self.letzte_pos = pos
    
    def beende_zeichnen(self):
        self.zeichnen = False
        self.letzte_pos = None

    def zeichenzustand(self):
        return self.zeichnen
    
    def zeichne(self):
        if self.zeichnen:
            maus_pos = pygame.mouse.get_pos()
            if self.letzte_pos != None:
                pygame.draw.line(self.bildschirm, self.farbe, self.letzte_pos, maus_pos, self.groesse)
                #satz des Pythagoras
                d = int((self.letzte_pos[0] - maus_pos[0])**2) + ((self.letzte_pos[1] - maus_pos[1])**2)

                print(self.letzte_pos[0])
                if d > 121:
                    self.liste += maus_pos
                self.letzte_pos = maus_pos
            pygame.display.flip()
    def liste(self):
        return self.liste
    def zeichneX(self,x,y):
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y - self.groesse), (x + self.groesse, y + self.groesse), stift_groesse)
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y + self.groesse), (x + self.groesse, y - self.groesse), stift_groesse)
        pygame.display.flip()
    def zeichneKreis(self,mx,my,r):
        pygame.draw.circle(self.bildschirm, self.farbe, (mx, my), r, stift_groesse)
        pygame.display.flip()


class Button:
    def __init__(self, img, pos, size, color, font_size):
        self.img = img
        self.rect = pygame.Rect(pos, size)
        self.color = color
        self.font = pygame.font.SysFont('Arial', font_size)
    
    def draw(self, screen):
        if self.img:
            img_surface = pygame.image.load(self.img).convert_alpha()
            img_surface = pygame.transform.scale(img_surface, self.rect.size)
            screen.blit(img_surface, self.rect.topleft)
        else:
            text_surface = self.font.render(self.img, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class Gui:
    def __init__(self, window_width, window_height):
        self.bildschirm = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Pirfekt v3.14")
        pygame.display.set_icon(pygame.image.load('./logos/pirfekt1.png'))
        self.laeuft = True
        self.zeichenklasse = Zeichenklasse(self.bildschirm, STIFT, stift_groesse)
        self.pirfektLogo = pygame.image.load('./logos/pirfektLogo circ.png').convert_alpha()
        self.pirfektLogoSurface = pygame.transform.scale(self.pirfektLogo, (70,70))
        self.neu_knopf = Button('./logos/pirfektreload 1.png', (900, 40), (70, 70), (65, 90, 99), 30)
        self.speichern_knopf = Button('./logos/pirfektsave circ1.png', (1050, 40), (70, 70), (65, 90, 99), 30)
        self.showtext()
        self.showbutton()
    
    def createwindow(self, window_width, window_height):
        self.bildschirm = pygame.display.set_mode((window_width, window_height))
    
    def showbutton(self):
        self.neu_knopf.draw(self.bildschirm)
        self.speichern_knopf.draw(self.bildschirm)
        self.bildschirm.blit(self.pirfektLogoSurface,(100,40))
    
    def showtext(self):
        font = pygame.font.SysFont('Arial', 30)
        infoText = font.render("Zeichnen Sie einen Kreis!", True, (255, 255, 255))
        self.bildschirm.fill(HINTERGRUND)
        self.bildschirm.blit(infoText, (300, 60))
        pygame.display.flip()
    
    def reset(self):
        self.bildschirm.fill(HINTERGRUND)
        self.zeichenklasse.zeichnen = True
        self.zeichenklasse.liste = []  # Leere die Liste der gezeichneten Punkte
        self.zeichenklasse.letzte_pos = None  # Setze die letzte Position zurück
        self.showtext()
        self.showbutton()
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.laeuft = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.neu_knopf.is_clicked(event):
                    self.reset()
                elif self.speichern_knopf.is_clicked(event):
                    print("Speichern")
                elif self.zeichenklasse.zeichnen:
                    self.zeichenklasse.starte_zeichnen(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.zeichenklasse.beende_zeichnen()
                
    
    def update(self):
        self.zeichenklasse.zeichne()
    
    def is_running(self):
        return self.laeuft

    def testkreis(self):
        self.zeichenklasse.zeichneKreis(500,500,100)
    def testmittelpunkt(self, x,y):
        self.zeichenklasse.zeichneX(x,y)


