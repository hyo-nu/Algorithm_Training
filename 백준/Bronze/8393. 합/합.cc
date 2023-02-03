#include <iostream>
using namespace std;

int main()
{
    int n;
    int result=0;
    cin >> n;
    
    if(n >= 1 && n <= 10000)
    {
        for(int i=1; i<=n; i++)
            result += i;
    }
    cout << result;
}