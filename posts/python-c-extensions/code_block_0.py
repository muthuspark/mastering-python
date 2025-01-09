#include <Python.h>

static PyObject* add(PyObject *self, PyObject *args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("i", a + b);
}

static PyMethodDef methods[] = {
    {"add", add, METH_VARARGS, "Add two integers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&moduledef);
}