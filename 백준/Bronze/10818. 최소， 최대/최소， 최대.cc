#include <iostream>
using namespace std;

int main()
{
    int N;
    int max, min;
    cin>>N;
    int arr[N];
    
    for(int i = 0; i<N; i++)
    {
        cin>>arr[i];   
    }
    max=arr[0];
    min=arr[0];
    
    for(int j = 1; j<N; j++)
    {
        if(max < arr[j])
        {
            max=arr[j];
        }
        if(min > arr[j])
        {
            min=arr[j];
        }
    }
    cout<<min<<" "<<max;
    return 0;
}