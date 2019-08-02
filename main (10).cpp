/******************************************************************************
1. Implement merge and insertion sort 
2. Run the program with 5 sets of inputs, each list needs to have 20 numbers. 
3. C++ ok. 
*******************************************************************************/
#include <iostream>
#include <stdlib.h> 
using namespace std; 

void merge(int*, int, int, int);

void mergesort(int *duparray, int first, int last){
    int mid; 
    if (first < last)
    {
    mid = (first + last)/2;
    mergesort(duparray, first, mid); 
    mergesort(duparray, mid+1, last);
    merge (duparray, first, last, mid);
    }
}
void merge(int* duparray, int first, int last, int mid)
{
int x, size=21, firsthi, secondh, outputi, output[20]; 

firsthi = first; 
secondh = mid +1; 
outputi = first;

while (firsthi <= mid && secondh <= last)
 {
     if (duparray[firsthi] < duparray[secondh])
     {
         output[outputi] = duparray[firsthi];
         outputi++;
         firsthi++;
     }
     else
        {
            output[outputi] = duparray[secondh];
            outputi++;
            secondh++; 
        }
 }

while (firsthi <= mid)
{
    output[outputi] = duparray[firsthi];
    
    outputi++;
    firsthi++; 
}

while(secondh <= mid)
{
output[outputi] = duparray[secondh];

outputi++; 
secondh++; 
}

for (firsthi = first; firsthi < outputi; firsthi++)
    {
    duparray[firsthi] = output[firsthi];
    }

for(x=0; x<size; x++)
	{
		cout<<"This is the MERGEsort array:" << duparray[x]<<" ";
	}
	
}

int main()
{
	int size=20, arr[20], i, j, temp;
	int duparray[20], x; 
	cout<<"Enter only 20 array Elements, spaces after each one: ";
	for(i=0; i<size; i++)
	{
		cin>>arr[i];
	}
	
	for (int i = 0; i <size; i++)
	{
	    duparray[x] = arr[i];
	    cout << "This value is going into the duplicated array: " << duparray[x] << endl; 
	}
	
	cout << "Using this duplicated array to start a MERGEsort." << endl; // this works correctly, each item gets called out.

//Mergesort using the duplicated array (duparray)

mergesort(duparray, 0, duparray[x]-1); //SPACE ISSUE HERE, MERGE SORT is malfunctioning. 

//Insertion sort section:
	cout<< endl << "Sorting array using insertion sort. One moment.";
		for(i=1; i<size; i++)
	{
		temp=arr[i];
		j=i-1;
		while((temp<arr[j]) && (j>=0))
		{
			arr[j+1]=arr[j];
			j=j-1;
		}
		arr[j+1]=temp;
	}
	cout<< endl << "Array after INSERTION sort:" << endl;
	for(i=0; i<size; i++)
	{
		cout<<arr[i]<<" "; //correctly outputs.
	}
	
}

