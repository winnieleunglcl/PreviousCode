#include <stdio.h>
#include <stdlib.h>
#define SIZE 4

struct date{
    char day[3];
    char month[3];
    char year[5];
};

typedef struct date Date;

void bubbleSort(double *sumArray, int *const resultArray); //function prototype

int main(void){
    Date dates[SIZE];
    double Day[SIZE];      //create arrays for comparing dates
    double Month[SIZE];    //by multiplying month and year with a specific number
    double Year[SIZE];     //and getting the sum of them and the day
    double sum[SIZE];
    int result[SIZE] = {0,1,2,3};  //create an array to store the order
    
    printf("Please input four dates in the format dd/mm/yyyy:\n");
    for (size_t i=0; i<4; i++){
        scanf("%2s/%2s/%4s",dates[i].day,dates[i].month,dates[i].year);
        
        char *d1Ptr;
        Day[i] = strtod(dates[i].day,&d1Ptr);
        Month[i] = strtod(dates[i].month,&d1Ptr)*31;  //1 month has 31 days at most
        Year[i] = strtod(dates[i].year,&d1Ptr)*372;   //1 year has 12*31 = 372 days at most (though not realistic)
    }
    
    for (size_t i=0; i<SIZE; i++){
        sum[i] = Day[i]+Month[i]+Year[i];  //store the 'sum value' of each date in the array
    }
    
    for (unsigned int pass=1; pass<SIZE; pass++){
        for (size_t j=0; j<SIZE-1; j++){
           if (sum[j]>sum[j+1]){
               bubbleSort(sum,result);  //sort the 'sum value' of each date by bubbleSort, update the order accordingly
           }
        }
    }
    
    puts("\nDates in chronological order from the earliest to the latest:");
    for (size_t i=0; i<SIZE; i++){
        printf("%2s/%2s/%4s\n",dates[result[i]].day,dates[result[i]].month,dates[result[i]].year);  //print result with the order
    }
    
    return 0;
}

void bubbleSort(double * sumArray, int * resultArray){
    void swap1(double *element1Ptr, double *element2Ptr);  //since 2 arrays have different data types
    void swap2(int *element1Ptr, int *element2Ptr);        //2 swap functions are needed
    for (unsigned int pass=1; pass<SIZE; pass++){
        for (size_t j=0; j<SIZE-1; j++){
           if (sumArray[j]>sumArray[j+1]){                 //compare 'sum values'
               swap1(&sumArray[j],&sumArray[j+1]);
               swap2(&resultArray[j],&resultArray[j+1]);
           }
        }
    }
}

void swap1(double *element1Ptr, double *element2Ptr){
    double hold = *element1Ptr;
    *element1Ptr = *element2Ptr;
    *element2Ptr = hold;
}
void swap2(int *element1Ptr, int *element2Ptr){
    int hold = *element1Ptr;
    *element1Ptr = *element2Ptr;
    *element2Ptr = hold;
}