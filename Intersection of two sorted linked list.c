#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* newNode(int data) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

Node* findIntersection(Node* head1, Node* head2) {
    Node* head = NULL, *curr = NULL;

    while (head1 && head2) {
        if (head1->data < head2->data) {
            head1 = head1->next;
        } else if (head1->data > head2->data) {
            head2 = head2->next;
        } else {
            if (head == NULL) {
                head = newNode(head1->data);
                curr = head;
            } else {
                curr->next = newNode(head1->data);
                curr = curr->next;
            }
            head1 = head1->next;
            head2 = head2->next;
        }
    }
    return head;
}

