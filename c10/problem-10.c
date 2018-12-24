#include <stdio.h>
#include <stdlib.h>


int isPrime(long long int n);

int main(void){
  long long int n = 2000000;
  long long int sum = 0;

  for(long long int i = 2;i < n;i++){

    if(isPrime(i) == 1){
      sum += i;
      printf("sum : %lld \n", sum);
    }
  }
}







int isPrime(long long int n){
  if(n <= 1) return 0;
  if(n <= 3) return 1;

  if(n%2 == 0 || n%3 == 0) return 0;

  for(int i = 5;i*i<= n;i+=6){
    if(n%i == 0 || n%(i+2) == 0){
      return 0;
    }
  }

  return 1;
}
