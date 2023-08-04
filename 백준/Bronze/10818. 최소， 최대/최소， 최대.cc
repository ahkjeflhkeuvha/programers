#include <stdio.h>
int main(void){
    int n, min, max;
    scanf("%d", &n);
    
    int ar[n] = {0, };
    for(int i = 0; i<n; i++){
        scanf(" %d", &ar[i]);
        
        if(i == 0){
            min = ar[0];
            max = ar[0];
        }
        
        if(max < ar[i]) max = ar[i];
        else if(min > ar[i]) min = ar[i];
    }
    
    printf("%d %d", min, max);
    return 0;
}