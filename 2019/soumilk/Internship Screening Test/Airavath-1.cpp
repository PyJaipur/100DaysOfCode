#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>
using namespace std;

class fight																			// Class which includes the details about the fighers
{
	private:																			// private data types of class
		float h_thanos=0,h_bahu=0,att_thanos_time=0,att_bahu_time=0;
		float t=0;
		float loss_thanos=0,loss_bahu=0;
		int attack_no=0;
	public:
		fight()																		   // default constructor
		{
			cout<<"Enter the health of thanos and bhaubhali, either same or maximum difference of 5%"<<endl;
			cin>>h_thanos>>h_bahu;
		}
		void display()															// To display the present status of both fighters
		{
			cout<<"health of bahu "<<h_bahu<<"\t health of thanos "<<h_thanos
			<<" \t attack no "<<attack_no<<"\tatt_thanos_time= "<<att_thanos_time<<" \tatt_bahu_time= "<<att_bahu_time
			<<"\t Current time= "<<t<<" sec "<<endl;
		}

		void checkinputs();													// To check whether the given input is correct or not
		void tattack();														 // Thanos is attacking
		void battack();														 // Bahubhali is attacking
		string start();														// fight begins
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
		loss_thanos=h_thanos*(0.10);								// amount of damage thanos receive from bahubali
		loss_bahu= h_bahu*(0.15);										// amount of damage bahubali receives from Thanos
	}
void fight::tattack()
{
	cout<<"***********THIS IS FOR GOOD**************"<<endl;
	h_bahu-=loss_bahu;														// damage to the health of bahubali when thanos attacks
	att_bahu_time+=1;															// recover time =1s
	att_thanos_time+=2.5;
	attack_no+=1;
	loss_bahu=h_bahu*(0.15);											// updated the % of present health damage
	display();
}
void fight::battack()
{
	cout<<"************JAI MAHESHMATI***************"<<endl;
	h_thanos-=loss_thanos;												// damage to the health of thanos when bahubali attacks
	att_bahu_time+=2;
	att_thanos_time+=1;
	attack_no+=1;
	loss_thanos=h_thanos*(0.10);									// updated the % of present health damage
	display();
}
string fight::start()
{
	while( h_bahu>0.1 && h_thanos>0.1)
	{
		if (t==att_thanos_time)
		{
			tattack();
		}
		if (t==att_bahu_time)
		{
			battack();
		}
		t+=0.5;																			// Increasing time by 0.5 seconds
	}
	if (h_bahu>0)
		return "Bahubhali wins";

	return "Thanos wins";
}
int main()
{
	fight f;
	f.checkinputs();
	srand (time(NULL));														// to generate a seed for the random values
	cout<<"At t=0"<<endl;
	if (rand()%2==0 && rand()%5==0)
	{
		//cout<<rand();
		f.battack();
	}
	else
	{
		//cout<<rand();
		f.tattack();
	}
	string s=f.start();
	cout<<s<<endl;
	return 0;
}
