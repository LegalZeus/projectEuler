#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isSquare(int n){
  int iVar;
  float fVar;
  fVar = sqrt((double)n);
  iVar = fVar;
  if (iVar == fVar){return true}
  else{return false};
}



int main(void){
  printf("\n\n");
  
  printf(isSquare(25));


}
