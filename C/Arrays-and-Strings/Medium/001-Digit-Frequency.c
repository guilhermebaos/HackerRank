#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX 1001

int main() {
    char num[MAX];
    
    fgets(num, MAX, stdin);
    int len = strlen(num);
    
    int freq[10] = {0};
    for (int i = 0; i < len; i++) {
        char ch = num[i];
        if ('0' <= ch && ch <= '9') {
            freq[ch - '0']++;
        }
    }
    
    for (int i = 0; i < 10; i++) {
        printf("%d ", freq[i]);
    }

    return 0;
}
