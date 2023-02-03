#include <iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    
    int max=0;
    double sum=0;
    int arr[N];
    double avg;
    
    for(int i=0; i<N; i++)
    {
        cin>>arr[i];
        
        if(max<arr[i])
        {
            max=arr[i];
        }
        sum=sum+arr[i];
    }
    avg = ( (sum/max) * 100) / N;
    
    cout << fixed;
    cout.precision(6);
    cout<<avg << endl;
  
}