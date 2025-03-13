from GUI import * 
from Kreis import *

# import canvas  #importiert die "Canvas/zeichenfläche aus canvas.py"

gui = Gui(1280, 720)
gui.reset()

while gui.is_running():
    gui.handle_events()
    gui.update()
    if gui.zeichenklasse.zeichenzustand():
        while gui.zeichenklasse.zeichenzustand():
            gui.handle_events()
            gui.update()
            

        print("Auswertung")
        kreis = Kreis(gui.zeichenklasse.liste)
        kreis.center = kreis.findcenterpoint()
        print(kreis.center)
        #print(gui.zeichenklasse.liste)
        

pygame.quit()




