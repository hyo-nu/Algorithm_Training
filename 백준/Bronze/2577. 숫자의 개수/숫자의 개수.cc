#include <iostream>
using namespace std;

int main()
{
    int a,b,c;
    int arr[10]={0,};
    cin >> a >> b >> c;   
    
    int multi = a*b*c;
    while(multi > 0)
    {
        arr[multi % 10]++;
        multi = multi / 10;
    }
    
    for(int i = 0; i < 10; i++)
    {
        cout << arr[i] << endl;
    }
    return 0;  
}