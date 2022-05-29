#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int sum = 0;
    
    int digit;
    for (int i = 4; i >= 0; i--) {
        digit = n / ((int) pow(10, i));
        sum += digit;
        n -= digit * pow(10, i);
    }
    
    printf("%d", sum);
    
    return 0;
}