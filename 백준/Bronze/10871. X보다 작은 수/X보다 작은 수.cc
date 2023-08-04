#include <stdio.h>
int main(void){
	int n, x;
	scanf("%d %d", &n, &x);
	int ar[n] = {0, };
	
	for(int i = 0; i<n; i++){
		scanf(" %d", &ar[i]);
		if(ar[i]<x) printf("%d ", ar[i]);
	}
	return 0;
}