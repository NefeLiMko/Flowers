#n = 24
#m1 = 7; n = 17
#m2 = 
#
def fib( n, cur = 4, is_main = True):
    if len(str(cur))<n:
        cur = fib(cur - 1) + fib(cur - 2)
        return fib(n, cur, is_main=True) 
    return cur




#def game(n):
    #max_first_move = n\3 - 1


#game(n=69)

print(fib(10))