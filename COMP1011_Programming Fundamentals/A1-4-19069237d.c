#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {

    // generate a random number for the price
	srand(time(NULL));
	double price;
	price = 0.5 + rand()%20 ;
	printf("The amount that you have to pay: %.2f\n",price);
        
    // let user input the amount of cash inserted
	double cash = 0.00;
	printf("The amount of cash that you will insert: ");
	scanf("%lf",&cash);

    // initialize the variables counting the number of various coins
	unsigned int cent = 0;
	unsigned int one = 0;
	unsigned int two = 0;
	unsigned int five = 0;
	unsigned int ten = 0;

	if (cash < price) {
		puts("The amount paid is not enough");
	}

    // calculate the change one-by-one
	else {
		cash = cash - price;
		while (cash > 0) {
			if (cash >= 10) {
				cash -= 10;
				ten += 1;
			}
			else if (cash >= 5) {
				cash -= 5;
				five += 1;
			}
			else if (cash >= 2) {
				cash -= 2;
				two += 1;
			}
			else if (cash >= 1) {
				cash -= 1;
				one += 1;
			}
			else if (cash >= 0.5) {
				cash -= 0.5;
				cent += 1;
			}
			else {
				continue;
			}
		}

		puts("\nCoins to be returned:\n");
		printf("%-10s%6d\n", "50-cent", cent);
		printf("%-10s%6d\n", "1-dollar", one);
		printf("%-10s%6d\n", "2-dollar", two);
		printf("%-10s%6d\n", "5-dollar", five);
		printf("%-10s%6d\n", "10-dollar", ten);

		return 0;
	}
	
}