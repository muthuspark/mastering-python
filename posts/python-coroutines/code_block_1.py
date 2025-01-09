def simple_coroutine():
    value = yield
    print(f"Received: {value}")
    value = yield "Coroutine yielded this!"
    print(f"Received: {value}")

coro = simple_coroutine()
next(coro)  # Prime the coroutine – essential before sending values
coro.send("Hello")  # Output: Received: Hello
coro.send("World")  # Output: Received: World
