#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int m, n, i, j;

    scanf("%d %d", &m, &n);
    
    int arr[101] = {0, };
    
    int a, b, c;

    for(i = 0; i<n; i++){
         scanf("%d %d %d", &a, &b, &c);
        for(j = a; j<=b; j++){
            arr[j] = c;
        }
    }
    
    for(i = 1; i<=m; i++){
        printf("%d ", arr[i]);
    }
    
    
    return 0;
}