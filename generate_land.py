#! /usr/bin/python

import math
import random

matrix=[]
deck=[]
watercount = 0
default="Water"

def matrixbuild(r,c):
        for i in range(r):
                matrix.append([cardlistgenerate(c) for x in range(1)])

def cardlistgenerate(x):
        returnd=[]
        difficulty = 5 #Lower for harder
        d = difficulty
        global watercount
        global default
        for i in range(x):
                z=random.randint(0,d)
                if z>1 and len(deck)!=0:
                        returnd.append(deck[0])
                        deck.pop(0)
                else:
                        returnd.append(default)
                        watercount +=1
        return returnd

def addcards():
        cards=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three","twenty-four"]
        x=len(cards)
        for i in range(x):
                n=len(cards)
                z=random.randint(0,n)
                deck.append(cards[z-1])
                cards.pop(z-1)

def printmatrix():
        print "\n \n \n ________________________________________________________ \n \n \n"
        for i in matrix:
                print i
        print"\n \n \n"
        print watercount

def start():
        global d
        print "Map Generation Program"
        print "Please only enter valid digits"
        print "\n \n"
        r = raw_input("Enter the number of rows: ")
        c = raw_input("Enter the number of columns: ")
        errormsg(r,c)
        matrixbuild(int(r),int(c))

def errormsg(x,y):
        try:
                x = int(x)
                y = int(y)
        except ValueError:
                print "That was not a valid choice, please start again"
                quit()

def main():
        global watercount
        addcards()
        start()
        printmatrix()
        return watercount
main()
