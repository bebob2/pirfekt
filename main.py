from GUI import * 
from Kreis import *

# import canvas  #importiert die "Canvas/zeichenfläche aus canvas.py"

gui = Gui(1280, 720)
gui.reset()

center = False

while gui.is_running():
    highscore = 0
    # print(gui.zeichenklasse.zeichenzustand())
    # gui.handle_events()
    if gui.zeichenklasse.zeichenzustand():
        gui.handle_events()
        gui.update()
        center = False
    else:
        if center == False and len(gui.zeichenklasse.liste) > 3:
            print("Auswertung")
            # print(gui.zeichenklasse.liste)
            kreis = Kreis(gui.zeichenklasse.liste)
            # for i in range(int(len(kreis.pixellist)/2)):                          ###
            #    gui.testmittelpunkt(kreis.pixellist[i*2],kreis.pixellist[i*2+1])   ###
            kreis.center = kreis.findcenterpoint()
            center = kreis.center
            # print(kreis.center)
            gui.testmittelpunkt(kreis.center[0], kreis.center[1])
            kreis.radius = kreis.findradius()
            gui.testkreis(kreis.center[0],kreis.center[1],kreis.radius)
            score = kreis.findscore()
            # print(score)
            gui.showScore(score)
            if score > gui.highscore:
                gui.setHScore(score)
                

            # print(gui.zeichenklasse.liste)
        gui.handle_events()
        gui.update()

        

pygame.quit()




