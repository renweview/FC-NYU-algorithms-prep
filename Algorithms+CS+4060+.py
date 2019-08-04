
# coding: utf-8

# In[3]:


# Professor Hsu 
# Ren
# : Implementing algorithms to sort 3 arrays and comparing their runtimes. 
import numpy as np #numpy is useful for randomly generating the numbers in the arrays, among other things
import pandas as pd #pandas is a data analysis library 


# In[45]:


#Submission will include Source code (hard copy to Professor Hsu in mailbox, soft copy emailed to TA Wang (not in docs))
#DESCRIPTION: We are using the 4 sorting algorithms: selection sort, insertion sort, merge sort and quick sort.
#For each data set (composed of 20,100, and 200 numbers respectively) we will 
#list the array, which are composed of randomly generated numbers.
#We will then list the four sorted arrays from the four sorting algorithms.
#I will get the runtime of each algorithm using "timeit." 
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html # for generating random numbers

#1. First i will generate the random integer arrays.
#2. INSERTION Sort runs:http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
#3. MERGE Sort runs
#4. QUICK Sort runs 
#5. SELECTION SORT runs


# In[46]:


a1 = np.random.randint(100, size=20) #randomly generating 20 integers, where the numbers range from 0-100. 
a2 = np.random.randint(100, size=100) #randomly generating 100 integers. 
a3 = np.random.randint(100, size=200) #randomly generating 200 integers. 
a4 = np.random.randint(100, size=3) #randomly generating 3 integers. This is null check to make sure my algorithms are working.
import timeit #import time for timing each run


# In[47]:


a1


# In[48]:


a2


# In[49]:


a3


# In[50]:


a4


# In[51]:


#Below are the runs for insertion sort.  
#a1 = array of 10 random integers. 

def insertionSort(a1):
   for index in range(1,len(a1)):

     currentvalue = a1[index]
     position = index

     while position>0 and a1[position-1]>currentvalue:
         a1[position]=a1[position-1]
         position = position-1

     a1[position]=currentvalue
start_time= timeit.timeit() #timing each run.
insertionSort(a1)
print(a1)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[54]:


#a2 = array of 100 random integers. 

def insertionSort(a2):
   for index in range(1,len(a2)):

     currentvalue = a2[index]
     position = index

     while position>0 and a2[position-1]>currentvalue:
         a2[position]=a2[position-1]
         position = position-1

     a2[position]=currentvalue
start_time= timeit.timeit() #timing each run.
insertionSort(a2)
print(a2)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[55]:


#a3 = array of 200 random integers. 

def insertionSort(a3):
   for index in range(1,len(a3)):

     currentvalue = a3[index]
     position = index

     while position>0 and a3[position-1]>currentvalue:
         a3[position]=a3[position-1]
         position = position-1

     a3[position]=currentvalue
start_time= timeit.timeit() #timing each run.
insertionSort(a3)
print(a3)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[60]:


#Below are the merge sort runs. 
a1merge = np.random.randint(100, size=20) #randomly generating 20 integers. 
a2merge = np.random.randint(100, size=100) #randomly generating 100 integers. 
a3merge = np.random.randint(100, size=200) #randomly generating 200 integers. 


# In[61]:


