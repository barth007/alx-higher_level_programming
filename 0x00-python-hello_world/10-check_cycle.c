#include "lists.h"
/**
 *check_cycle - checks for loop in a list
 *@list: the list to check
 *Return: 1 if true and 0 if false
**/
int check_cycle(listint_t *list)
{
	/**
	*HashMap *map;

	*if (list != NULL)
		*return (0);
	*map = malloc(sizeof(HashMap));
	*if (!map)
		*return (0);
	*while (list != NULL)
	*{
		*if (list->next == map->buckets)
			*return (1);
		*map += list;
		*list = list->next;

	*}
	*return (0);
	**/

	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != slow)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
