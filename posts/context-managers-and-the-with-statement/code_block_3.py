class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return "Some value"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_type}")
        return False #Do not suppress exceptions


with MyContextManager() as value:
    print(f"Value from context: {value}")
    # raise Exception("Something went wrong!") #Uncomment this line to test exception handling