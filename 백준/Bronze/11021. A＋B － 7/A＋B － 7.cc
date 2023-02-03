#include <iostream>
using namespace std;

int main()
{
    int test;
    cin>>test;
    
    for(int i =1; i<=test; i++)
    {
        int a,b;
        cin>>a>>b;
        cout<<"Case #"<<i<<": "<<a+b<<endl;
    }
    return 0;
}