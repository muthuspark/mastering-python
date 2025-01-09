class Rectangle:
    # ... (previous code) ...

    @width.deleter
    def width(self):
        print("Deleting width...")
        del self._width

rect = Rectangle(5,10)
del rect.width # Output: Deleting width...