#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX 101

int read_line(char* string) {
    char input = 'A';
    int i = 0;
    while (input >= 1) {
        input = getchar();
        string[i++] = input;
    }
    
    return i;
}

int main() {
    char ch;
    char word[MAX];
    char string[MAX];
    
    scanf("%c", &ch);
    scanf("%s", &word);
    int len = read_line(string);
    
    printf("%c", ch);
    printf("\n%s", word);
    for (int i = 0; i < len - 1; i++) {
        printf("%c", string[i]);
    }
    return 0;
}
