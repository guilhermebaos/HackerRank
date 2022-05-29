#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    int max_and = 0, max_or = 0, max_xor = 0;
    
    int and, or, xor;
    for (int a = 1; a < n; a++) {
        for (int b = a + 1; b <= n; b++) {
            and = a & b;
            or = a | b;
            xor = a ^ b;
            
            if (and > max_and && and < k) {
                max_and = and;
            }
            if (or > max_or && or < k) {
                max_or = or;
            }
            if (xor > max_xor && xor < k) {
                max_xor = xor;
            }
            
        }
    }
    
    printf("%d\n%d\n%d", max_and, max_or, max_xor);
    
    return;
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
