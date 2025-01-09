class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def serialize(self):
        return json.dumps({'x': self.x, 'y': self.y})

    @staticmethod
    def deserialize(data):
        d = json.loads(data)
        return Point(d['x'], d['y'])


class Shape:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def serialize(self):
        return json.dumps({'name': self.name, 'points': [p.serialize() for p in self.points]})

    @staticmethod
    def deserialize(data):
        d = json.loads(data)
        points = [Point.deserialize(p) for p in d['points']]
        return Shape(d['name'], points)

p1 = Point(1,2)
p2 = Point(3,4)
shape = Shape("Rectangle", [p1, p2])
serialized_shape = shape.serialize()
print(serialized_shape)
deserialized_shape = Shape.deserialize(serialized_shape)
print(deserialized_shape.name, [p.x for p in deserialized_shape.points])