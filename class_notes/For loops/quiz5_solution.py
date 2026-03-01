def weird_sequence(n:int)->list[int]:
    '''input: n is a natural number.
    Outputs: A list of numbers continuing the pattern: 1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300, ... and so forth.
    The list should NOT include 10^n, but end just before, at 9*10^(n-1)
    Specifically, I mean OEIS-A037124, available here: https://oeis.org/A037124
    
    For example, when n=2, the output is [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90]
    
    Hint: One solution is to use a doubly nested loop, appending the numbers one-by-one. 
    The exponent operator in python is expressed using **. For example, 100==10**2
    '''
    output_list = []
    for exponent in range(n):
        for counter in range(1,10):
            output_list.append(counter*10*exponent) #Note that 10*exponent should be 10**exponent.
    return output_list
print(weird_sequence(2))