#include <iostream>
using namespace std;

int han_number(int N)
{
    if(N < 100)
        return true;
    int a1,a2,a3;
    a3 = N / 100;
    a2 = N % 100 / 10;
    a1 = N % 10;
    
    if(a3-a2 == a2-a1)
        return true;
    else
        return false;
}

int main()
{
    int N;
    int count = 0;
    
    cin >> N;
    for(int i = 1; i<=N; i++)
    {
        if(han_number(i))
        {
            count++;
        }
    }
    cout << count;
}