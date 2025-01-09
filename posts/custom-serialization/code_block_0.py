import json

class MyCustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return json.dumps({'name': self.name, 'value': self.value})

    @staticmethod
    def deserialize(data):
        d = json.loads(data)
        return MyCustomObject(d['name'], d['value'])

obj = MyCustomObject("Example", 123)
serialized_data = obj.serialize()
print(f"Serialized data: {serialized_data}")

deserialized_obj = MyCustomObject.deserialize(serialized_data)
print(f"Deserialized object: {deserialized_obj.name}, {deserialized_obj.value}")
