#include <iostream>
using namespace std;

int main(void)
{
    int hour,min;
    cin>>hour>>min;
    
    if(hour>=0 && hour<=23 && min>=0 && min<=59)
    {
        if(min<45)
        {
            min = min +15;
            hour--;
            if(hour<0)
            {
                hour=23;
            }
        }
        else
        {
            min=min-45; 
        }
    }
    cout<<hour<<" "<<min;    
    return 0;
}