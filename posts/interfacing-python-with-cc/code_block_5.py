cython mymodule.pyx
gcc -shared -o mymodule.so -fPIC mymodule.c -I/usr/include/python3.x