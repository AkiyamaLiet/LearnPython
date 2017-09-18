#include <iostream>
#include <iomanip>
using namespace std;

void Magic(int n)
// Create a magic square of size n, n being odd.
{
    int square[10][10];
    int i, j;
    if (!(n%2)) {cout << "n is even" << endl; return;}
    else{
        for ( i=0; i<n; i++) // Initialize square to zero.
            for (int j=0; j<n; j++) square[i][j] = 0;
        square[0][(n-1)/2]=1;  // Middle of first row
        // (i,j) is the current position.
        int j = (n-1)/2, k, l;
        for (int key = 2; key <= n*n; key++){
            // Move up and left. The next two if statements
            // may be replaced by the % operator if -1%n is
            // implemented to have value n-1.
            k = (i) ? (i-1):(n-1);
            l = (j) ? (j-1):(n-1);
            if (square[k][l]) i = (i+1)%n;
            else{ // square[k][l] is empty.
                i = k, j = l;
            }
            square[i][j] = key;
        }
    }
    // Output the magic square.
    for (i=0; i<n; i++){
        for (j=0; j<n; j++) cout << setw(5) << square[i][j];
        cout << endl;
    }
}

int main(){
    Magic(5);
}
