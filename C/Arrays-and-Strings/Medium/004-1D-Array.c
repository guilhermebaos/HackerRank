#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Link: https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=false

int main() {
    int n, num;
    scanf("%d", &n);
    
    int *arr = (int*) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &num);
        arr[i] = num;
    }
    
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    
    printf("%d", total);
       
    return 0;
}