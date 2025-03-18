import pygame
import os
import datetime

# Initialisiere Pygame
pygame.init()

# Farben definieren
HINTERGRUND = (34, 39, 41)      # Definieren der Farbe für den Hintergrund
FORDERGRUND = (255, 255, 255)   # Definieren der Farbe für den Fordergrund
stift_groesse = 4

class Zeichenklasse:
    '''
    Klasse die für das Zeichnen zuständig ist.

    Benötigt die pygame-Bildschirmfläche, die gewünschte zeichen-Farbe, und die größe der Line.
    '''    
    def __init__(self, bildschirm, farbe, groesse):
        self.bildschirm = bildschirm
        self.farbe = farbe
        self.groesse = groesse
        self.zeichnen = True
        self.letzte_pos = None
        self.liste = []
    
    def starte_zeichnen(self, pos):
        '''
        Methode von der Klasse Zeichenklasse, die dafür sorgt dass gezeichnet werden kann; Das eine Zeichnung/Strich anfängt.

        Braucht die letzte Position der Maus.

        '''    

        self.zeichnen = True
        self.letzte_pos = pos
    
    def beende_zeichnen(self):
        '''
        Methode von der Klasse Zeichenklasse, die dafür sorgt dass NICHT MEHR gezeichnet werden kann.
        '''  
        self.zeichnen = False
        self.letzte_pos = None

    def zeichenzustand(self):
        '''
        Methode von der Klasse Zeichenklasse, die den Zeichnezustand als Bool zurückgibt.
        '''          
        return self.zeichnen
    
    def zeichne(self):
        '''
        Methode von der Klasse Zeichenklasse, die für das Zeichnen selber zuständig ist.
        '''   
        if self.zeichnen:
            maus_pos = pygame.mouse.get_pos()
            if self.letzte_pos != None:
                pygame.draw.line(self.bildschirm, self.farbe, self.letzte_pos, maus_pos, self.groesse)
                
                d = int((self.letzte_pos[0] - maus_pos[0])**2) + ((self.letzte_pos[1] - maus_pos[1])**2) #satz des Pythagoras
                if d > 50:                                     ##################### <---- hier Punkt-dichte ändern | Wenn der Abstand >50LE ist, wird eine neuer Punkt gespeichert

                    # print(str(self.letzte_pos) + "  --  " + str(maus_pos) + "  --  " + str(d)) ## Aktivieren wenn man die letzte Maus position und die aktuelle mausposition sehen möchte

                    self.liste += maus_pos
                    self.letzte_pos = maus_pos
            pygame.display.flip()

    def zeichneX(self,x,y):
        '''
        Methode von der Klasse Zeichenklasse, die ein X Einzeichnet (z.B. Um den Mitttelpunkt anzuzeigen oder die Punkte vom Kreis).

        Braucht die x und y Koordinate vom Mittelpunkt des zu zeichnenden X.
        '''        
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y - self.groesse), (x + self.groesse, y + self.groesse), stift_groesse)
        pygame.draw.line(self.bildschirm, self.farbe, (x - self.groesse, y + self.groesse), (x + self.groesse, y - self.groesse), stift_groesse)
        pygame.display.flip()
        
    def zeichneKreis(self,mx,my,r):
        '''
        Methode von der Klasse Zeichenklasse, die ein Kreis Einzeichnet.

        Braucht die x und y Koordinate vom Mittelpunkt und den Radius des Kreises.
        '''    
        pygame.draw.circle(self.bildschirm, (255, 100, 100), (mx, my), r, 2)
        pygame.display.flip()

