#include <python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - print some list info
 * @p: pyobject pointer
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *node;
	Py_ssize_t idx;

	list = (PyListObject *) p;
	printf("[*] Size of the Python List = %d\n", (int) Py_SIZE(list));
	printf("[*] Allocated = %d\n", (int) list->allocated);

	for (idx = 0; idx < Py_SIZE(list); idx++)
	{
		node = PyList_GetItem(p, idx);
		if (node)
			printf("Element %d: %s\n", idx, node->ob_type->tp_name);
	}
}
