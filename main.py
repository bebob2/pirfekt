from GUI import * 
from Kreis import *

# import canvas  #importiert die "Canvas/zeichenfläche aus canvas.py"

gui = Gui(1280, 720)
gui.reset()

while gui.is_running():
    gui.handle_events()
    if gui.zeichenklasse.zeichenzustand():
        while gui.zeichenklasse.zeichenzustand():
            gui.handle_events()
            gui.update()
            

        print("Auswertung")
        print(gui.zeichenklasse.liste)
        kreis = Kreis(gui.zeichenklasse.liste)
        kreis.center = kreis.findcenterpoint()
        print(kreis.center)
        gui.testmittelpunkt(kreis.center[0], kreis.center[1])
        #for i in range(int(len(kreis.pixellist)/2)):
        #    gui.testmittelpunkt(kreis.pixellist[i*2],kreis.pixellist[i*2+1])
        kreis.radius = kreis.findradius()
        gui.testkreis(kreis.center[0],kreis.center[1],kreis.radius)
        #print(gui.zeichenklasse.liste)
        

pygame.quit()




