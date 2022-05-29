#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void print_num(int n) {
    if (n > 9) {
        if (n % 2 == 0) {
            printf("even");
        } else {
            printf("odd");
        }
        return;
    }
    switch (n) {
        case 1:
            printf("one");
            break;
        case 2:
            printf("two");
            break;
        case 3:
            printf("three");
            break;
        case 4:
            printf("four");
            break;
        case 5:
            printf("five");
            break;
        case 6:
            printf("six");
            break;
        case 7:
            printf("seven");
            break;
        case 8:
            printf("eight");
            break;
        case 9:
            printf("nine");
            break;
        default:
            printf("Greater than 9");
            break;
    }
    return;
}


int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);
    
    for (int i = a; i <= b; i++) {
        print_num(i);
        printf("\n");
    }

    return 0;
}

