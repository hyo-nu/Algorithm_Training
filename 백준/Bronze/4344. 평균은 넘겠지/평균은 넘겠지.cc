#include <iostream>
using namespace std;

int main()
{
    int C, num, sum, avg, count;
    int score[1000];
    double result;
    
    cin>>C;
    for(int i=0; i<C; i++)
    {
        sum = 0;
        avg = 0;
        count = 0;
        
        cin>>num;
        for(int j=0; j<num; j++)
        {
            cin>>score[j];
            sum += score[j];
        }
        for(int j=0; j<num; j++)
        {
            avg = sum / num;
            if(score[j]>avg)
            {
                count++;
            }
        }
        result = (double)count / num *100;
        
        cout << fixed;
        cout.precision(3);
        cout<<result<<"%"<<endl;
    }
    return 0; 
}