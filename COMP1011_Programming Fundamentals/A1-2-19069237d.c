#include <stdio.h>

int main(void) {
	int saving = 360000*1.04; // account's balance with interest added in year 1
	int withdraw = 50000; // withdrawn amount in year 1 
	int years = 1; // number of years

	// keep withdrawing until first failed withdrawal occured
	while (saving >= withdraw) {
		// find current balance
		saving = saving - withdraw;

		// calculate balance with interest added in next year
		saving *= 1.04;

		// calculate withdrawn amount in next year
		withdraw *= 1.02;

		years += 1;
	}

	printf("The withdrawal fails in year %d",years);

	return 0;
}