#include <stdio.h>
#include <math.h>


int divSum(int n);

int main(void){
  int lim = 28123;
  long int sum = 0;
  for(int n = 0;n < lim;n++){
    
    for(int i = n/2;i < n;i++){
      for(int j = n/2;j < n;j++){
	if(divSum(i) > i && divSum(j) > j){
	  if(i+j == n){
	    sum += 0;
	  }else{
	    sum += n;
	  }
	  printf("%ld \n", sum);
	}
	
      } 
    }
  }
  

  printf("\n\n%ld \n", sum);
}



int divSum(int n){
  int sum = 0;

  for(int i = 1;i < sqrt(n);i++){

    if(n%i == 0 && i != n && n/i != n){
      if(n/i == i){
	sum += i;
      }else{
	sum += (n/i) + i;
      }
    }
  }
  return sum+1;
}
