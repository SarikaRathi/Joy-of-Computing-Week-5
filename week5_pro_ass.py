# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:53:28 2021

@author: ADMIN
"""

# Week 5: Programming Assignment 1 - k times
# Due on 2021-09-02, 23:59 IST
# Given a list of integers and a value k, print the number in the list that appears exactly k times. (It is guaranteed that there’s exactly one integer that appears k times).
# Input Format:
# First line of the input contains a list of integers
# Second line of the input contains a value k
# Output Format:
# Display the number that appears exactly k 

from collections import Counter
l = [int(x) for x in input().split()]
k=int(input())
a=Counter(l)

for key,value in a.items():
  if k == value:
    print(key,end="")
    
# Week 5: Programming Assignment 2 - kth Largest
# Due on 2021-09-02, 23:59 IST
# Given a list of integers and a value k, print the kth largest element in the list. (All the elements in the list are guaranteed to be distinct).
# Input Format:
# First line of the input contains a list of integers
# Second line of the input contains a value k
# Output Format:
# # Display the kth largest element in the list

list_int = input().split()
k=int(input())
ans=[]
for i in list_int:
  ans.append(int(i))
ans.sort(reverse=True)

print(ans[k-1],end="")  

# Week 5: Programming Assignment 3 - Cumulative sum
# Due on 2021-09-02, 23:59 IST
# Given a list of n integers, print a new list such that every element in the new list represents the cumulative sum of all the elements until that position.
# Input Format:
# Single line of input contains a list of space separated integers 
# Output Format:
# Print the cumulative list

l = [int(x) for x in input().split()]
def Cumulative(l):
    cu_list = []
    length = len(l)
    cu_list = [sum(l[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
 
for i in range(len(Cumulative(l))):
  print(Cumulative(l)[i],end=" ")
