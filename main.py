from GUI import * 
from Kreis import *

# import canvas  #importiert die "Canvas/zeichenfläche aus canvas.py"

gui = Gui(1280, 720)
gui.reset()

kreis = Kreis(gui.zeichenklasse.liste)

center = False
while gui.is_running():
    # print(gui.zeichenklasse.zeichenzustand())
    # gui.handle_events()
    if gui.zeichenklasse.zeichenzustand():
        gui.handle_events()
        gui.update()
        center = False
    else:
        if center == False :
            print("Auswertung")
            print(gui.zeichenklasse.liste)
            kreis.center = kreis.findcenterpoint()
            center = kreis.center
            print(kreis.center)
            gui.testmittelpunkt(kreis.center[0], kreis.center[1])
            #for i in range(int(len(kreis.pixellist)/2)):
            #    gui.testmittelpunkt(kreis.pixellist[i*2],kreis.pixellist[i*2+1])
            kreis.radius = kreis.findradius()
            gui.testkreis(kreis.center[0],kreis.center[1],kreis.radius)
            #print(gui.zeichenklasse.liste)
            gui.handle_events()
            gui.update()
        gui.handle_events()
        gui.update()

        

pygame.quit()




