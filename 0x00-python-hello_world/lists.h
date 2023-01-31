#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - Singly linked list
 * @n : integer.
 * @next: points to the next node.
 */
typedef struct listint_s
{
	int n; /* n - integer */
	struct listint_s *next; /* struct listint_s - singly linked list */
} listint_t; /* listint_t - singly linked list */

size_t print_listint(const listint_t *h); /* print_listint - prints all the elements of a listint_t list */
listint_t *add_nodeint(listint_t **head, const int n);  /* add_nodeint - adds a new node at the beginning of a listint_t list */
void free_listint(listint_t *head);  /* free_listint - frees a listint_t list */
int check_cycle(listint_t *list); /* check_cycle - checks if a singly linked list has a cycle in it. */

#endif
