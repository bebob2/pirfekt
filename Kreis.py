
class Kreis:
    def __init__(self, pixellist):
        self.center = None
        self.radius = None
        self.score = None
        self.pixellist = pixellist

    def findcenterpoint(self):
        länge = int(len(self.pixellist))
        x_sum = 0
        y_sum = 0
        for i in range(länge):
            if self.pixellist[i] % 2 == 0:
                x_sum += self.pixellist[i]
            else:
                y_sum += self.pixellist[i]

        x_Mitte = int(x_sum / (länge/2))
        y_Mitte = int(y_sum / (länge/2))
        return x_Mitte, y_Mitte
    
    def findradius(self):
        pass

    def findscore(self):
        pass