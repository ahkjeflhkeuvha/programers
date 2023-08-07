#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int n, i;
	scanf("%d", &n);
	
	int* score = (int*)malloc(n * sizeof(int));
	int max = 0;
	double total = 0.0;
	
	for(i = 0; i<n; i++){
		scanf(" %d", &score[i]);
	}
	
	for(i = 0; i<n; i++){
		if(score[i]>max) max=score[i];
	}
	
	for(i = 0; i<n; i++){
		total += (double)score[i]/(double)max*100.0;
	}
	
	printf("%.10f", total/(double)n);
	
	return 0;
}