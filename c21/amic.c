#include <stdio.h>
#include <math.h>

int divSum(int n);

int main(void){
  int lim = 10000;
  long int sum = 0;
  for(int i = 1;i < lim;i++){
    for(int j = 1;j < lim;j++){
      if(divSum(i) == j && divSum(j) == i && i!=j){
	sum += i+j;
	printf("x : %d , y = %d\n\n",i,j);
	printf("sum : %ld \n\n", sum);
      }
    }
  }
  printf("\n\n sum : %ld \n\n", sum/2);
}


int divSum(int n){
  int sum = 0;

  for(int i = 1;i < sqrt(n);i++){
    if(n%i == 0){
      if(n/i == i && n != n/i){
	sum += i;
      }else if(n != i && n != n/i){
	sum += i+(n/i);
      }
    }
  }
  return sum+1;
}
