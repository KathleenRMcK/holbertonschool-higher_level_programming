#include "lists.h"
/**
 * insert_node - Inserts new node to singly linked list
 * @head: First node
 * @number: New node
 * Return: NULL on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *helper;
	listint_t *start, *temp;

	start = *head;
	helper = NULL;

	if (head == NULL)
		return (NULL);

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if (start->n > number)
	{
		temp->next = *head;
		*head = temp;
		return (*head);
	}

	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}

	while(start && start->n < number)
	{
		helper = start;
		start = start->next;
	}

	temp->next = start;
	helper->next = temp;
	return (temp);
}
