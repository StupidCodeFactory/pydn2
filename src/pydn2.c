// idn2module.c
#include <Python.h>
#include <idn2.h>     // libidn2 header
#include <stdlib.h>   // For free()

// Wrapper for idn2_to_ascii.
// Python signature: idn2.to_ascii(input_string, flags=0)
static PyObject* py_idn2_to_ascii(PyObject *self, PyObject *args) {
    const char *input;
    unsigned int flags = 0;

    // Parse the Python arguments: a required string and an optional unsigned int (flags)
    if (!PyArg_ParseTuple(args, "s|I", &input, &flags)) {
        return NULL;  // If parsing fails, return NULL to signal an error.
    }

    char *output = NULL;
    int ret = idn2_to_ascii(input, &output, flags);
    if (ret != IDN2_OK) {
        // If libidn2 reports an error, set a Python RuntimeError.
        PyErr_Format(PyExc_RuntimeError, "idn2_to_ascii failed with error code: %d", ret);
        return NULL;
    }

    // Create a Python Unicode object from the output C string.
    PyObject *result = PyUnicode_FromString(output);

    // Free the memory allocated by libidn2 (which typically uses malloc)
    free(output);

    return result;
}

// Method definitions for the module.
// Each entry maps a Python function name to the corresponding C function.
static PyMethodDef Idn2Methods[] = {
    {"to_ascii", py_idn2_to_ascii, METH_VARARGS,
     "Convert an internationalized domain name to ASCII using libidn2.\n\n"
     "Parameters:\n"
     "  input (str): The domain name to convert.\n"
     "  flags (int, optional): Flags for conversion (default is 0).\n\n"
     "Returns:\n"
     "  str: The ASCII version of the domain name."},
    {NULL, NULL, 0, NULL}  // Sentinel indicating the end of the array.
};

// Module definition.
static struct PyModuleDef idn2module = {
    PyModuleDef_HEAD_INIT,
    "idn2",                     // Module name
    "Python binding for libidn2", // Module documentation
    -1,                         // Size of per-interpreter state of the module (-1 means global state)
    Idn2Methods                 // The methods defined in this module
};

// Module initialization function.
// This function is called when Python imports the module.
PyMODINIT_FUNC PyInit_idn2(void) {
    return PyModule_Create(&idn2module);
}
