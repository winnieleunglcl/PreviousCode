// Fig. 10.7: fig10_07.c
// Displaying an unsigned int in bits
#include <stdio.h>

void displayBitsAsCharacter(unsigned int value, char fillCharacter); // prototype

int main(void)
{ 
  unsigned int graphix [] = {529002622 , 12589153 , 12595297 , 260071521 , 12632161 , 12681313 , 528678974};
  size_t nr_of_rows = sizeof(graphix) / sizeof(graphix[0]);
  size_t i;
  for ( i = 0; i < nr_of_rows ; i ++) {
      displayBitsAsCharacter (graphix[i],'X');
  }
} 

// display bits of an unsigned int value
void displayBitsAsCharacter(unsigned int value, char fillCharacter)
{ 
   // define displayMask and left shift 31 bits
   unsigned int displayMask = 1 << 31; 

   // loop through bits 
   for (unsigned int c = 1; c <= 32; ++c) { 
      putchar(value & displayMask ? fillCharacter : ' ');
      value <<= 1; // shift value left by 1      

   } 

   putchar('\n');
} 
