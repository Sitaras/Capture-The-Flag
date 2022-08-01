#include <stdio.h>

// finds the 48th multiple of 7 that contains a 7 in its decimal representation

int main() {
    int mul;
    int i=1;
    int count=0;
    for(;;){
        mul=7*i;
        int temp=mul;
        while(temp!=0){
            int digit=temp%10;
            if(digit==7){
                count++;
                break;
            }
            temp/=10;
        }
        if(count==48){
            printf("%d\n",mul);
            break;
        }
        i++;
    }
        
    return 0;
}
