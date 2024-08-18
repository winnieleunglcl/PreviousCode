#include <stdio.h>
#define SIZE 5

void print_best_buy_and_sell(float history[], size_t nr_of_days);

int main(){
    float historicalPrices[SIZE] = {10, 11.11, 7, 10, 6.50};   // initialize an array to store historical daily prices
    
    printf("Historical daily prices: ");
    for (size_t i=0; i<SIZE; i++){
        printf("%.2f ",historicalPrices[i]);
    }
    printf("\n");
    
    print_best_buy_and_sell(historicalPrices, SIZE);
}

void print_best_buy_and_sell(float history[], size_t nr_of_days){
    float max = 0.0;      // maximum profit
    int buyDay = 0;       
    
    for (size_t i=0; i<SIZE; i++){
        float profit = history[i+1] - history[i];    // calculate profit
        if ((max < profit) && (profit > 0)){         // compare the profit with the previous maximum profit
            max = profit;
            buyDay = i;
        }
    }
    if (max == 0){
        printf("Buy day 0; sell day 0");            // if no positive profit is possible, let the buy day and the sell day both be 0
    }
    else{
        printf("Buy day %d; sell day %d",buyDay,buyDay+1);
    }
}
