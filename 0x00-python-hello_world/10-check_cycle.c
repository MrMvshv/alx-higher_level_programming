#include "lists.h"
/**
 * check_cycle - checks if list loops (has cycle)
 * @list: list to check
 *
 * ndege goes faster, will overlap if loops
 * Return: 1 if it loops, else nun
 */
int check_cycle(listint_t *list)
{
	listint_t *ndege, *kalessa;

	ndege = list;
	kalessa = list;

	while (ndege && kalessa)
	{
		ndege = ndege->next->next;
		if (ndege == NULL)
			return (0);
		kalessa = kalessa->next;

		if (ndege == kalessa)
			return (1);
	}
	return (0);
}
