{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the no.of.elements4\n",
      "Enter the numbers:3\n",
      "new list is: [3]\n",
      "Enter the numbers:4\n",
      "new list is: [3, 4]\n",
      "Enter the numbers:5\n",
      "new list is: [3, 4, 5]\n",
      "Enter the numbers:6\n",
      "new list is: [3, 4, 5, 6]\n",
      "4\n",
      "Largest Number in the list 6\n",
      "Second largest Number in the list  5\n",
      "After swapping, the list is: 6 3\n"
     ]
    }
   ],
   "source": [
    "#Question1\n",
    "l=[]\n",
    "elements=int(input(\"Enter the no.of.elements\"))\n",
    "for i in range(elements):\n",
    "    n=int(input(\"Enter the numbers:\"))\n",
    "    l.append(n)\n",
    "    print(\"new list is:\",l)\n",
    "temp=len(l)\n",
    "print(len(l))\n",
    "l.sort()\n",
    "\n",
    "print(\"Largest Number in the list\",l[temp-1])\n",
    "print(\"Second largest Number in the list \",l[temp-2])\n",
    "\n",
    "l[0],l[-1] = l[-1], l[0]\n",
    "print(\"After swapping, the list is:\",l[0],l[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 5, 6, 3, 9, 2, 1, 7]\n",
      "After Sorting the list is : [1, 2, 3, 4, 5, 6, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "#Question2\n",
    "l1 = [4, 5, 6, 3]\n",
    "l2 = [9, 2, 1, 7]\n",
    "res=l1+l2\n",
    "print(res)\n",
    "res.sort()\n",
    "print(\"After Sorting the list is :\",res)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2, 5}\n",
      "{1, 2, 5, 7, 9}\n"
     ]
    }
   ],
   "source": [
    "#Question3\n",
    "l1 = {1, 2, 2, 5}\n",
    "l2 = {2, 5, 7, 9}\n",
    "\n",
    "print(l1.intersection(l2))\n",
    "print(l1.union(l2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the no.of.elements6\n",
      "Enter the numbers:8\n",
      "updated list is : [8]\n",
      "Enter the numbers:4\n",
      "updated list is : [8, 4]\n",
      "Enter the numbers:5\n",
      "updated list is : [8, 4, 5]\n",
      "Enter the numbers:4\n",
      "updated list is : [8, 4, 5, 4]\n",
      "Enter the numbers:3\n",
      "updated list is : [8, 4, 5, 4, 3]\n",
      "Enter the numbers:6\n",
      "updated list is : [8, 4, 5, 4, 3, 6]\n",
      "6\n",
      "The 3rd and 6th element 5 6\n",
      "First 5 elements [8, 4, 5, 4, 3]\n",
      "From 7 elements []\n",
      "After Changing first and second elements  x y\n",
      "The no.of elements in the list is  6\n"
     ]
    }
   ],
   "source": [
    "#Question4\n",
    "l=[]\n",
    "elem=int(input(\"Enter the no.of.elements\"))\n",
    "for i in range(elem):\n",
    "    n=int(input(\"Enter the numbers:\"))\n",
    "    l.append(n)\n",
    "    print(\"updated list is :\",l)\n",
    "length=len(l)\n",
    "print(len(l))\n",
    "print(\"The 3rd and 6th element\",l[2],l[5])\n",
    "print(\"First 5 elements\",l[:5])\n",
    "print(\"From 7 elements\",l[7:8])\n",
    "l[0]='x'\n",
    "l[1]='y'\n",
    "print(\"After Changing first and second elements \",l[0],l[1])\n",
    "print(\"The no.of elements in the list is \",len(l))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of elements to be in the list:4\n",
      "Element: 3\n",
      "Element: 4\n",
      "Element: 5\n",
      "Element: 6\n",
      "Largest even number: 6\n",
      "Largest odd number 5\n"
     ]
    }
   ],
   "source": [
    "# Question5\n",
    "n=int(input(\"Enter the number of elements to be in the list:\"))\n",
    "b=[]\n",
    "for i in range(0,n):\n",
    "    a=int(input(\"Element: \"))\n",
    "    b.append(a)\n",
    "c=[]\n",
    "d=[]\n",
    "for i in b:\n",
    "    if(i%2==0):\n",
    "        c.append(i)\n",
    "    else:\n",
    "        d.append(i)\n",
    "c.sort()\n",
    "d.sort()\n",
    "count1=0\n",
    "count2=0\n",
    "for k in c:\n",
    "    count1=count1+1\n",
    "for j in d:\n",
    "    count2=count2+1\n",
    "print(\"Largest even number:\",c[count1-1])\n",
    "print(\"Largest odd number\",d[count2-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the lower range:3\n",
      "Enter the upper range:4\n",
      "[(3, 9), (4, 16)]\n"
     ]
    }
   ],
   "source": [
    "#Question6\n",
    "l=int(input(\"Enter the lower range:\"))\n",
    "u=int(input(\"Enter the upper range:\"))\n",
    "a=[(x,x**2) for x in range(l,u+1)]\n",
    "a.sort()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of elements6\n",
      "Randomised list is:  [19, 11, 14, 10, 3, 11]\n"
     ]
    }
   ],
   "source": [
    "#Question7\n",
    "import random\n",
    "l=[]\n",
    "n=int(input(\"Enter number of elements\"))\n",
    "for j in range(n):\n",
    "    l.append(random.randint(1,20))\n",
    "print('Randomised list is: ',l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the coefficients of the polynomial\n",
      "Enter the coefficient:3\n",
      "Enter the coefficient:4\n",
      "Enter the coefficient:5\n",
      "Enter the value of x:2\n",
      "The value of the polynomial is: 25.0\n"
     ]
    }
   ],
   "source": [
    "#Question8\n",
    "import math\n",
    "print(\"Enter the coefficients of the polynomial\")\n",
    "lst=[]\n",
    "for i in range(0,3):\n",
    "    n=int(input(\"Enter the coefficient:\"))\n",
    "    lst.append(n)\n",
    "x=int(input(\"Enter the value of x:\"))\n",
    "sum=0\n",
    "j=2\n",
    "for i in range(0,2):\n",
    "    while(j>0): \n",
    "        sum=sum+(lst[i]*math.pow(x,j))\n",
    "        break\n",
    "    j=j-1\n",
    "sum=sum+lst[2]\n",
    "print(\"The value of the polynomial is:\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter lower range: 3\n",
      "Enter upper range: 60\n",
      "[<generator object perfect_squares.<locals>.<genexpr> at 0x00000293B9735AF0>]\n"
     ]
    }
   ],
   "source": [
    "#Question9\n",
    "l=int(input(\"Enter lower range: \"))\n",
    "u=int(input(\"Enter upper range: \"))\n",
    "a=[]\n",
    "a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question10\n",
    "a=[]\n",
    "num= int(input(\"Enter the number of elements in list:\"))\n",
    "for x in range(0,num):\n",
    "    element=int(input(\"Enter element\" + str(x+1) + \":\"))\n",
    "    a.append(element)\n",
    "b=[sum(a[0:x+1]) for x in range(0,len(a))]\n",
    "print(\"The original list is: \",a)\n",
    "print(\"The new list is: \",b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
