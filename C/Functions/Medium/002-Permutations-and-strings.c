#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Algorithm: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

int lexicographic_order(const char* a, const char* b) {
    // Find out the smallest string
    int len_a = strlen(a), len_b = strlen(b);
    
    int len_order;
    const char *smaller;
    if (len_a <= len_b) {
        smaller = a;
        len_order = 1;
    } else {
        smaller = b;
        len_order = 0;
    }
    
    // Compare the strings character by character
    for (int i = 0; i <= strlen(smaller); i++) {
        if (a[i] < b[i]) {
            return 1;
        } else if (b[i] < a[i]) {
            return 0;
        }
    }
    
    // If the strings are equal, none is strictly smaller than the other
    if (len_a == len_b) return 0;
    
    // If the strings are equal so far, return the smallest string
    return len_order;
}

int next_permutation(int n, char **s) {
    int k = -1, l = -1;
    
    // Find k
    for (int i = 0; i < n - 1; i++) {
        if (lexicographic_order(s[i], s[i+1])) {
            k = i;
        }
    }
    if (k == -1) return 0;
    
    // Find l
    for (int i = k+1; i < n; i++) {
        if (lexicographic_order(s[k], s[i])) {
            l = i;
        }
    }
    
    // Swap a[k] and a[l]
    char *temp = s[k];
    
    s[k] = s[l];
    s[l] = temp;
    
    
    // Reverse the string after a[k+1]
    int start = k+1;
    
    // Length of the substring
    int len = (n - start) / 2;
    
    if (len < 1) return 1;
    
    for (int i = 0; i < len; i++) {
        temp = s[start + i];
        
        s[start + i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }
    
    
    return 1;
}

// Locked code
int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}