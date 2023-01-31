#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all the elements of a listint_t list
 * @h: pointer to the start of the list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h) /* print_listint - prints all the elements of a listint_t list */
{
	const listint_t *current; /* current node */
	unsigned int n; /* number of nodes */

	current = h; /* initialize current */
	n = 0; /* initialize n */
	while (current != NULL) /* while current is not null */
	{
		printf("%i\n", current->n); /* print current->n */
		current = current->next; /* move current to next node */
		n++; /* increment n */
	}

	return (n); /* return n */
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer to the start of the list
 * @n: integer to be added to the new node
 * Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)  /* add_nodeint - adds a new node at the beginning of a listint_t list */
{
	listint_t *new; /* new node */

	new = malloc(sizeof(listint_t)); /* allocate memory for new node */
	if (new == NULL) /* if new is null */
		return (NULL); /* return null */

	new->n = n; /* set new->n to n */
	new->next = *head; /* set new->next to head */
	*head = new;  /* set head to new */

	return (new);  /* return new */
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to a pointer to the start of the list
 * @n: integer to be added to the new node
 * Return: address of the new element, or NULL if it failed
 */
void free_listint(listint_t *head)  /* free_listint - frees a listint_t list */
{
	listint_t *current;  /* current node */

	while (head != NULL)  /* while head is not null */
	{
		current = head;  /* set current to head */
		head = head->next;  /* set head to head->next */
		free(current);  /* free current */
	}
}