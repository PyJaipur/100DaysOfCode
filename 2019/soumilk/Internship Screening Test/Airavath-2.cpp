#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>
using namespace std;

class fight
{
	private:
		float h_thanos=0,h_bahu=0,att_thanos_time=0,att_bahu_time=0;
		float t=0;
		float dup_thanos=0,dup_bahu=0;																	// to store the values of the health initially (useful in calculating 61.5% factor)
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
			<<" \t attack no "<<attack_no<<"\ttime "<<t<<"\n"
			<<"att_thanos_time "<<att_thanos_time<<" \tatt_bahu_time "<<att_bahu_time<<endl;
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
		float t=0;
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
	cout<<"****************THIS IS FOR GOOD**************"<<endl;
	float limit= ((dup_bahu-h_bahu)/dup_bahu)*100;
	if ((t_attack_no%5==0 || t_attack_no%7==0) && limit>61.5)					//if this is the condition then there will be no damage to the opponent
	{		// do nothing																									// this condition is superier then the below condition logically
	}
	else if (t_attack_no%2==0 && t_attack_no!=0)
	{
		h_bahu-=h_bahu*(0.20);																					// according to the rule 5% more power
	}
	else
	{
		h_bahu-=h_bahu*(0.15);
	}
	att_bahu_time+=1;
	att_thanos_time+=2.5;
	attack_no+=1;
	t_attack_no+=1;
	display();
}
void fight::battack()
{
	cout<<"******************JAI MAHESHMATI*****************"<<endl;
	float limit= ((dup_thanos-h_thanos)/dup_thanos)*100;
	if ((t_attack_no%5==0 || t_attack_no%7==0) && limit>61.5)					//if this is the condition then there will be no damage to the opponent
	{		// do nothing																								 // this condition is superier then the below condition logically
	}
	else if (b_attack_no%3==0 && b_attack_no!=0)
	{
		h_thanos-=h_thanos*(0.18);																			// according to the rule 8% more power
	}
	else
	{
		h_thanos-=h_thanos*(0.10);
	}
	att_bahu_time+=2;
	att_thanos_time+=1;
	attack_no+=1;
	b_attack_no+=1;
	display();

}
string fight::start()
{
	while(h_bahu>0.1 && h_thanos>0.1)
	{
		if (t==att_thanos_time)
		{
			tattack();
		}
		if (t==att_bahu_time)
		{
			battack();
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
	string s=f.start();
	cout<<s<<endl;
	return 0;
}
