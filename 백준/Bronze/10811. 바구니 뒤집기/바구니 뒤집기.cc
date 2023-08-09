#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int n, m;
	scanf("%d %d", &n, &m);
	
	int ar[101] = {0, };
	int i;
	for(i = 0; i<n; i++){
		ar[i] = i+1;
	}
	
	int a, b;
	int j, k = 0, temp;
	
	for(i = 0; i<m; i++){
		scanf(" %d %d", &a, &b);
		
		for(j = a-1; j<b; j++){
			temp = ar[j];
			ar[j] = ar[b-1];
			ar[b-1] = temp;
			b--;
		}
	}
	
	for(i = 0; i<n; i++){
		printf("%d ",ar[i]);
	}
	
	return 0;
}