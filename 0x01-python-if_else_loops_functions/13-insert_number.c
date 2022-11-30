#include "lists.h"
/**
 * insert_node - inserts a sorted number
 * @head: head node
 * @number: to insert
 *
 * Return: address or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = *head;
	listint_t *next = NULL;

	if (!head)
		return (NULL);

	while (list)
	{
		if (number >= list->n && number <= list->next->n)
		{
			next = list->next;
			list->next = new1(number);
			if (!list->next)
				return (NULL);
			list->next->next = next;
			return (list->next);
		}
		if (!list->next)
		{
			list->next = new1(number);
			if (!list->next)
				return (NULL);
			list->next->next = next;
			return (list->next);
		}
		list = list->next;
	}
	return (NULL);
}
/**
 * new1 - creates a new node
 * @n: number to insert into new node
 *
 * Return: pointer to newly allocated node
 */
listint_t *new1(int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->next = NULL;
	new->n = n;
	return (new);
}
