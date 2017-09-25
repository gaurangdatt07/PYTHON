class Floor():
    Tileb = 8
    Tileh = 8
    length = 0
    breadth = 0
    def dim(self):
        self.length = input("Enter the Length of the floor: \n")
        self.breadth = input("Enter the breadth of the floor : \n")

    def Tiles(self):
        total = 0
        total += self.breadth/self.Tileb
        print total
        total +=self.length/self.Tileh 
        print total
        rbreadth = self.breadth%self.Tileb
        
        rlength = self.length%self.Tileh
        total += ( rlength+rbreadth)/self.Tileh
            

        print total

a = Floor()
a.dim()
a.Tiles()
        

            
    
