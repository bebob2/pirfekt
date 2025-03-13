
class Kreis:
    def __init__(self, pixellist):
        self.center = None
        self.radius = None
        self.score = None
        self.pixellist = pixellist

    def findcenterpoint(self):
        länge = len(self.pixellist)/2
        x_sum = 0
        y_sum = 0
        for i in self.pixellist:
            if self.pixellist[i] % 2:
                x_sum += self.pixellist
            else:
                y_sum += self.pixellist

        x_Mitte = x_sum / länge
        y_Mitte = y_sum / länge
        return x_Mitte, y_Mitte
    
    def findradius(self):
        pass

    def findscore(self):
        pass