#!/usr/bin/env python
# -*- coding: utf-8 -*-


#doCollatz is iterative due to the fact that python limits the recursive depth
def doCollatz(number):
    #Continue until it is 1
    while number > 1:
        #If it is an even number
        if number % 2 == 0:
            number /= 2
        #If it is an odd number
        else:
            number = 3 * number + 1

        #Print the step made
        print "Step: {0}" .format(number)



def main():
    #Gives the possibility to do it as many times as you want
    while True:
        #Take input until it is correct
        while True:
            number = int(raw_input('Enter positive number (-1 to exit): '))

            #If is valid continue execution
            if int(number) >= 0:
                break
            else:
                if int(number) == -1:
                    exit(0)

        print "Number {0}" .format(number)

        #execute doCollatz with the number introduced
        doCollatz(int(number))

if __name__ == '__main__':
    main()
