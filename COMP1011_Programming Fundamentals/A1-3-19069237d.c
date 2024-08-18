#include <stdio.h>

int main(void) {
	unsigned int days = 0; // total number of days
	unsigned int start = 0; // starting day
	unsigned int count = 0; // 'grids' of calendar

	printf("%s","Please input the number of days: ");
	scanf("%d",&days);

	printf("%s", "Please input the starting day (1 = Monday, 2 = Tuesday, ..., 7 = Sunday): ");
	scanf("%d",&start);

	count += start-1; // not include the starting day

	puts("Mo Tu We Th Fr Sa Su");

	for (unsigned int i = 1; i <= days+start-1; ++i) {

		// print the blank grid
		if (i < start) {
			printf("   ");
			continue;
		}

		// start to print the days
		printf("%2d ", i-start+1);

		// count the number of grids
		count += 1;

		// start a new line when there are 7 grids on a line (= 1 week)
		if (count % 7 == 0) {
			puts("\n");
		}
	}
	return 0;
}