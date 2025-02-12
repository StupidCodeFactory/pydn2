#include <Python.h>
#include <idn2.h>
#include <stdlib.h>

static PyObject *py_idn2_to_ascii_8z(PyObject *self, PyObject *args) {
  const char *input;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &input, &flags))
    return NULL;
  char *output = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_to_ascii_8z(input, &output, flags);
  Py_END_ALLOW_THREADS;
  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  PyObject *result = PyUnicode_FromString(output);
  free(output);
  return result;
}

static PyObject *py_idn2_to_unicode_8z8z(PyObject *self, PyObject *args) {
  const char *input;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &input, &flags))
    return NULL;
  char *output = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_to_unicode_8z8z(input, &output, flags);
  Py_END_ALLOW_THREADS;
  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  if (output == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(output);
  free(output);
  return result;
}

static PyObject *py_idn2_register_u8(PyObject *self, PyObject *args) {
  const char *ulabel = NULL;
  const char *alabel = NULL;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "zz|I", &ulabel, &alabel, &flags))
    return NULL;
  char *insertname = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS
  ret = idn2_register_u8((const uint8_t *)ulabel, (const uint8_t *)alabel,
                             (uint8_t **)&insertname, flags);
  Py_END_ALLOW_THREADS;
  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  if (insertname == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(insertname);
  free(insertname);
  return result;
}

static PyObject *py_idn2_to_ascii_lz(PyObject *self, PyObject *args) {
  const char *input;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &input, &flags))
    return NULL;
  char *output = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS
  ret = idn2_to_ascii_lz(input, &output, flags);
  Py_END_ALLOW_THREADS;
  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  if (output == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(output);
  free(output);
  return result;
}

static PyObject *py_idn2_to_unicode_8zlz(PyObject *self, PyObject *args) {
  const char *input;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &input, &flags))
    return NULL;
  char *output = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_to_unicode_8zlz(input, &output, flags);
  Py_END_ALLOW_THREADS;

  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  if (output == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(output);
  free(output);
  return result;
}

static PyObject *py_idn2_to_unicode_lzlz(PyObject *self, PyObject *args) {
  const char *input;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &input, &flags))
    return NULL;
  char *output = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_to_unicode_lzlz(input, &output, flags);
  Py_END_ALLOW_THREADS;

  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "%s: %s", idn2_strerror_name(ret), idn2_strerror(ret));
    return NULL;
  }
  if (output == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(output);
  free(output);
  return result;
}

static PyObject *py_idn2_lookup_ul(PyObject *self, PyObject *args) {
  const char *src;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "s|I", &src, &flags))
    return NULL;
  char *lookupname = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_lookup_ul(src, &lookupname, flags);
  Py_END_ALLOW_THREADS;

  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "idn2_lookup_ul error: %d", ret);
    return NULL;
  }
  if (lookupname == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(lookupname);
  free(lookupname);
  return result;
}

static PyObject *py_idn2_register_ul(PyObject *self, PyObject *args) {
  const char *ulabel = NULL;
  const char *alabel = NULL;
  unsigned int flags = 0;
  if (!PyArg_ParseTuple(args, "zz|I", &ulabel, &alabel, &flags))
    return NULL;
  char *insertname = NULL;
  int ret;
  Py_BEGIN_ALLOW_THREADS;
  ret = idn2_register_ul(ulabel, alabel, &insertname, flags);
  Py_END_ALLOW_THREADS;

  if (ret != IDN2_OK) {
    PyErr_Format(PyExc_RuntimeError, "idn2_register_ul error: %d", ret);
    return NULL;
  }
  if (insertname == NULL)
    Py_RETURN_NONE;
  PyObject *result = PyUnicode_FromString(insertname);
  free(insertname);
  return result;
}

static PyObject *py_idn2_strerror(PyObject *self, PyObject *args) {
  int rc;
  if (!PyArg_ParseTuple(args, "i", &rc))
    return NULL;
  const char *msg = idn2_strerror(rc);
  return PyUnicode_FromString(msg);
}

static PyObject *py_idn2_strerror_name(PyObject *self, PyObject *args) {
  int rc;
  if (!PyArg_ParseTuple(args, "i", &rc))
    return NULL;
  const char *name = idn2_strerror_name(rc);
  return PyUnicode_FromString(name);
}

static PyMethodDef pydn2_methods[] = {
    {"to_ascii_8z", py_idn2_to_ascii_8z, METH_VARARGS, NULL},
    {"to_unicode_lzlz", py_idn2_to_unicode_lzlz, METH_VARARGS, NULL},
    {"to_unicode_8z8z", py_idn2_to_unicode_8z8z, METH_VARARGS, NULL},
    {"register_u8", py_idn2_register_u8, METH_VARARGS, NULL},
    {"to_ascii_lz", py_idn2_to_ascii_lz, METH_VARARGS, NULL},
    {"to_unicode_8zlz", py_idn2_to_unicode_8zlz, METH_VARARGS, NULL},
    {"to_unicode_lzlz", py_idn2_to_unicode_lzlz, METH_VARARGS, NULL},
    {"lookup_ul", py_idn2_lookup_ul, METH_VARARGS, NULL},
    {"register_ul", py_idn2_register_ul, METH_VARARGS, NULL},
    {"strerror", py_idn2_strerror, METH_VARARGS, NULL},
    {"strerror_name", py_idn2_strerror_name, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef pydn2_module = {PyModuleDef_HEAD_INIT, "pydn2._pydn2", NULL,
                                          -1, pydn2_methods};

PyMODINIT_FUNC PyInit__pydn2(void) {
  PyObject *module = PyModule_Create(&pydn2_module);
    if (module == NULL)
        return NULL;

  PyModule_AddIntConstant(module, "IDN2_NFC_INPUT", IDN2_NFC_INPUT);
  PyModule_AddIntConstant(module, "IDN2_ALABEL_ROUNDTRIP", IDN2_ALABEL_ROUNDTRIP);
  PyModule_AddIntConstant(module, "IDN2_TRANSITIONAL", IDN2_TRANSITIONAL);
  PyModule_AddIntConstant(module, "IDN2_NONTRANSITIONAL", IDN2_NONTRANSITIONAL);
  PyModule_AddIntConstant(module, "IDN2_NO_TR46", IDN2_NO_TR46);
  PyModule_AddIntConstant(module, "IDN2_USE_STD3_ASCII_RULES", IDN2_USE_STD3_ASCII_RULES);

  return module;
}
