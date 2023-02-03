#include <iostream>
using namespace std;

int self_number(int n)
{
    int sum = n;
    while(n != 0 )
    {
        sum += n % 10;
        n = n / 10;
    }    
    return sum;
}

int main()
{
    for(int i = 1; i <= 10000; i++)
    {
        int count = 0;
        for(int j = 1; j <= 10000; j++)
        {          
            if(i == self_number(j))
            {
                count++;
            }
        }
        if(count == 0)
        {
            cout << i << "\n";
        }     
    }
    return 0;
}