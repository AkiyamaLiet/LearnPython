#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define random() (rand())
using namespace std;

int Prime0(int n, int alpha)
// Returns 1 if n is a prime and 0 otherwise;
// alpha is the probability parameter.
{
    int q = n-1, large=20;  // Specify large.
    for(int i=1; i <= large; i++){
        int m = q, y = 1;
        int a = rand() % q + 1;
        // Choose a random number in the range [1, n-1]
        int z = a;
        // Compute a^n-1 mod n.
        while(m > 0){
            while(m%2 == 0){
                z = (z*z) % n; m /= 2;
            }
            m--; y = (y*z) % n;
        }
        if (y != 1) return(0);
    }
    return(1);
}

int main()
{
    for(int i = 2; i < 50; i++){
        cout << Prime0(i, 6);
        cout<<i<<endl;
    }
}
