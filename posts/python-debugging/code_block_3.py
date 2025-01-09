import logging

logging.basicConfig(filename='my_app.log', level=logging.ERROR)

def my_function():
    try:
        # ... some code ...
        result = 10 / 0  # Potential error
    except ZeroDivisionError:
        logging.exception("ZeroDivisionError occurred") # Logs the error with traceback

my_function()