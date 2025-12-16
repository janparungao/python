import math

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
       
    @property
    def width(self):
        return self._width
    
    def set_width(self, new_width):
        if not isinstance(new_width, (float, int)):
            raise TypeError("'Width must be a integer or float'")
        self._width = new_width
        
    @property
    def height(self):
        return self._height
     
    def set_height(self, new_height):
        if not isinstance(new_height, (float, int)):
            raise TypeError("'Height must be a integer or float'")
        self._height = new_height
        
    def __str__(self):
            return f"Rectangle(width={self.width}, height={self.height})"
        
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = math.sqrt(self.width**2 + self.height**2)
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for _ in range(int(self.height)):
            result += ("*" * self.width) + "\n"
        return result
    
    def get_amount_inside(self):
        pass
            
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._side = side
        
    @property
    def side(self):
        return self._side
    
    def set_width(self, new_side):
        if not isinstance(new_side, (float, int)):
            raise TypeError("'Width must be a integer or float'")
        self._width = new_side
        
    def set_height(self, new_side):
        if not isinstance(new_side, (float, int)):
            raise TypeError("'Width must be a integer or float'")
        self._height = new_side
        
    def set_side(self, new_side):
        self._height = new_side
        self._width = new_side
    
    def __str__(self):
        return f"Square(side={self.side})"       
            
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))