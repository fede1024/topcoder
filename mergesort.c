#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void mergesort(int *, int, int);
void merge(int *, int, int, int);

int main(int argc, char *argv[]){
    int *vett;
    int len = argc-1;
    int i;

    vett = malloc(sizeof(int)*len);

    for (i = 0; i < len; i++){
        vett[i] = atoi(argv[i+1]);
        printf("%d ", vett[i]);
    }
    printf("\n");

    mergesort(vett, 0, len);

    for (i = 0; i < len; i++)
        printf("%d ", vett[i]);
    printf("\n");

    return 0;
}

void mergesort(int *vett, int start, int end){
    int middle = start + (end-start)/2;

    if (start == end-1) return;

    mergesort(vett, start, middle);
    mergesort(vett, middle, end);
    merge(vett, start, middle, end);
}

void merge(int *vett, int start, int middle, int end){
    int *tmp = malloc(sizeof(int)*(end-start));
    int i = start, j = middle, k=0;

    i = start;

    while(k < (end - start)){
        if(i == middle){
            tmp[k] = vett[j];
            j++;
        }
        else if(j == end){
            tmp[k] = vett[i];
            i++;
        }
        else if(vett[i] < vett[j]){
            tmp[k] = vett[i];
            i++;
        }
        else{
            tmp[k] = vett[j];
            j++;
        }
        k++;
    }

    memcpy(vett+start, tmp, sizeof(int)*(end-start));

    free(tmp);
}

