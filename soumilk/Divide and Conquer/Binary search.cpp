#include<iostream>
using namespace std;

// This is the method of iteration for the binary search
void binarysearch(int arr[],int t,int n)
{
	int low=0;
	int high=n-1;
	int mid= (low+high)/2;
	for( ; high>=low ; )
	{
		if(arr[mid]==t)
		{
			cout<<"The element is found at "<<mid<<endl;
			return;
		}
		else if(arr[mid]<t)
		{
			low =mid+1;
			mid=(low+high)/2;
		}
		else
		{
			high=mid-1;
			mid=(low+high)/2;
		}
	}
	cout<<"element not found"<<endl;
}

// Recurssive method for the binary search 
int binarysearchrecurssion(int arr[],int t, int high, int low)
{
	if(high>=low)
	{
		int mid=(high+low)/2;
		if(arr[mid]==t)
		{
			cout<<"The elelemt is found at "<<mid<<endl;
			return 1;
		}
		if(arr[mid]<t)
		{
			binarysearchrecurssion(arr,t,high,mid+1);
		}
		else {
			binarysearchrecurssion(arr,t,mid-1,low);
		}
	}
	return -1;
}
int main()
{
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	cout<<"enter the element to search in the array"<<endl;
	int t;
	cin>>t;
	binarysearch(arr,t,n);
	int s=binarysearchrecurssion(arr,t,n-1,0);
	if (s==-1)
	{
		cout<<"Element not found "<<endl;
	}
	return 0;
}
