#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

#define INVALID -1

// Calculate square of the area of a triangle
float area(triangle tr) {
    int a = tr.a, b = tr.b, c = tr.c;
    float p = (a + b + c) / 2.0;
    
    return p * (p - a) * (p - b) * (p - c);
}

// Sort the triangles by their area
void sort_by_area(triangle* tr, int n) {
    float all_areas[n];
    triangle sorted_tr[n];
    
    // Calculate the area of all triangles
    for (int i = 0; i < n; i ++) {
        all_areas[i] = area(tr[i]);
    }
    
    float min, tr_area;
    
    int i, index;
    int sorted_index = 0;
    for (i = 0; i < n; i++){
        min = INFINITY;
        
        // Find the smallest area
        for (index = 0; index < n; index++) {
            tr_area = all_areas[index];
            
            if (tr_area > INVALID && tr_area < min) {
                min = tr_area;
            }
        }
        
        // Add the minimum area triangle to a sorted array
        for (index = 0; index < n; index++) {
            if (all_areas[index] == min) {
                all_areas[index] = INVALID;
                
                sorted_tr[sorted_index++] = tr[index];
                break;
            }
        }
    }
    
    // Copy the values on the sorted array to the normal array
    for (i = 0; i < n; i++) {
        tr[i] = sorted_tr[i];
    }
    
    return;
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}