#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct Node {
    int data;
    struct Node *left, *right;
} Node;

typedef struct QueueNode {
    Node* node;
    int hd;
    struct QueueNode* next;
} QueueNode;

typedef struct Queue {
    QueueNode *front, *rear;
} Queue;

Node* newNode(int data) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

QueueNode* newQueueNode(Node* node, int hd) {
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->node = node;
    temp->hd = hd;
    temp->next = NULL;
    return temp;
}

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

void enqueue(Queue* q, Node* node, int hd) {
    QueueNode* temp = newQueueNode(node, hd);
    if (!q->rear) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}

QueueNode* dequeue(Queue* q) {
    if (!q->front) return NULL;
    QueueNode* temp = q->front;
    q->front = q->front->next;
    if (!q->front) q->rear = NULL;
    return temp;
}

// Map structure for storing bottom view
typedef struct MapNode {
    int hd;
    int data;
    struct MapNode* next;
} MapNode;

MapNode* head = NULL;

void insertOrUpdate(int hd, int data) {
    MapNode* temp = head;
    while (temp) {
        if (temp->hd == hd) {
            temp->data = data;
            return;
        }
        temp = temp->next;
    }
    MapNode* newNode = (MapNode*)malloc(sizeof(MapNode));
    newNode->hd = hd;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

void bottomView(Node* root) {
    if (!root) return;
    
    Queue* q = createQueue();
    enqueue(q, root, 0);
    
    while (q->front) {
        QueueNode* temp = dequeue(q);
        Node* node = temp->node;
        int hd = temp->hd;
        free(temp);
        
        insertOrUpdate(hd, node->data);
        
        if (node->left) enqueue(q, node->left, hd - 1);
        if (node->right) enqueue(q, node->right, hd + 1);
    }
    
    for (int i = -10; i <= 10; i++) {
        MapNode* temp = head;
        while (temp) {
            if (temp->hd == i) {
                printf("%d ", temp->data);
                break;
            }
            temp = temp->next;
        }
    }
}

int main() {
    Node* root = newNode(20);
    root->left = newNode(8);
    root->right = newNode(22);
    root->left->left = newNode(5);
    root->left->right = newNode(3);
    root->right->left = newNode(4);
    root->right->right = newNode(25);
    root->left->right->left = newNode(10);
    root->left->right->right = newNode(14);

    printf("Bottom View: ");
    bottomView(root);
    return 0;
}

