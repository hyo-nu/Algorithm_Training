#include <iostream>
using namespace std;

int main(void)
{
    int num;
    cin>>num;
    
    if(num>=0 && num<=100)
    {
        if(num>=90 && num<=100)
        {
            cout<<"A";
        }
        else if(num>=80 && num<=89)
        {
            cout<<"B";
        }
        else if(num>=70 && num<=79)
        {
            cout<<"C";
        }
        else if(num>=60 && num<=69)
        {
            cout<<"D";
        }
        else
        {
            cout<<"F";
        }
    }
    return 0;
}