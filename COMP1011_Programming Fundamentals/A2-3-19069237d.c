// Exercise 05-36 from the textbook:
// Tower of Hanoi puzzle
// (Move n disks from peg A to peg C, using peg B as temporary storage.)
//
#include <stdio.h>
 
void tower_of_Hanoi(int n, char pegFrom, char pegExtra, char pegTo);
 
int main(void)
{
  int n;
  printf("Please input number of disks: ");
  scanf("%d",&n);
  tower_of_Hanoi(n, 'A', 'B', 'C');
}

// Recursively move n disks from pegFrom to pegTo, using pegExtra.
void tower_of_Hanoi(int n, char pegFrom, char pegExtra, char pegTo)
{
  if (n > 0) {                                              //Since direct moves between the leftmost peg and the rightmost peg are not allowed
    tower_of_Hanoi(n-1, pegFrom, pegExtra, pegTo);          
    printf("Move disk #%d: %c --> %c\n", n, pegFrom, pegExtra);   //first step should be from A to B (i.e. pegFrom to pegExtra)
    tower_of_Hanoi(n-1, pegTo, pegExtra, pegFrom);
    printf("Move disk #%d: %c --> %c\n", n, pegExtra, pegTo);     //then from pegExtra to pegTo
    tower_of_Hanoi(n-1, pegFrom, pegExtra, pegTo);                //repeat steps
  }
}