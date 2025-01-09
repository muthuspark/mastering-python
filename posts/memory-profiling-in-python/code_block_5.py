import objgraph

class MyClass:
    pass

def create_objects():
    objects = []
    for i in range(1000):
        objects.append(MyClass())
    return objects

objects = create_objects()
objgraph.show_refs([objects[0]], filename='object_graph.png')