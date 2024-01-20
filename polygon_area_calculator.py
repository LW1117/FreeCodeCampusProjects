class Rectangle:
    
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        if self.width != self.height:
            return (self.width ** 2 + self.height ** 2) ** 0.5
        else:
            return self.width * (2 ** 0.5)
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            row_text = '*' * self.width + '\n'
            return f'{row_text * self.height}'
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, other_shape):
        return int(self.get_area() / other_shape.get_area())
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side
        super().set_height(side)
        super().set_width(side)
    
    def set_width(self, side):
        self.set_side( side)

    def set_height(self, side):
        self.set_side( side)

    def __str__(self):
        return f'Square(side={self.side})'

rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))


sq.set_width(4)
rect.set_width(7)
rect.set_height(3)
rect.get_picture()
print(sq)
print(rect)
