#include "lists.h"
#include <stddef.h>
#include <stdio.h>
/**
 * is_palindrome - checks if sllist is a palindrome
 * @head: adress of first node
 * palindrome is to boob as C is to i
 *
 * Return: 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *a, *z, *p = NULL;
	int j = 0, k, m, e;

	a = *head;
	if (!a)
		return (1);
	z = a;
	p = z;
	while (z->next != NULL)
	{
		z = z->next;
		j++;
	}
	j++;
	if (j % 2 == 0)
		k = j / 2;
	else
		k = (j / 2) + 1;
	e = k;
	while (e > 0 && p->next != NULL)
	{
		p = p->next;
		e--;
	}
	if (j % 2)
		k--;
	while (k > 0)
	{	k--;
		z = p;
		m = k;
		while (m > 0)
		{	z = z->next;
			m--;
		}
		printf("comparin: %d, %d\n", z->n, a->n);
		if (z->n != a->n)
			return (0);
		a = a->next;
	}
	return (1);
}
