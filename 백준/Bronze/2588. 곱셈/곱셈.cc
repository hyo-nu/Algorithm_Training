#include <iostream>
using namespace std;

int main(void)
{
    int a,b;
    int c,d,e;
    int result;
    cin>>a>>b;
    
    c=a*(b%10);
    d=a*((b/10)%10);
    e=a*(b/100);
    result=a*b;
    
    cout<<c<<endl;
    cout<<d<<endl;
    cout<<e<<endl;
    cout<<result<<endl;
    
    return 0;
}
   
   
    
    
    
   
    