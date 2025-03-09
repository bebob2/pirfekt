import pygame
import os
import datetime

# Initialisiere Pygame
pygame.init()

# Richte die Farben ein
HINTERGRUND = (34, 39, 41)
STIFT = (255, 255, 255)

# Richte den Stift ein
stift_groesse = 4

class ZeichneX:
    def __init__(self, bildschirm, farbe, groesse):
        self.bildschirm = bildschirm
        self.farbe = farbe
        self.groesse = groesse

    def zeichnen(self, mitte_x, mitte_y):
        # Zeichne ein X in der Mitte des Kreises
        pygame.draw.line(self.bildschirm, self.farbe, (mitte_x - self.groesse, mitte_y - self.groesse), (mitte_x + self.groesse, mitte_y + self.groesse), stift_groesse)
        pygame.draw.line(self.bildschirm, self.farbe, (mitte_x - self.groesse, mitte_y + self.groesse), (mitte_x + self.groesse, mitte_y - self.groesse), stift_groesse)
        pygame.display.flip()

class Button:
    def __init__(self, text, pos, size, color, font_size):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont('Arial', font_size)
        self.rect = pygame.Rect(pos, size)

    def draw(self, screen):
        # Zeichne den Button
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        # Überprüfe, ob der Button geklickt wurde
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Canvas:
    def __init__(self):
        # Fenster erstellen
        self.bildschirm = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Pirfekt v3.14")
        logo = pygame.image.load('./logos/pirfekt1.png')
        pygame.display.set_icon(logo)

        # Variablen definieren
        self.punkte = []
        self.zeichnen = False
        self.letzte_pos = None
        self.x_zeichnen = ZeichneX(self.bildschirm, STIFT, 5)
        self.laeuft = True
        self.zeichnen_abgeschlossen = False
        self.start = True

        # Texte und Knöpfe definieren
        self.font = pygame.font.SysFont('Arial', 30)
        self.infoText1 = self.font.render("Zeichnen Sie einen Perfekten Kreis!", True, (255, 255, 255)) 
        self.infoText2 = self.font.render("Zum Neustarten drücken Sie auf den 'Neu' Knopf oder 'c' ", True, (255, 255, 255)) 

        self.neu_knopf = Button("Neu", (900, 100), (100, 50), (65, 90, 99), 30)
        self.speichern_knopf = Button("Speichern", (1010, 100), (120, 50), (65, 90, 99), 30)
        self.leere_leinwand()
        # Texte zeichnen
        self.bildschirm.blit(self.infoText1, (300, 60))
        self.bildschirm.blit(self.infoText2, (200, 100))
        pygame.display.flip()
    
    def verarbeite_ereignisse(self):
        # Ereignisse verarbeiten
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                self.laeuft = False
            elif ereignis.type == pygame.MOUSEBUTTONDOWN:
                self.start = False
                if self.neu_knopf.is_clicked(ereignis):
                    self.leere_leinwand()
                elif self.speichern_knopf.is_clicked(ereignis):
                    self.screenshot_speichern()
                elif not self.zeichnen_abgeschlossen:
                    self.zeichnen = True
                    self.letzte_pos = pygame.mouse.get_pos()
            elif ereignis.type == pygame.MOUSEBUTTONUP and self.zeichnen:
                self.zeichnen = False
                self.letzte_pos = None
                self.zeichnen_abgeschlossen = True
                if len(self.punkte) >= 2:
                    self.mittelpunkt_zeichnen()
                self.zeichnen_abgeschlossen = True
            elif ereignis.type == pygame.KEYDOWN:
                self.verarbeite_tastendruck(ereignis)

    def verarbeite_tastendruck(self, ereignis):
        # Tastendrücke verarbeiten
        if ereignis.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
            # Wenn 'Strg + S' gedrückt wird, einen Screenshot speichern
            self.screenshot_speichern()
        elif ereignis.key == pygame.K_c:
            # Wenn 'c' gedrückt wird, die Leinwand leeren
            self.leere_leinwand()

    def zeichne(self):
        # Zeichnen
        if self.zeichnen and not self.zeichnen_abgeschlossen:
            maus_pos = pygame.mouse.get_pos()
            if self.letzte_pos != None:
                pygame.draw.line(self.bildschirm, STIFT, self.letzte_pos, maus_pos, stift_groesse)
                if self.letzte_pos != maus_pos:
                    self.punkte.append(self.letzte_pos)
                    self.punkte = list(set(self.punkte))
                    # print(self.punkte)
                self.letzte_pos = maus_pos
            pygame.display.flip()

    def run(self):
        # Hauptschleife
        while self.laeuft:
            self.verarbeite_ereignisse()
            self.zeichne()

    def mittelpunkt_zeichnen(self):
        # Zeichne X in der Mitte des Kreises
        start_pos, end_pos = self.punkte[0], self.punkte[1]
        mitte_x = (start_pos[0] + end_pos[0]) // 2
        mitte_y = (start_pos[1] + end_pos[1]) // 2
        self.x_zeichnen.zeichnen(mitte_x, mitte_y)

    def screenshot_speichern(self):
        # Screenshot speichern
        zeitstempel = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        speicherpfad = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(speicherpfad):
            os.makedirs(speicherpfad)
        pygame.image.save(self.bildschirm, os.path.join(speicherpfad, f'screenshot_{zeitstempel}.png'))

    def leere_leinwand(self):
        # Leinwand leeren
        self.bildschirm.fill(HINTERGRUND)
        self.punkte = []
        self.zeichnen_abgeschlossen = False
        self.start = True
        self.neu_knopf.draw(self.bildschirm)
        self.speichern_knopf.draw(self.bildschirm)
        self.bildschirm.blit(self.infoText1, (300, 60))
        self.bildschirm.blit(self.infoText2, (200, 100))
        pygame.display.flip()

canvas = Canvas()
canvas.run()








