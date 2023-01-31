#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to a pointer to the start of the list
 * @number: integer to be added to the new node
 * Return: address of the new element, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)  /* insert_node - inserts a number into a sorted list */
{
    listint_t *new = NULL;  /* new node */
	listint_t *prev = NULL;  /* previous node */

	new = malloc(sizeof(listint_t)); /* allocate memory for new node */
	if (new == NULL)  /* if new is null */
		return (NULL); /* return null */

	if (new) /* if new is not null */
	{
		new->n = number; /* set new->n to number */
		new->next = *head; /* set new->next to head */
		if (new->next == NULL || new->n <= (*head)->n) /* if new->next is null or new->n is less than or equal to head->n */
			*head = new; /* set head to new */
		while(new->next && new->n > new->next->n) /* while new->next is not null and new->n is greater than new->next->n */
		{
			prev = new->next; /* set prev to new->next */
			new->next = prev->next; /* set new->next to prev->next */
		}
		if (prev) /* if prev is not null */
			prev->next = new; /* set prev->next to new */
	}

	return (new); /* return new */
}