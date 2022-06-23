'''
class Vector2D:

    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def show(self):
        print(f"{self.icap}i^+{self.jcap}j^")

class Vector3D(Vector2D):

    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    
    def show(self):
        print(f"{self.icap}i^+{self.jcap}j^+{self.kcap}k^")
    

v1=Vector2D(1,3)
v1.show()

v2=Vector3D(2,4,6)
v2.show()
'''