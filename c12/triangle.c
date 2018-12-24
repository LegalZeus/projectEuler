#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int divisors(int n);

int main(void){
  int target = 500;
  int found = 0;
  for(long int i = 1, triangle = 0;found == 0;i++){
    triangle += i;
    if(divisors(triangle) >= target){
      printf("%ld \n ", triangle);
      found = 1;
    }
  }

}



int divisors(int n){

  int div = 0;

  for(int i = 1;i <= sqrt(n);i++){
    if(n%i == 0){
      if(n/i == i){
	div += 1;
      }else{
	div += 2;
      }
    }
  }
  return div;
}

