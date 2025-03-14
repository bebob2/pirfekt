import math

class Kreis:
    def __init__(self, pixellist):
        self.center = None
        self.radius = None
        self.score = None
        self.pixellist = pixellist

    def findcenterpoint(self):
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
    
    def findradius(self):
        länge = int(len(self.pixellist))
        t = 0.0
        for i in range(int(länge/2)):
            t += ((self.center[0] - self.pixellist[i*2])**2+(self.center[1] - self.pixellist[i*2+1])**2)

        r = math.sqrt(t/(länge/2))
        return r

    # def findscore(self):
    #     varianzsumme = 0
    #     for i in self.pixellist:
    #         varianzsumme += abs(i - self.radius)
            
    #     standartabweichung = (varianzsumme / len(self.pixellist))

    #     return standartabweichung

    def findscore(self):
        länge = len(self.pixellist)
        varianzsumme = 0
        for i in range(int(länge/2)):
            abstand = math.sqrt(((self.center[0] - self.pixellist[i*2])**2+(self.center[1] - self.pixellist[i*2+1])**2))
            varianzsumme += abs(abstand - self.radius)
            
        standartabweichung = varianzsumme / (int(len(self.pixellist) / 2))
        prozentuale_abweichung = (standartabweichung / self.radius) * 100
        score = 100 - prozentuale_abweichung

        return score
