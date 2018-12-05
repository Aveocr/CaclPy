#!/usr/bin/env python3
from math import pow
NULL = ''
version = 0.1
action = True


# main unit
def main():
    print("Hello! This is my calc, which I was writting with Python. Version %f and Autor - Denis Mustafin" % version)
    action = True
    while action==True:
        oneNumb = float(input("\nPlease, input your first number -> "))
        twoNumb = float(input("\nPlease, input your second number -> "))
        value = str(input("\nWhat do you want doing now? *, /, +, -. ^ or for exit exit --> "))
        chooseValue = {
		    '+': "\n%f+%f=%f\n " % (oneNumb, twoNumb, oneNumb+twoNumb),
		    '-': "\n%f-%f=%f\n " % (oneNumb, twoNumb, oneNumb-twoNumb),
		    '*': "\n%f*%f=%f\n " % (oneNumb, twoNumb, oneNumb*twoNumb),
		    '/': "\n%f/%f=%f\n " % (oneNumb, twoNumb, oneNumb/twoNumb),
		    '^': "\n%f*%f=%f\n " % (oneNumb, twoNumb, pow(oneNumb, twoNumb))
	    }
        if(value == 'exit'):
            action = False
            print("=(. goodluck you and I'm sleep!")
        print(chooseValue.get(value))



main()
