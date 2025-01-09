class PrintableMixin:
    def print_data(self):
        print(f"Data: {self.__dict__}")

class LoggedPrintableDatabase(Database, LoggingMixin, PrintableMixin):
    pass

logged_db = LoggedPrintableDatabase()
logged_db.connect()
logged_db.log("Connected!")
logged_db.print_data()