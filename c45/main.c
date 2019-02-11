#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool isTriangular(long int n){
  long int c = (-2 * n);
  long int b = 1;
  long int a = 1;
  long int d = (b * b) - (4 * a * c);

  if (d < 0)
    return false;

  float root1 = (-b + (float)sqrt(d)) / (2 * a);
  float root2 = ( -b - (float)sqrt(d)) / (2 * a); 

  if(root1 > 0 && floor(root1) == root1)
    return true;
  if(root2 > 0 && floor(root2) == root2)
    return true;

  return false;
}

bool isPenta(long int n){
  double s = (1 + sqrt(24 * n + 1)) / 6;
  return (s - floor(s)) == 0;
}

bool isHexa(long int n){
  double s = (sqrt(8 * n + 1)+1) / 4;
  return (s - floor(s) == 0); 
}

int main(void){
  
  long int n = 40755;  
          

  while (1){
    n++;
    if(isTriangular(n) == true && isPenta(n) == true && isHexa(n) == true){
      printf("\n\n%ld\n\n", n);
      break;
    }
  }


}























//