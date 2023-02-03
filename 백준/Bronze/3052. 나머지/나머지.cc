#include <iostream>
using namespace std;

int main()
{
    int arr[10];
    int rest[42] = {0,}; 
    int sum = 0;     
    
    for(int i = 0; i <10; i++)
    {
        cin >> arr[i];
        rest[arr[i] % 42] = 1;      
    }
    
    for(int i = 0; i < 42; i++)
    {
        sum += rest[i];
    }
    cout << sum;     
}