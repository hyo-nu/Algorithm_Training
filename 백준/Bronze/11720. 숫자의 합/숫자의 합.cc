#include <iostream>
using namespace std;

int main()
{
    int num;
    cin>>num;
    int sum=0;
    
    for(int i=0; i<num; i++)
    {
        char arr[i];
        cin>>arr[i];
        sum+=(int)arr[i]-48;
    }
    cout << sum;
    return 0;
}