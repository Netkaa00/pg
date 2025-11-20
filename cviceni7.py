
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def secti(self, jiny_vector):
        x = self.x + jiny_vector.x
        y = self.y + jiny_vector.y
        return Vector(x, y)
    
    def vynasob(self, skalar):
        x = self.x * skalar
        y = self.y * skalar
        return Vector(x, y)        

if __name__ == "__main__":
    v1 = Vector(5, 6)
    v2 = Vector(10, 15)

    v3 = v1.secti(v2)

    v4 = v1.vynasob(2)
    print(v3)  
    print(v4)  