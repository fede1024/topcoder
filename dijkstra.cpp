/*
 * Simple Dijkstra algorithm implementation
 */

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

#define K 6

typedef struct node {
    int n, w;
    struct node *next;
} node;

void add_edge(vector<node*> &, int, int, int);
void dijkstra(vector<node*>, int, vector<int> &);

int main(){
    vector<node*> graph(K, NULL);
    vector<int> dist;

    dist.resize(K);

    add_edge(graph, 0, 5, 14);
    add_edge(graph, 0, 2, 9);
    add_edge(graph, 0, 1, 7);
    add_edge(graph, 1, 2, 10);
    add_edge(graph, 1, 3, 15);
    add_edge(graph, 2, 3, 11);
    add_edge(graph, 5, 2, 2);
    add_edge(graph, 5, 4, 9);
    add_edge(graph, 3, 4, 6);

    cout << "Graph:" << endl;
    for(int i = 0; i < K; i++)
        for(node *tmp = graph[i]; tmp; tmp = tmp->next)
            cout << i << " -> " << tmp->n << " " << tmp->w << endl;

    dijkstra(graph, 0, dist);

    cout << endl << "Distances:" << endl;
    for(int i = 0; i < K; i++)
        cout << i << " " << dist[i] << endl;

    return 0;
}

// Assuming non ordered graph
void add_edge(vector<node*> &graph, int a, int b, int w){
    node *tmp = new node;
    tmp->n = b;
    tmp->w = w;
    tmp->next = graph[a];
    graph[a] = tmp;

    tmp = new node;
    tmp->n = a;
    tmp->w = w;
    tmp->next = graph[b];
    graph[b] = tmp;
}

void dijkstra(vector<node*> graph, int start, vector<int> &dist){
    vector<int> closed(K, 0);
    int closed_num = 0, curr, min;

    dist.assign(K, INT_MAX);
    dist[start] = 0;

    while(closed_num < K){
        min = INT_MAX;
        curr = -1;
        for(int i = 0; i < K; i++)
            if(!closed[i] && dist[i] < min){
                min = dist[i];
                curr = i;
            }

        //cout << "=> " << curr << " " << min << endl;

        for(node *tmp = graph[curr]; tmp; tmp = tmp->next){
            if(closed[tmp->n])
                continue;

            int alt = dist[curr] + tmp->w;

            //cout << " - " << tmp->n << " " << alt<< endl;

            if(alt < dist[tmp->n])
                dist[tmp->n] = alt;
        }

        closed[curr] = 1;
        closed_num++;
    }

}
