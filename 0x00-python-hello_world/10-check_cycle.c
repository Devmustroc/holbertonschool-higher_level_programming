#include "lists.h"

/**
 * check_cycle - fucntion that check if a S LinkedList has a cycle in it.
 * @list: pointer to the beginning of the node.
 * Return: 0 if no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *cursor;
	listint_t *head;

	head = list;
	cursor = list;
	while (cursor != NULL && cursor->next != NULL)
	{
		head = head->next;
		cursor = cursor->next->next;
		if (head == cursor)
			return (1);
	}
	return (1);
}