class Button:
    '''
    Klasse Button: Klasse für Knöpfe aus Bildern.

    Attribute: img (für das Bild im Knopf), pos (position des Knopfs), size (länge des Knopfs)
    '''
    def __init__(self, img, pos, size ):
        self.img = img
        self.rect = pygame.Rect(pos, size)
        

    
    def draw(self, screen):
        '''
        Methode von der Klasse Button, die den Knopf zeichnet. Brauch den Pygame-Bildschirm auf dem der Knopf gezeichnet werden soll.
        '''
        
        img_surface = pygame.image.load(self.img).convert_alpha()
        img_surface = pygame.transform.scale(img_surface, self.rect.size)
        screen.blit(img_surface, self.rect.topleft)

    
    def is_clicked(self, event):
        '''
        Methode von der Klasse Button, die prüft ob der Knopf gedrückt wird also ob eine Maustaste über dem Knopf gedrückt wird. Gibt einen Boolean zurück.
        '''

        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class Gui:
    '''
    Klasse GUI: Klasse für die Benutzeroberfläche (GUI = Graphical User Interface).

    Nimmt Fensterbreite und Fensterhöhe an.
    '''

    def __init__(self, fenster_breite, fenster_hoehe):
        # Fenstereinstellungen:
        self.bildschirm = pygame.display.set_mode((fenster_breite, fenster_hoehe))
        pygame.display.set_caption("Pirfekt v3.14")
        pygame.display.set_icon(pygame.image.load('./logos/pirfekt1.png'))
        # Variablen:
        self.laeuft = True
        self.zeichenklasse = Zeichenklasse(self.bildschirm, FORDERGRUND, stift_groesse)
        self.pirfektLogo = pygame.image.load('./logos/pirfektLogo circ.png').convert_alpha()
        self.pirfektLogoSurface = pygame.transform.scale(self.pirfektLogo, (70,70))
        self.neu_knopf = Button('./logos/pirfektreload 1.png', (900, 40), (70, 70))
        self.speichern_knopf = Button('./logos/pirfektsave circ1.png', (1050, 40), (70, 70) )
        self.highscore = 0

        # Zeigt GUI-Elemente durch die Methoden an
        self.showtext()
        self.showbutton()
    

    
    def showbutton(self):
        '''
        Methode von der Klasse GUI, die die Knöpfe zum Speichern und Neustarten (und auch das Knopfähnlichaussehende Logo oben links) anzeigt/rendert.
        '''        
        self.neu_knopf.draw(self.bildschirm)
        self.speichern_knopf.draw(self.bildschirm)
        self.bildschirm.blit(self.pirfektLogoSurface,(90 ,20))
    
    def showtext(self):
        '''
        Methode von der Klasse GUI, die den Text "Zeichnen Sie einen Kreis!" anzeigt/rendert.
        '''          
        font = pygame.font.SysFont('Arial', 30)  # Definiere Schriftart
        infoText = font.render("Zeichnen Sie einen Kreis!", True, FORDERGRUND) # Text mit der Schriftart definieren/speichern
        self.bildschirm.blit(infoText, (340, 60)) #Text Einblenden
        pygame.display.flip() #Aktualiesieren

    def showScore(self,score):
        '''
        Methode von der Klasse GUI, die den Score/die Punktzahl anzeigt/rendert.

        Erwartet den Score.
        '''         
        font = pygame.font.SysFont('Arial', 35)
        scoreText = font.render(f'Score: {round(score,2)}', True, FORDERGRUND)
        self.bildschirm.blit(scoreText, (300, 100))
        pygame.display.flip()


    def showHScore(self,highscore):
        '''
        Methode von der Klasse GUI, die den Highscore/die höchste Punktzahl anzeigt/rendert.

        Erwartet den Highscore.

        '''          
        font = pygame.font.SysFont('Arial', 30)
        scoreText = font.render(f'Highscore: {round(highscore,2)}', True, FORDERGRUND)
        self.bildschirm.blit(scoreText, (90, 103))
        pygame.display.flip()

    def setHScore(self, hscore):
        '''
        Methode von der Klasse GUI, die den Highscore/die höchste Punktzahl überschreibt.

        Erwartet den Highscore.

        '''   
        self.highscore = hscore

    def reset(self):
        '''
        Methode von der Klasse GUI, die dafür sorgt, dass der Reset-Knopf funktioniert.

        Wenn die Methode Aufgerufgen wird, wird der Bildschrim geleert die UI-Elemente angezeigt und die Punktliste zurückgesetzt, sowie ein print-Befehl erzeugt

        '''          
        self.zeichenklasse.zeichnen = True  # Zeichnen wieder Erlauben
        print("reset")
        self.bildschirm.fill(HINTERGRUND) # Bildschirm mit der Hintergrundfarbe füllen --> "leerer" Bildschirm
        self.zeichenklasse.liste = []  # Leere die Liste der gezeichneten Punkte
        self.zeichenklasse.letzte_pos = None  # Setze die letzte Position zurück
        # Zeige UI-Elemente und Aktualisiere:
        self.showtext()
        self.showbutton()
        self.showHScore(self.highscore)
        pygame.display.flip()


    def screenshot_speichern(self):

        '''
        Methode von der Klasse GUI, die dafür sorgt, dass der Speichern/Screenshot-Knopf funktioniert.

        Wenn die Methode Aufgerufgen wird, wird ein Screenshot gespiechert (mehr dazu in der readme.md Datei), sowie ein print-Befehl erzeugt

        '''      

        zeitstempel = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') # Zeitstempelformat Bsp.:  20250309_140937
        speicherpfad = os.path.join(os.getcwd(), 'screenshots')  ## Speicherpfad auf ./screenshots setzen
        if not os.path.exists(speicherpfad):
            os.makedirs(speicherpfad)
        pygame.image.save(self.bildschirm, os.path.join(speicherpfad, f'screenshot_{zeitstempel}.png'))
        
    
    def handle_events(self):
        '''
        Methode von der Klasse GUI, die dafür sorgt, dass Pygame-"Events" erkannt und Behandelt werden also wenn u.a. die Maustaste gedrückt wird oder die Tastatur usw.

        '''    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Wenn man auf programm beenden drückt (vom Betriebssystem Abhängig)
                self.laeuft = False # Setze laeuft auf False --> in der main.py schleife wird die Schleife beendet also das programm beendet (wegen der letzten main Zeile). 

            elif event.type == pygame.MOUSEBUTTONDOWN: # Wenn Maustaste gedrückt wird:

                if self.neu_knopf.is_clicked(event): # Wen der neuknopf gedrückt wird:
                    self.reset() 

                elif self.speichern_knopf.is_clicked(event): # Wenn der Screenshot/Speichern Knopf gedrückt wird:
                    print("Speichern")
                    self.screenshot_speichern()

                elif self.zeichenklasse.zeichnen: # Wenn kein Knopf gedrückt wurde, also etwas andres:
                    self.zeichenklasse.starte_zeichnen(event.pos) 

            elif  event.type == pygame.KEYDOWN: # Wenn eine Tastatur-Taste gedrückt wird:

                if  event.key == pygame.K_c: # Wenn "c" gedrückt wurde:
                    self.reset()

                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL: # Wenn ("Strg" + "S") gedrückt wurde:
                    print("Speichern")
                    self.screenshot_speichern()

            elif event.type == pygame.MOUSEBUTTONUP and self.zeichenklasse.letzte_pos != None: # Wenn die Maustaste wieder lossgelassen wird UND eine Zeichnung stattgefunden hat (sonst beendet das losslasen über einem Knopf schon das Spiel):
                self.zeichenklasse.beende_zeichnen()
                
    
    def update(self):
        '''
        Methode von der Klasse GUI, die dafür sorgt, dass das Zeichnen funktioniert, durch abrufen der zeichne Methode von der Zeichenklasse.

        '''           
        self.zeichenklasse.zeichne()
    
    def is_running(self):
        '''
        Methode von der Klasse GUI, die angibt (bool) ob das Spiel läuft (also ob man Zeichnen kann oder eben nicht).

        '''         
        return self.laeuft

    def testkreis(self, x, y, r):
        '''
        Methode von der Klasse GUI, die mit der zeichenklasse einen "ideal-Kreis" zeichnet.

        Braucht die x-Koordinate vom Mittelpunkt, die y-Koordinate vom Mittelpunkt und den Radius.

        '''    
        self.zeichenklasse.zeichneKreis(x, y, r)

    def testmittelpunkt(self, x,y):
        '''
        Methode von der Klasse GUI, die mit der zeichenklasse den Mittelpunkt einzeichnet (mit einem X).

        Braucht die x-Koordinate vom Mittelpunkt, die y-Koordinate vom Mittelpunkt.

        '''            
        self.zeichenklasse.zeichneX(x,y)


