#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    // Find out the smallest string
    int len_a = strlen(a), len_b = strlen(b);
    
    int len_order;
    const char *smaller;
    if (len_a <= len_b) {
        smaller = a;
        len_order = 0;
    } else {
        smaller = b;
        len_order = 1;
    }
    
    // Compare the strings character by character
    for (int i = 0; i <= strlen(smaller); i++) {
        if (a[i] < b[i]) {
            return 0;
        } else if (b[i] < a[i]) {
            return 1;
        }
    }
    
    // If the strings are equal so far, return the smallest string
    return len_order;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    // Reverse of lexicographic sort
    return 1 - lexicographic_sort(a, b);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    // Cont the number os distinct characters
    int dist_a = 0, dist_b = 0;
    char letters_a[30] = {0}, letters_b[30] = {0};
    
    int index;
    for (int i = 0; i < strlen(a); i++) {
        index = a[i] - 'a';
        if (letters_a[index] == 0) {
            dist_a++;
            letters_a[index]++;
        }
    }
    for (int i = 0; i < strlen(b); i++) {
        index = b[i] - 'a';
        if (letters_b[index] == 0) {
            dist_b++;
            letters_b[index]++;
        }
    }
    
    // The string with the fewer characters should be first 
    if (dist_a < dist_b) {
        return 0;
    } else if (dist_a > dist_b) {
        return 1;
    } else {
        return lexicographic_sort(a, b);
    }
}

int sort_by_length(const char* a, const char* b) {
    // Length of each string
    int len_a = strlen(a), len_b = strlen(b);
    
    // Return the smallest string
    if (len_a < len_b) {
        return 0;
    } else if (len_a > len_b) {
        return 1;
    } else {
        return lexicographic_sort(a, b);
    }
}

void string_sort(char** arr, const int len, int (*cmp_func)(const char* a, const char* b)){
    // Sort by comparing every pair of strings until no further changes are needed
    int order, change;
    for (int n = 0; n < len; n++) {
        change = 0;
        for (int i = 0; i < len-1; i++) {
            order = cmp_func(arr[i], arr[i+1]);
            if (order) {
                char *temp = arr[i+1];
                
                arr[i+1] = arr[i];
                arr[i] = temp;
                
                change = 1;
            }
        }
        
        if (!change) break;
    }
    
    return;
}

