#include "lists.h"

int check_cycle(listint_t *list)
{
	int noPsycho = 0;
	listint_t *ndege, *kalessa;

	ndege = list;
	kalessa = list;

	while (ndege && kalessa)
	{
		ndege = ndege->next->next;
		kalessa = kalessa->next;
		if (ndege == kalessa)
		{	noPsycho = 1;
			break;
		}
	}
	if(!noPsycho)
		return (0);
	return (1);
}
