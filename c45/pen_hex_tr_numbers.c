#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isTriangular(long int n){
  if(n < 0)
    return false;

  int c = (-2 * n);
  int a = 1, b = 1;
  int d = (b*b) - (4*a*c);

  if(d < 0)
    return false;

  float root1 = (-b + sqrt(d)) / (2*a);
  float root2 = (-b - sqrt(d)) / (2*a);
  if (root1 > 0 && (float)root1 == root1)
    return true;
  if(root2 > 0 && floor(root2) == root2)
    return true;
  return false;
}

bool isPenta(long int n){
  float k = (sqrt(24*n+1)+1)/6;

  if(k == roundf(k))
    return true;
  else
    return false;
}

bool isHexa(long int n){
  float k = (sqrt(8*n +1)+1)/4;

  if (k == roundf(k))
    return true;
  else
    return false;

}

int main(void){
  long int n = 40756;
  while(true){
    if(isTriangular(n) && isPenta(n) && isHexa(n)){
      printf("\n %ld \n", n);
      break;
    }
    n++;
  }
} 