#a1merge= randomly generating 20 integers.
def mergeSort(a1merge):

   print("Splitting ",a1merge)

   if len(a1merge)>1:
       mid = len(a1merge)//2
       lefthalf = a1merge[:mid]
       righthalf = a1merge[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               a1merge[k]=lefthalf[i]
               i=i+1
           else:
               a1merge[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           a1merge[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           a1merge[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",a1merge)
start_time= timeit.timeit() #timing each run.
mergeSort(a1merge)
print(a1merge)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[62]:


#a2merge= randomly generating 100 integers.
def mergeSort(a2merge):

   print("Splitting ",a2merge)

   if len(a2merge)>1:
       mid = len(a2merge)//2
       lefthalf = a2merge[:mid]
       righthalf = a2merge[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               a2merge[k]=lefthalf[i]
               i=i+1
           else:
               a2merge[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           a2merge[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           a2merge[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",a2merge)
start_time= timeit.timeit() #timing each run.
mergeSort(a2merge)
print(a2merge)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[70]:


#a3merge= randomly generating 200 integers.
def mergeSort(a3merge):

   print("Splitting ",a3merge)

   if len(a3merge)>1:
       mid = len(a3merge)//2
       lefthalf = a3merge[:mid]
       righthalf = a3merge[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               a3merge[k]=lefthalf[i]
               i=i+1
           else:
               a3merge[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           a3merge[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           a3merge[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging", a3merge)
start_time= timeit.timeit() #timing each run.
mergeSort(a3merge)
print(a3merge)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[64]:


a1quick = np.random.randint(100, size=20) #randomly generating 20 integers. 
a2quick = np.random.randint(100, size=100) #randomly generating 100 integers. 
a3quick = np.random.randint(100, size=200) #randomly generating 200 integers.

#Below are the quick sort runs! 


# In[71]:


def quickSort(a1quick):
   quickSortHelper(a1quick,0,len(a1quick)-1)

def quickSortHelper(a1quick,first,last):
   if first<last:

       splitpoint = partition(a1quick,first,last)

       quickSortHelper(a1quick,first,splitpoint-1)
       quickSortHelper(a1quick,splitpoint+1,last)


def partition(a1quick,first,last):
   pivotvalue = a1quick[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and a1quick[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while a1quick[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = a1quick[leftmark]
           a1quick[leftmark] = a1quick[rightmark]
           a1quick[rightmark] = temp

   temp = a1quick[first]
   a1quick[first] = a1quick[rightmark]
   a1quick[rightmark] = temp


   return rightmark
print ("Quicksorting", a1quick)
quickSort(a1quick)
start_time= timeit.timeit() #timing each run.
print(a1quick)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[72]:


def quickSort(a2quick):
   quickSortHelper(a2quick,0,len(a2quick)-1)

def quickSortHelper(a2quick,first,last):
   if first<last:

       splitpoint = partition(a2quick,first,last)

       quickSortHelper(a2quick,first,splitpoint-1)
       quickSortHelper(a2quick,splitpoint+1,last)


def partition(a2quick,first,last):
   pivotvalue = a2quick[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and a2quick[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while a2quick[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = a2quick[leftmark]
           a2quick[leftmark] = a2quick[rightmark]
           a2quick[rightmark] = temp

   temp = a2quick[first]
   a2quick[first] = a2quick[rightmark]
   a2quick[rightmark] = temp


   return rightmark
print ("Quicksorting", a2quick)
quickSort(a2quick)
start_time= timeit.timeit() #timing each run.
print(a2quick)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[73]:


def quickSort(a3quick):
   quickSortHelper(a3quick,0,len(a3quick)-1)

def quickSortHelper(a3quick,first,last):
   if first<last:

       splitpoint = partition(a3quick,first,last)

       quickSortHelper(a3quick,first,splitpoint-1)
       quickSortHelper(a3quick,splitpoint+1,last)


def partition(a3quick,first,last):
   pivotvalue = a3quick[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and a3quick[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while a3quick[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = a3quick[leftmark]
           a3quick[leftmark] = a3quick[rightmark]
           a3quick[rightmark] = temp

   temp = a3quick[first]
   a3quick[first] = a3quick[rightmark]
   a3quick[rightmark] = temp


   return rightmark
print ("Quicksorting", a3quick)
quickSort(a3quick)
start_time= timeit.timeit() #timing each run.
print(a3quick)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[75]:


a1s = np.random.randint(100, size=20) #randomly generating 20 integers. 
a2s = np.random.randint(100, size=100) #randomly generating 100 integers. 
a3s = np.random.randint(100, size=200) #randomly generating 200 integers.

#Below are the SELECTION sort runs! 

def selectionSort(a1s):
   for fillslot in range(len(a1s)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if a1s[location]>a1s[positionOfMax]:
               positionOfMax = location

       temp = a1s[fillslot]
       a1s[fillslot] = a1s[positionOfMax]
       a1s[positionOfMax] = temp
start_time= timeit.timeit() #timing each run.
selectionSort(a1s)
print(a1s)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[76]:


def selectionSort(a2s):
   for fillslot in range(len(a1s)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if a2s[location]>a2s[positionOfMax]:
               positionOfMax = location

       temp = a2s[fillslot]
       a2s[fillslot] = a1s[positionOfMax]
       a2s[positionOfMax] = temp
start_time= timeit.timeit() #timing each run.
selectionSort(a2s)
print(a2s)
print('--- %s seconds ---' % (timeit.timeit() - start_time))


# In[77]:


def selectionSort(a3s):
   for fillslot in range(len(a3s)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if a3s[location]>a3s[positionOfMax]:
               positionOfMax = location

       temp = a3s[fillslot]
       a3s[fillslot] = a3s[positionOfMax]
       a3s[positionOfMax] = temp
start_time= timeit.timeit() #timing each run.
selectionSort(a3s)
print(a3s)
print('--- %s seconds ---' % (timeit.timeit() - start_time))

