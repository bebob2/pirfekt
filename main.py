from GUI import * 
from Kreis import *

# import canvas  #importiert die "Canvas/zeichenfläche aus canvas.py"

gui = Gui(1280, 720)
gui.reset()

mittelpunkt = False

while gui.is_running():
    highscore = 0
    # print(gui.zeichenklasse.zeichenzustand())
    # gui.handle_events()
    if gui.zeichenklasse.zeichenzustand():
        gui.handle_events()
        gui.update()
        mittelpunkt = False
    else:
        if mittelpunkt == False and len(gui.zeichenklasse.liste) > 5:  #Prüft ob die Punktliste der Zeichnung mindestens mehr als 5 Punkte hat, um falsche Auswertungen zu vermeiden
            print("Auswertung")
            # print(gui.zeichenklasse.liste)
            kreis = Kreis(gui.zeichenklasse.liste)
            # for i in range(int(len(kreis.pixellist)/2)):                          ### aktivieren um die Punkte durch ein X zu kennzeichnen
            #    gui.testmittelpunkt(kreis.pixellist[i*2],kreis.pixellist[i*2+1])   ### aktivieren um die Punkte durch ein X zu kennzeichnen
            kreis.mittelpunkt = kreis.findeMittelpunkt()
            mittelpunkt = kreis.mittelpunkt
            # print(kreis.center)
            gui.testmittelpunkt(kreis.mittelpunkt[0], kreis.mittelpunkt[1])
            kreis.radius = kreis.findeRadius()
            gui.testkreis(kreis.mittelpunkt[0],kreis.mittelpunkt[1],kreis.radius)
            score = kreis.findeScore()
            # print(score)
            gui.showScore(score)
            if score > gui.highscore:
                gui.setHScore(score)
                

            # print(gui.zeichenklasse.liste)
        gui.handle_events()
        gui.update()

        

pygame.quit()




