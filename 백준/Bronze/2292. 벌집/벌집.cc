#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int first = 1;
    int last = 1;
    
    for(int i = 0; i < 100000; i++)
    {
        last = 6*i + last;
        if(n >= first && n <= last)
        {
            cout << i+1;
            return 0;
        }         
        first = last + 1;    
    }  
}