#include<iostream>
#include<bits/stdc++.h>
#include<string>
using namespace std;
// Each unit is of 20 marks

class properties 				// Abstract class
{
	public:
		int units;
		int chapters;
		int marks_per_unit=18;
		virtual void chapter_assignment()=0;				// Pure virtual function
};

bool sortbysec(const tuple<int, int>& a,
               const tuple<int, int>& b)		// function used for sorting the tuple
{
    return (get<1>(a) < get<1>(b));
}

class subject: public properties							// derived class inheriting the abstract base class
{
	private:
		vector<tuple<int,int>> s;						  		// vector of tuple of 2 items
		//float marks =0;
		float marks_of_subtopic_for_each_unit[6]={0};
		//float marks_obtained=0;

	public:
    int subtopics_done;
		int index_of_s=0;
		string name;
    int like;
		subject()                								   // Constructor
		{
		    cout<<"Name of the subject ?"<<endl;
		    //getline(cin,name);
        cin>>name;
			units=5;
			chapters=10;
      chapter_assignment();
      unit_choosing();
      subtopics_done=0;
		}
		void unit_choosing();															// Defined all these functions outside the class to
		void display();																		// have a clear view of class
		void chapter_assignment();
		void marks_distribution();
		int study();
		friend void studyplan();             // Friend function to access the array of objects from main function
                                        //and to access class functions
};
//int subject::subtopics_done=0;
void subject :: chapter_assignment()    //Provided defination to the pure virtual function of base class in derived class
{
	// Now we need to assign the number of chapters to each unit
	srand(time(0));
	int u=units;
	int c=chapters;
	for (int i=0;i<units;i++)
	{
		int count=c-u+1;
		int num=(rand()% (1-count+1))+1;
		if (i==units-1)
		{
		    s.push_back(make_tuple(i,c));
		    break;
		}
		if (num<=count && c-num>=u-1)
		{
			u--;
			c-=num;
		}
		else{
			s.push_back(make_tuple(i,1));
			continue;
		}
		s.push_back(make_tuple(i,num));
	}
}

void subject ::unit_choosing()					// selection of units, select those which have minimum no. of elements
{
	// In case to choose a unit for a subject, sort the units  according to the increasing order or number of chapters
  sort(s.begin(), s.end(), sortbysec);
}

void subject :: display()							 // Display the index of all the subjects
{
  cout<<"Name Of Subject : "<<name<<endl;
    for (int i=0;i<s.size();i++)
    {
      cout<<"Unit - "<<get<0>(s[i])<<"\t Chapters - "<<get<1>(s[i])<<" Marks distribution "<<marks_of_subtopic_for_each_unit[i]<<endl;
    }
}

void subject :: marks_distribution()		// distribution of marks to each subtopic which is based on the no. of chapters in a unit
{
	for (int i=0;i<6;i++)									// Distribution of marks of a subtopic in each unit
	{
		int no_of_chap= get<1>(s[i]);
		float marks_per_chap = marks_per_unit/no_of_chap;
		float marks_per_subtopic= marks_per_chap/6;
		marks_of_subtopic_for_each_unit[i]=marks_per_subtopic;
	}
}
// Study for 1 hour each day, each subject

int subject :: study()
{
	float score=0;
	int net_subtopics= get<1>(s[index_of_s])*6;
	if (like)
	{
		//cout<<"Net_subtopics "<<net_subtopics<<endl;
		score =3*marks_of_subtopic_for_each_unit[index_of_s];
		subtopics_done +=3;
	}
	else
	{
		//cout<<"Net_subtopics "<<net_subtopics<<endl;
		score =2*marks_of_subtopic_for_each_unit[index_of_s];
		subtopics_done +=2;
	}
	cout<<name<<"_"<<get<0>(s[index_of_s])<<"\t";      // name of subject_ unit number
	if (subtopics_done >= net_subtopics )
	{
    //cout<<"Subtopics "<<subtopics_done<<" net_subtopics "<<net_subtopics<<endl;
		index_of_s+=1;
		subtopics_done=0;
	}
	return score;
}

void studyplan(vector <subject> &
  arr, float marks[])
{
	for(int i=0;i<6;i++)									// 6 timing slots of 1 hour each, now to determine which subject is need to be learned, we run loop
	{
		int min=0;
		for (int j=0;j<6;j++)
		{
			if (marks[j]<marks[min])
			{
				min=j;
			}
		}
		marks[min]+=arr[min].study();	  	// We choose to study the subject with minimum marks till now.
	}
}

int main()
{
  int max_study_inaday=6;
  vector <subject> arr;
	float marks[6]={0};
  cout<<"Total number of Subjects = 6"<<endl;
  cout<<"Each subject has= units=5      Each unit has chapters=10      subtopics in each chapter=6"<<endl;
  for(int i=0;i<6;i++)
  {
    cout<<"Enter the details of subject "<<i+1<<endl;
    subject s ;
    cout<<"Do you like "<<s.name<<" subject yes/no ?"<<endl;
    string x;
    cin>>x;
    if (x=="yes")
    s.like=1;
    else
    s.like=0;
    arr.push_back(s);
  }
	/*
  	 Marks could be scored based on the	currently studied material are assigned to every subject.

		 The marks assignment is done on the basis of subtopics studied ans subtopics are divided according to the chapters
		 assigned to the unit (as each unit is of 18 marks).

		 After the assignment of th marks, we will choose the subject which has the least score and if the subject is a 'dislike', then
		 we wont study it again in that day.
	*/
	for (int i=0;i<6;i++)					// Distribution of marks to each subtopic of a chapter in each unit is stored.
	{
		arr[i].marks_distribution();
	}

	cout<<"******* This is the Index of the subjects ********"<<endl;
  for(int i=0;i<6;i++)
  {
    arr[i].display();
  }

// Now initially study every subject for 2 hours
	for(int i=0;i<23;i++)
	{
    cout<<"***********DAY "<<i+1<<" **************"<<endl;			// Running loop for 23 days
    /*if (i>22)
    {
      practicals()
    }*/
		studyplan(arr,marks);
		cout<<endl;
	}

  cout<<"************* MARKS SCORED **************"<<endl;
	cout<<"marks scored in each subject"<<endl;
	for(int i=0;i<6;i++)
	{
		cout<<arr[i].name<<"\t"<<marks[i]<<endl;
	}
	return 0;
}
