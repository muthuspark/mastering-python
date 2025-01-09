class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

class Database:
    def connect(self):
        print("Connecting to database...")

class LoggedDatabase(Database, LoggingMixin):
    def __init__(self):
        super().__init__() # Calls Database's __init__ if needed

    def query(self):
        self.log("Executing query")
        self.connect()

db = LoggedDatabase()
db.query()