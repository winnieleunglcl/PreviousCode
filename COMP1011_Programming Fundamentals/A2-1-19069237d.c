#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int decideMove(int random);

int main()
{
    //seed the random number generator with the current time
    srand(time(NULL));
    
    int step = 1;
    printf("The robot starts on step %d.\n\n",step);
    
    while ((step > 0) && (step < 12)){
        int r = 1 + rand()%100;               // generate a random number (i.e. probability)
        int result = decideMove(r);           // call a function to decide whether the robot moves up or down, or falls off
        
        if (result == 1){
            step += 1;
            puts("The robot moves up one step.");
        }
        else if (result == 0){
            step -= 1;
            puts("The robot moves down one step.");
        }
        else{
            step = 0;
            puts("The robot falls off.");
            break;
        }
        printf("Robot’s current location: %d\n\n",step);
    }
    
    if (step == 0){
        puts("FAILURE");
    }
    else{
        puts("SUCCESS");
    }
    
}

int decideMove(int random){
    if (random <= 80){          // probability 0.80 (80/100)
        return 1;
    }
    else if (random <= 97){    // probability 0.17 (17/100)
        return 0; 
    }
    else{
        return 2;              // probability 0.03 (3/100)
    }
}