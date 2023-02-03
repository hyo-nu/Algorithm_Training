#include <iostream>
using namespace std;

int main()
{
    int num;
    int X;
    cin>>num>>X;
    
    int arr[num];
    for(int i = 0; i<num; i++)
    {
        cin>>arr[i];
    }
    for(int j = 0; j<num; j++ )    
    {
        if(arr[j]<X)
        {
            cout<<arr[j]<<" ";
        }
    }
    return 0;
}