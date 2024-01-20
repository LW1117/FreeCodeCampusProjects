class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width():
        pass

    def set_height():
        pass

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            row_text = '*' * self.width
            col_text = (f'*{" " * (self.width - 2)}*\n') * (self.height - 2)
            return f'{row_text}\n{col_text}{row_text}'
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, other_shape):
        return other_shape.get_area() / self.get_area()
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square:
    pass

shape1 = Rectangle(5,5)
shape2 = Rectangle(10,10)
print(shape2.get_picture())