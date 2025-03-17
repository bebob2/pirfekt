import math

class Kreis:
    '''
    Klasse Kreis: Kreis mit Mittelpunkt, Radius, Punktzahl(Score), und Liste mit den Punkten vom Kreis ([x1;y1:x2;y2]). Diese Liste soll in der main.py Datei aus der GUI Datei übergeben werden.
    '''


    def __init__(self, pixellist):
        self.mittelpunkt = None
        self.radius = None
        self.score = None
        self.pixellist = pixellist

    def findeMittelpunkt(self):
        '''
        Methode von der Klasse Kreis, die den Mittelpunkt bestimmt.
        '''

        
        länge = int(len(self.pixellist))
        # print(länge)
        x_sum = 0
        y_sum = 0
        for i in range(int(länge/2)):
            x_sum +=self.pixellist[i*2]
            y_sum +=self.pixellist[i*2+1]

        x_Mitte = int(x_sum / (länge/2))
        y_Mitte = int(y_sum / (länge/2))
        return x_Mitte, y_Mitte
    
    def findeRadius(self):
        '''
        Methode von der Klasse Kreis, die den Radius bestimmt.
        '''

        länge = int(len(self.pixellist))
        t = 0.0
        for i in range(int(länge/2)):
            t += ((self.mittelpunkt[0] - self.pixellist[i*2])**2+(self.mittelpunkt[1] - self.pixellist[i*2+1])**2)

        r = math.sqrt(t/(länge/2))
        return r


    def findeScore(self):
        '''
        Methode von der Klasse Kreis, die die Punktzahl bestimmt.
        '''

        länge = len(self.pixellist) 
        varianzsumme = 0
        for i in range(int(länge/2)): # In zweierschritten, weil die liste x und y Koordinaten abwechselnd gespeichert
            abstand = math.sqrt(((self.mittelpunkt[0] - self.pixellist[i*2])**2+(self.mittelpunkt[1] - self.pixellist[i*2+1])**2)) #Satz des Pythagoras zur Abstanndsbestimmung
            varianzsumme += abs(abstand - self.radius) # Summe der Abweichungen vom Radius
            
        standartabweichung = varianzsumme / (int(len(self.pixellist) / 2)) # Summe der Abweichungen vom Radius / Anzahl der Punkte in der Liste (x und y Koordinaten abwechselnd speichert)
        prozentuale_abweichung = (standartabweichung / self.radius) * 100
        score = 100 - prozentuale_abweichung # Score = 100 - Prozentuale Abweichung. Ziel: 100 Punkte für einen Perfekten Kreis mit keiner Abweichung zum Radius

        return score
