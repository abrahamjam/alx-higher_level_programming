#include "lists.h"

/**
 *check_cycle-linked list contains cycle or not
 *@list:to be checked
 *Return:1 if it has a cycle, 0 if has not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow -> next;
		fast = fast -> next;
		if (slow == fast)
			return (0);
	}
	return (0);
}
