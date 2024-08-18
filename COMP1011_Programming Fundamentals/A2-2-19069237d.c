#include <stdio.h>
#include <math.h>

int checkDigit(int num);
int getNthDigit(int num, int n);

int main(){
    int number = 1;
    int sum = 0;
    int x = 0;
    int result = 0;
    
    while (sum < 1000){
        sum += number;
        if ((sum>99)&&(sum < 1000)){                 // 3-digit numbers should be smaller than 1000
            result = checkDigit(sum);
            if (result == 1){
                x = number;
                printf("x = %d\n",x);
                printf("sum: %d\n\n",sum);
            }
        }
        number += 1;        
    }
    printf("x should be: %d",x);
}

int checkDigit(int num){
    int digit[4] = {0};         // initialize an array to store each digit of the sum
    int count = 0;              // initialize a variable to check whether all digits are identical
    
    for (int i = 1; i < 4; i++){
        digit[i] = getNthDigit(num,i);
    }
    
    for (size_t j = 1; j <4; j++){
        if (digit[j] == digit[j+1]){
            return 0;
            break;
        }
        else{
            count += 1;
        }
    }
    
    if (count == 3){     // if all 3 digits are not equal
        return 1;
    }
    
}

int getNthDigit(int num, int n) {                          // function from Tutorial Ch.5 Part 2
	int removedBottomDigits = num / pow(10.0, n - 1); 
	return removedBottomDigits % 10; 
} 


