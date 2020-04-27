#include "lists.h"
/**
 * check_cycle - checks if cycle exists
 * @list: singly linked list being checked
 * Return: 0 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *check;

	if (list && list->next)
		check = list->next;
	else
		return (0);

	while (list && check)
	{
                if (list == check)
                        return (1);

                list = list->next;

		if (check->next)
			check = check->next;
		else
			return (0);

		if (check->next)
			check = check->next;
		else
			return (0);
	}
	return (0);
}
