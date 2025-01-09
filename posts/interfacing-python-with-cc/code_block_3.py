from cffi import FFI

ffi = FFI()
ffi.cdef("""
    int add(int a, int b);
""")

lib = ffi.dlopen("./add.so") #Still requires compiled C code

result = lib.add(10, 5)
print(f"The sum is: {result}")
