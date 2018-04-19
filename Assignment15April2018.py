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
      "Please enter the first number 23\n",
      "Please enter the second number42\n",
      "the sum of 2 numbers is : 65\n"
     ]
    }
   ],
   "source": [
    "Number1 = int(input(\"Please enter the first number \"))\n",
    "Number2 = int(input(\"Please enter the second number\"))\n",
    "sum = Number1+Number2\n",
    "print(\"the sum of 2 numbers is : %d\"%(sum))"
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
      "Please enter the first number 4\n",
      "It is not a prime Number\n"
     ]
    }
   ],
   "source": [
    "Num = int(input(\"Please enter the first number \"))\n",
    "e=0\n",
    "for i in range(2,Num):\n",
    "    if(Num%i==0):\n",
    "        e=1\n",
    "        break\n",
    "if(e==0):\n",
    "    print(\"It is a prime number\")\n",
    "else:\n",
    "    print(\"It is not a prime Number\")"
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
      "Enter the Height of the triangle4\n",
      "Enter the Base of the triangle6\n",
      "Area of the triangle : 12.000000\n"
     ]
    }
   ],
   "source": [
    "height=float(input(\"Enter the Height of the triangle\"))\n",
    "base=float(input(\"Enter the Base of the triangle\"))\n",
    "\n",
    "area =(height * base)/2\n",
    "\n",
    "print(\"Area of the triangle : %f\" %area)\n",
    "\n",
    "\n"
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
      "Please enter the first number 5\n",
      "Please enter the second number6\n",
      "Before swap : \n",
      "First : 5  second : 6\n",
      "After swap : \n",
      "First : 6  second : 5\n"
     ]
    }
   ],
   "source": [
    "first = int(input(\"Please enter the first number \"))\n",
    "second = int(input(\"Please enter the second number\"))\n",
    "\n",
    "print(\"Before swap : \")\n",
    "print(\"First : %d  second : %d\" %(first,second))\n",
    "\n",
    "first = first + second\n",
    "second = first-second\n",
    "first = first-second\n",
    "\n",
    "print(\"After swap : \")\n",
    "print(\"First : %d  second : %d\" %(first,second))"
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
      "Enter a: 8\n",
      "Enter b: 16\n",
      "Enter c: 8\n",
      "The solution are (-1+0j) and (-1+0j)\n"
     ]
    }
   ],
   "source": [
    "import cmath  \n",
    "a = float(input('Enter a: '))  \n",
    "b = float(input('Enter b: '))  \n",
    "c = float(input('Enter c: '))  \n",
    "  \n",
    "d = (b**2) - (4*a*c)  \n",
    " \n",
    "sol1 = (-b-cmath.sqrt(d))/(2*a)  \n",
    "sol2 = (-b+cmath.sqrt(d))/(2*a)  \n",
    "print('The solution are {0} and {1}'.format(sol1,sol2))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the year : 2100\n",
      "Entered Year is not a leap year\n"
     ]
    }
   ],
   "source": [
    "year = int (input(\"Enter the year : \"))\n",
    "\n",
    "valid=0\n",
    "\n",
    "if((year%400==0 and  year%4==0)):\n",
    "    valid=1\n",
    "elif year%100==0:\n",
    "    valid=0\n",
    "\n",
    "if(valid==1):\n",
    "    print(\"Entered Year is  leap year\")\n",
    "else:\n",
    "    print(\"Entered Year is not a leap year\")\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " enter the number :-4\n",
      "negative number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\" enter the number :\" ))\n",
    "\n",
    "if(num>0):\n",
    "    print(\"positive number\")\n",
    "elif(num==0):\n",
    "    print(\"Number is zero\")\n",
    "else:\n",
    "    print(\"negative number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter how many number of natural numbers20\n",
      "the sum is : 210\n"
     ]
    }
   ],
   "source": [
    "n= int(input(\"Enter how many number of natural numbers\"))\n",
    "\n",
    "sum = n*(n+1)/2\n",
    "print(\"the sum is : %d\" %sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number4\n",
      "number is even\n"
     ]
    }
   ],
   "source": [
    "n= int(input(\"Enter the number\"))\n",
    "\n",
    "if(n%2==0):\n",
    "    print(\"number is even\")\n",
    "    \n",
    "else:\n",
    "    print(\"number is odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n= int(input(\"Enter the number\"))\n",
    "\n",
    "def fact(n):\n",
    "    if(n==1):\n",
    "        return 1\n",
    "    else:\n",
    "        return n * fact(n-1)\n",
    "    \n",
    "fact(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Table number5\n",
      "how many no of multiples you want : 10\n",
      " 5  * 1 : 5 \n",
      " 5  * 2 : 10 \n",
      " 5  * 3 : 15 \n",
      " 5  * 4 : 20 \n",
      " 5  * 5 : 25 \n",
      " 5  * 6 : 30 \n",
      " 5  * 7 : 35 \n",
      " 5  * 8 : 40 \n",
      " 5  * 9 : 45 \n",
      " 5  * 10 : 50 \n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter the Table number\"))\n",
    "m = int (input (\"how many no of multiples you want : \"))\n",
    "\n",
    "for i in range(1,m+1):\n",
    "    mul=n*i\n",
    "    print(\" %d  * %d : %d \" %(n,i,mul))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of series8\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter the number of series\"))\n",
    "\n",
    "n1=0\n",
    "n2=1\n",
    "i=0\n",
    "print(n1)\n",
    "print(n2)\n",
    "while(i<n-2):\n",
    "    num=n1+n2\n",
    "    print(num)\n",
    "    n1=n2\n",
    "    n2=num\n",
    "    i=i+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number12\n",
      "Enter the number23\n",
      "Enter the number34\n",
      "4 is the largest number \n"
     ]
    }
   ],
   "source": [
    "n1 =  int(input(\"Enter the number1\"))\n",
    "n2 =  int(input(\"Enter the number2\"))\n",
    "n3 =  int(input(\"Enter the number3\"))\n",
    "\n",
    "if((n1>=n2) and (n1>n3)):\n",
    "    print(\"%d is the largest number \" % n1)\n",
    "elif((n2>=n1) and (n2>n3)):\n",
    "    print(\"%d is the largest number \" % n2)\n",
    "elif((n3>=n1) and (n3>n2)):\n",
    "    print(\"%d is the largest number \" % n3)\n",
    "if((n1<=n2) and (n1<n3)):\n",
    "    print(\"%d is the smallest number \" % n1)\n",
    "elif((n2<=n1) and (n2<n3)):\n",
    "    print(\"%d is the smallest number \" % n2)\n",
    "elif((n3<=n1) and (n3<n2)):\n",
    "    print(\"%d is the smallest number \" % n3)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " please enter the kilo meters 5\n",
      "the mile convertion :  3.106855\n"
     ]
    }
   ],
   "source": [
    "km = float(input(\" please enter the kilo meters \"))\n",
    "\n",
    "miles =  km * 0.621371\n",
    "\n",
    "print(\"the mile convertion :  %f\" %miles )\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " please enter the celsius 30\n",
      "the farenheit convertion :  86.000000\n"
     ]
    }
   ],
   "source": [
    "c = float(input(\" please enter the celsius \"))\n",
    "\n",
    "f =  c * 1.8 +32\n",
    "\n",
    "print(\"the farenheit convertion :  %f\" %f )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number4\n",
      "0b100 in binary.\n",
      "0o4 in octal.\n",
      "0x4 in hexadecimal.\n"
     ]
    }
   ],
   "source": [
    "dec = int(input(\"enter the number\"))\n",
    "\n",
    "print(bin(dec),\"in binary.\")\n",
    "print(oct(dec),\"in octal.\")\n",
    "print(hex(dec),\"in hexadecimal.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number: 2\n",
      "Enter second number: 3\n",
      "Enter your choice.\n",
      "1.Add\n",
      "2.Subtract\n",
      "3.Multiply\n",
      "4.Divide\n",
      "choose one of the above:2\n",
      "2 - 3 : -1 \n"
     ]
    }
   ],
   "source": [
    "n1 = int(input(\"Enter first number: \"))\n",
    "n2 = int(input(\"Enter second number: \"))\n",
    "\n",
    "print(\"Enter your choice.\")\n",
    "print(\"1.Add\")\n",
    "print(\"2.Subtract\")\n",
    "print(\"3.Multiply\")\n",
    "print(\"4.Divide\")\n",
    "\n",
    "\n",
    "c = int(input(\"choose one of the above:\"))\n",
    "\n",
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    return x / y\n",
    "\n",
    "if c == 1:\n",
    "    print(\"%d + %d : %d \" %(n1,n2,add(n1,n2)))\n",
    "\n",
    "elif c == 2:\n",
    "    print(\"%d - %d : %d \" %(n1,n2,subtract(n1,n2)))\n",
    "elif c == 3:\n",
    "    print(\"%d * %d : %d \" %(n1,n2,multiply(n1,n2)))\n",
    "\n",
    "elif c == 4:\n",
    "    print(\"%d / %d : %d \" %(n1,n2,divide(n1,n2)))\n",
    "else:\n",
    "    print(\" please give write  input \")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
