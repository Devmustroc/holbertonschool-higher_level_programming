#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cursor; /* cursor */
	listint_t *head;  /* head */

	head = list;  /* initialize head */
	cursor = list; /* initialize cursor */
	while (cursor != NULL && cursor->next != NULL)  /* while cursor is not null and cursor->next is not null */
	{
		head = head->next; /* move head to next node */
		cursor = cursor->next->next;   /* move cursor to next node */
		if (head == cursor) /* if head and cursor are equal */
			return (1); /* return 1 */
	}
	return (0); /* return 0 */
}
