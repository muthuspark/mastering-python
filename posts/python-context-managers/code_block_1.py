class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Optionally handle exceptions here:
        # if exc_type is not None:
        #     print(f"Exception occurred: {exc_type}")
        #     return True # Suppress exception


with FileManager('my_file.txt', 'w') as f:
    f.write("Hello, context managers!")