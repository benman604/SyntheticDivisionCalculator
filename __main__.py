import util
from synthdiv import SynthDiv

# get coeficients and convert to list of ints
coef = input("Coeficients : ").split(' ')
coef = util.strListToInt(coef)

while(True): # input loop
    opt = input('''
        [d] divide  [z] find real zeros  
        [u] upper bound [l] lower bound  
        [r] reenter coeficients [q] quit
    ''')
    
    if opt == 'r':

        # reenter coeficients
        coef = input("Coeficients : ").split(' ')
        coef = util.strListToInt(coef)

    elif opt == 'q':

        # quit
        break

    if opt == 'd': 

        # divide polynomial by (x-zero)
        zero = float(input("Zero        : "))
        synthdiv = SynthDiv(coef, zero)
        synthdiv.calc()
        synthdiv.disp()
        synthdiv.dispQuotient()

    elif opt == 'z': 
        
        # find all zeros
        # find all possible zeros with p/q
        p = util.factors(coef[len(coef) - 1])
        q = util.factors(coef[0])
        possible = []
        for i in p:
            for j in q:
                possible.append(i / j)
        possible = util.removeDuplicates(possible)
        zeros = []

        def loopTillFindZero(coeficients): # recursively test possibilities
            # use synthetic division on each possible zero
            global possible
            for i in possible:
                synthdiv = SynthDiv(coeficients, i)
                res = synthdiv.calc()
                synthdiv.disp()

                if res[len(res)-1] == 0: # i is a solution
                    res.pop() # removes 0
                    print("******* " + str(i) + " is a zero *******")
                    zeros.append(i)
                    if len(res) == 3: # its a quadratic!
                        print("Down to 2nd degree, use the quadratic formula")
                        print(str(res[0]) + "x^2 + " + str(res[1]) + "x + " + str(res[2]))
                        return res
                    else: # degree too high, keep reducing!
                        return loopTillFindZero(res)
            if len(zeros) == 0:
                print("No more real zeros")
            return None
        
        res = loopTillFindZero(coef)
        if len(coef) == 3:
            quadraticResult = util.quadraticFormula(coef[0], coef[1], coef[2])
            for i in quadraticResult:
                zeros.append(i)
            if(quadraticResult == []):
                print("No more real zeros")
        elif res != None:
            quadraticResult = util.quadraticFormula(res[0], res[1], res[2])
            for i in quadraticResult:
                zeros.append(i)
            if(quadraticResult == []):
                print("No more real zeros")
        if(len(zeros) > 0):
            zeros = util.removeDuplicates(zeros)
            print("Here are your zeros!")
            print(zeros)

    elif opt == 'l' or opt == 'u':

        # upper or lower bound
        add = 1 if opt == 'u' else -1 # number to add to add each itteration
        current = add # zero to test
        done = False
        while not done:
            synthdiv = SynthDiv(coef, current)
            res = synthdiv.calc()
            synthdiv.disp()
            if opt == 'u': # finding upper bound, all coeficients must be positave
                allpos = True
                for i in res:
                    if i < 0:
                        allpos = False
                if allpos:
                    done = True
                    print("Upper Bound x=" + str(current))
            elif opt == 'l': # finding lower bound, coeficients must have alternating signs
                if all((res[i] ^ res[i-1]) < 0 for i in range(1, len(res))):
                    done = True
                    print("Lower bound is x=" + str(current))
            current += add

