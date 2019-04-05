#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>
#include <iomanip>
using namespace std;

bool effects(int n)                       // this is the funciton which tests the condition and rules in 3 question.
{                                         // prime or not and is it divisible by 13 or 15
    if (n <= 1)
        return false;
    for (int i = 2; i < n; i++)
        {if (n % i == 0)
        {
			return false;
		}
        }
	if (n%13==0 || n%15==0)
    return true;

    return false;
}
class fight
{
	private:
		float h_thanos=0,h_bahu=0,att_thanos_time=0,att_bahu_time=0;
		float t=0;
		float dup_thanos=0,dup_bahu=0;
		int attack_no=0,b_attack_no=0,t_attack_no=0;
	public:
		fight()
		{
			cout<<"Enter the health of thanos and bhaubhali, either same or maximum difference of 5%"<<endl;
			cin>>h_thanos>>h_bahu;
		}
        void display()
		{
			cout<<"health of bahu "<<h_bahu<<"\t health of thanos "<<h_thanos
			<<" \t attack no "<<attack_no<<"\tatt_thanos_time= "<<att_thanos_time<<" \tatt_bahu_time= "<<att_bahu_time
			<<"\t Current time= "<<t<<" sec "<<endl;
		}

		void checkinputs();
		void tattack();
		void battack();
		string start();
};
void fight::checkinputs()
	{
		float ma=max(h_thanos,h_bahu);
		float mi=min(h_thanos,h_bahu);
		while (((ma-mi)/ma)*100>5)
		{
			cout<<"You havnt entered the valid input, please enter the valid inputs of health of both fighters"<<endl;
			cin>>h_thanos>>h_bahu;
			ma=max(h_thanos,h_bahu);
			mi=min(h_thanos,h_bahu);
		}
		dup_thanos=h_thanos;
		dup_bahu=h_bahu;
	}
void fight::tattack()
{
	cout<<"***************THIS IS FOR GOOD BUT WHO TOOK MY STONE******************"<<endl;
	float limit= ((dup_bahu-h_bahu)/dup_bahu)*100;                     // calculating the present % of health in comparision to the initial health
	float damage=0.15;
	float num=rand();                                                  // random number
	if (effects(num))                                                  // function calling which will return a bool
	{
		num = ((rand() % (8 - 5 + 1)) + 5)/100;                           // Generate a random value between 5 to 8
		damage=damage -num;                                               // damage % of thanos is decreased by that random fraction
	}
	if ((t_attack_no%5==0 || t_attack_no%7==0) && limit>61.5)
	{
	}
	else if (t_attack_no%2==0 && t_attack_no!=0)
	{
		h_bahu=h_bahu - h_bahu*(damage+0.5);
	}
	else
	{
		h_bahu=h_bahu- h_bahu*(damage);
	}
	att_bahu_time+=1;
	att_thanos_time+=3;                                                  // reattacking time is increased to 3sec
	attack_no+=1;
	t_attack_no+=1;
}
void fight::battack()
{
	cout<<"***********JAI MAHESHMATI*************"<<endl;
	float limit= ((dup_thanos-h_thanos)/dup_thanos)*100;
	if ((t_attack_no%5==0 || t_attack_no%7==0) && limit>61.5)
	{
	}
	else if (b_attack_no%3==0 && b_attack_no!=0)
	{
		h_thanos-= h_thanos*(0.18);
	}
	else
	{
		h_thanos-=h_thanos*(0.10);
	}
	att_bahu_time+=2;
	att_thanos_time+=3;                                                 // recover time is increased to 3 sec
	attack_no+=1;
	b_attack_no+=1;

}
string fight::start()
{
	while(h_bahu>=0.1 && h_thanos>=0.1)
	{
		if (t==att_thanos_time)
		{
			tattack();
			display();
		}
		if (t==att_bahu_time)
		{
			battack();
			display();
		}
		//display(h_bahu,h_thanos,attack_no);
		t+=0.5;
	}
	if (h_bahu>0)
		return "Bahubhali wins";

	return "Thanos wins";
}
int main()
{
	fight f;
	f.checkinputs();
	srand (time(NULL));
	cout<<"At t=0"<<endl;
	if (rand()%2==0 && rand()%5==0)
	{
		f.battack();
	}
	else
	{
		f.tattack();
	}
	f.display();
	//cout<<f.dup_bahu<<" "<<f.dup_thanos<<endl;
	string s=f.start();
	cout<<s<<endl;
	return 0;
}
