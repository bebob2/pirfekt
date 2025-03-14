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
                if d > 50:                                     #####################hier Punkt-dichte ändern
                    # print(str(self.letzte_pos) + "  --  " + str(maus_pos) + "  --  " + str(d)) 
                    self.liste += maus_pos
                    self.letzte_pos = maus_pos
            pygame.display.flip()

    def zeichneX(self,x,y):
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y - self.groesse), (x + self.groesse, y + self.groesse), stift_groesse)
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y + self.groesse), (x + self.groesse, y - self.groesse), stift_groesse)
        pygame.display.flip()
    def zeichneKreis(self,mx,my,r):
        pygame.draw.circle(self.bildschirm, (255, 100, 100), (mx, my), r, 2)
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
        self.highscore = 0
        self.showtext()
        self.showbutton()
    
    def createwindow(self, window_width, window_height):
        self.bildschirm = pygame.display.set_mode((window_width, window_height))
    
    def showbutton(self):
        self.neu_knopf.draw(self.bildschirm)
        self.speichern_knopf.draw(self.bildschirm)
        self.bildschirm.blit(self.pirfektLogoSurface,(90 ,20))
    
    def showtext(self):
        font = pygame.font.SysFont('Arial', 30)
        infoText = font.render("Zeichnen Sie einen Kreis!", True, STIFT)
        self.bildschirm.fill(HINTERGRUND)
        self.bildschirm.blit(infoText, (340, 60))
        pygame.display.flip()

    def showScore(self,score):
        font = pygame.font.SysFont('Arial', 35)
        scoreText = font.render(f'Score: {round(score,2)}', True, STIFT)
        # self.bildschirm.fill(HINTERGRUND)
        self.bildschirm.blit(scoreText, (300, 100))
        pygame.display.flip()

    def setHScore(self, hscore):
        self.highscore = hscore

    def showHScore(self,highscore):
        font = pygame.font.SysFont('Arial', 30)
        scoreText = font.render(f'Highscore: {round(highscore,2)}', True, STIFT)
        # self.bildschirm.fill(HINTERGRUND)
        self.bildschirm.blit(scoreText, (90, 103))
        pygame.display.flip()

    def reset(self):
        self.zeichenklasse.zeichnen = True
        print("reset")
        self.bildschirm.fill(HINTERGRUND)
        self.zeichenklasse.liste = []  # Leere die Liste der gezeichneten Punkte
        self.zeichenklasse.letzte_pos = None  # Setze die letzte Position zurück
        self.showtext()
        self.showbutton()
        self.showHScore(self.highscore)
        pygame.display.flip()


    def screenshot_speichern(self):
        # Screenshot speichern
        zeitstempel = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        speicherpfad = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(speicherpfad):
            os.makedirs(speicherpfad)
        pygame.image.save(self.bildschirm, os.path.join(speicherpfad, f'screenshot_{zeitstempel}.png'))
        
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.laeuft = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.neu_knopf.is_clicked(event):
                    self.reset()
                elif self.speichern_knopf.is_clicked(event):
                    print("Speichern")
                    self.screenshot_speichern()
                elif self.zeichenklasse.zeichnen:
                    self.zeichenklasse.starte_zeichnen(event.pos)
            elif  event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_c:
                    self.reset()
                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    print("Speichern")
                    self.screenshot_speichern()
            elif event.type == pygame.MOUSEBUTTONUP and self.zeichenklasse.letzte_pos != None:
                self.zeichenklasse.beende_zeichnen()
                
    
    def update(self):
        self.zeichenklasse.zeichne()
    
    def is_running(self):
        return self.laeuft

    def testkreis(self, x, y, r):
        self.zeichenklasse.zeichneKreis(x, y, r)

    def testmittelpunkt(self, x,y):
        self.zeichenklasse.zeichneX(x,y)


