#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){

  int n = 100;

  int sumsqr = 0;
  for(int i = 1;i <= n;i++){
    sumsqr += pow(i, 2);
  }

  int sqrsum = 0;
  for(int j = 1;j <= n;j++){
    sqrsum += j;
  }
  sqrsum = pow(sqrsum, 2);

  printf("difference : %d\n", sqrsum - sumsqr);
}
