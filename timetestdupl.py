# Usage:
# Default params: python timetestdupl.py
# Any combination of following options is allowed
#
# Change number of items in list. Default is 1000000: python timetestdupl.py -i 10
# Change number of times the benchmark runs. Default is 1000000 / number_of_items : python timetestdupl.py -t 10
# Change mininum integer in list. Default is 1: python timetestdupl.py -n -1
# Change maximum integer in list. Default is number_of_items/2: python timetestdupl.py -x 100000
# Display the original and sorted array. Defalt - only if it's small: python timetestdupl.py -d
# Test all algorithms. Defalt - only if the test case is small: python timetestdupl.py -a
import testdupl
from random import randint
import timeit
import sys, getopt
def timealg(alg, arr, number):
    print( timeit.timeit( alg +"("+str(arr)+")", setup="from testdupl import "+ alg, number=number) )

def testalg(alg, arr):
    methodToCall = getattr(testdupl, alg)
    res = methodToCall(arr)
    print res

def main(argv):
    itemCount = number = maxInt = minInt = displayLists = allAlgs = None
    
    opts, args = getopt.getopt(argv,'i:t:n:x:d')
    for opt, arg in opts:
        if opt == '-i':
            itemCount = int(arg)
        elif opt == '-t':
            number = int(arg)
        elif opt == '-n':
            minInt = int(arg)
        elif opt == '-x':
            maxInt = int(arg)
        elif opt == '-d':
            displayLists = True
        elif opt == '-a':
            allAlgs = True
            
    # defaults
    if itemCount == None:
        itemCount = 1000000
    if number == None:
        number = 1000000 / itemCount
    if minInt == None:
        minInt = 1
    if maxInt == None:
        maxInt = itemCount / 2
    if displayLists == None:
        displayLists = itemCount < 100
    if allAlgs == None:
        allAlgs = itemCount < 500
        
    if minInt >= maxInt:
        print "Change the range.", minInt, maxInt
    
    arr = []
        
    for i in xrange(itemCount):
        arr.append(randint(minInt, maxInt) )    
    if displayLists:
        print "Generated list:", arr    
    if allAlgs:
        algs = ['dupl_eat', 'dupl_utdemir', 'dupl_lthaulow', 'dupl_pmcguire', 'dupl_ivazques_abrams', 'dupl_rbespal']
    else: # with more than 1000 some algorithms are slow
        algs = ['dupl_pmcguire', 'dupl_ivazques_abrams', 'dupl_rbespal']
    
    for alg in algs:
        print "Algorithm:", alg
        if displayLists:            
            print "Sorted:",
            testalg(alg,arr)
            
        print "Timing:",
        timealg(alg, arr, number)        
        print '#'*20        
            
if __name__ == "__main__":
   main(sys.argv[1:])