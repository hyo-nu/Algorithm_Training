#include <iostream>
using namespace std;

int main(void)
{
    double A,B;
    
    while(1)
    {
        cin>>A>>B;
        if(A>0 && B<10 && B!=0)
            break;
        else
            continue;
    }
    cout.precision(15);
    cout<<A/B;
    return 0;
}