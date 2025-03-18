# Das ist das Hauptprogamm, welches die Abläufe in dem Spiel regelt

# importiert die Klassen GUI und Kreis
from GUI import * 
from Kreis import *

# Fenster mit der Größe 1280, 720 wird erstellt
gui = Gui(1280, 720)
gui.reset()

mittelpunkt = False

# Die Schleife läuft so lange das Fenster offen ist
while gui.is_running():
    if gui.zeichenklasse.zeichenzustand():
        gui.handle_events()
        gui.update()
        mittelpunkt = False
    else:
        
        if mittelpunkt == False and len(gui.zeichenklasse.liste) > 5: # Prüft ob die Punktliste der Zeichnung mindestens mehr als 5 Punkte hat, um falsche Auswertungen zu vermeiden
            # Auswertung wird gestartet
            # Ein Objekt wird erstellt von dem der Mittelpunkt, Radius und Score ermittelt wird
            kreis = Kreis(gui.zeichenklasse.liste)

            # for i in range(int(len(kreis.pixellist)/2)):                          ### --> aktivieren um die Punkte durch ein X zu kennzeichnen
            #    gui.testmittelpunkt(kreis.pixellist[i*2],kreis.pixellist[i*2+1])   ### --> aktivieren um die Punkte durch ein X zu kennzeichnen

            kreis.mittelpunkt = kreis.findeMittelpunkt()
            mittelpunkt = kreis.mittelpunkt
            gui.testmittelpunkt(kreis.mittelpunkt[0], kreis.mittelpunkt[1]) # Mittelpunkt wird gezeichnet
            kreis.radius = kreis.findeRadius()
            gui.testkreis(kreis.mittelpunkt[0],kreis.mittelpunkt[1],kreis.radius) # Kreis wird gezeichnet
            score = kreis.findeScore()
            gui.showScore(score)
            # Fals der score ein neuer Hightscore ist wird dieser als Hightscore übernommen
            if score > gui.highscore:
                gui.setHScore(score)
                

        gui.handle_events()
        gui.update()

# Program wird geschlossen
pygame.quit()




