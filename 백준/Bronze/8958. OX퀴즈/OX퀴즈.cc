#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int num;
    cin>>num;
    
    char arr[80];
    int score[num]={0};
    
    for(int i = 0; i < num; i++)
    {
       int con=0;
       cin>>arr;
        
       for(int j = 0; j < strlen(arr); j++)
       {           
           if(arr[j]=='O')
           {
               con++;
               score[i] += con;
           }
           else if(arr[j]=='X')
           {
               con=0;
           }
       }
       cout<<score[i]<<endl;
    }
    return 0;
}