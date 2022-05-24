#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    
    // Print first half
    int num, min, down_len, const_len;
    for (int i = n; i >= -n; i--) {
        // Skip this two cases
        if (i == 0 || i == -1) continue;
        
        min = abs(i);
        for (num = n; num > min; num--) {
            printf("%d ", num);
        }
      
        const_len = 2 * (min - 1);
        for (int i = 0; i < const_len; i++) {
            printf("%d ", min);
        }
      
        for (num = min; num <= n; num++) {
            printf("%d ", num);
        }
        printf("\n");
    }
    
    return 0;
}