import math
class GeoLocation():
    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z

    def dist (self,other_location : 'GeoLocation')->float:
        dx = self.x-other_location.x
        dy = self.y-other_location.y
        dz = self.z-other_location.z
        ddx = pow(dx,2)
        ddy = pow(dy,2)
        ddz = pow(dz,2)
        answer = math.sqrt(ddx++ddy+ddz)
        return  answer

    def __repr__(self)->str:
        return "{},{},{}".format(self.x,self.y,self.z)







