#include <iostream>
using namespace std;

int main()
{
    int count=0;
    int max=0;
    int arr[9];
    
    for(int i=0; i<9; i++)
    {       
        cin>>arr[i];
        
        if(max<=arr[i])
        {
            max=arr[i];
            count=i;
        }
    }
    cout<<max<<endl<<count+1;

    return 0;
}
