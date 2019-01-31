#include<iostream>
using namespace std;

void swap(int *p,int *q)
{
	int temp=*p;
	*p=*q;
	*q=temp;
}
void printarray(int arr[],int n)
{
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}

// This is the sorting for selection sort
void selectionsort(int arr[],int n)
{
	for (int i=0;i<n-1;i++)
	{
		int pos=i;
		for (int j=i+1;j<n;j++)
		{
			if(arr[j]<arr[pos])
			{
				pos=j;
			}
		}
		swap(&arr[i],&arr[pos]);
	}
}
// This is the sorting algorithum for the bubble sort 
void bubblesort(int arr[],int n)
{
	for(int i=0;i<n-1;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			if (arr[j]<arr[i])
			{
				swap(&arr[j],&arr[i]);
			}
		}
	}
}
// This is the sorting done by the insertion sort
void insertionsort(int arr[],int n)
{
	for (int i=0;i<n;i++)
	{
		int pos=i;
		while( pos>0 && arr[pos]<arr[pos-1])
		{
			swap(&arr[pos],&arr[pos-1]);
			pos=pos-1;
		}
	}
}
int main()
{
	int n;
	cout<<"Enter the number of elements in the array"<<endl;
	cin>>n;
	int arr[n];
	for  (int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	cout<<"Now sorting the array"<<endl;
	//selectionsort(arr,n);
	//bubblesort(arr,n);
	insertionsort(arr,n);
	cout<<"Printing the array"<<endl;
	printarray(arr,n);
	return 0;
}
