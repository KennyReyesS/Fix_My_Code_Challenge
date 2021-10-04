#!/usr/bin/python3
"""
square.py module
"""


class Square():
    """ Return area of square, permiter, str """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ constructor for my square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiterofmysquare(self):
        """ Permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return string """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterofmysquare())
