"""

Happy number is a number which eventually leads to 1 after repeatedly replacing it with the sum of the square of its digits.

at first thought it was simple recursion, but it's not. 

think about the example. 

1 9 1

1 + 81 + 1 = 83
8*8 + 3*3 = 64 + 9 = 73
7*7 + 3*3 = 49 + 9 = 58
5*5 + 8*8 = 25 + 64 = 89
8*8 + 9*9 = 64 + 81 = 145
1*1 + 4*4 + 5*5 = 1 + 16 + 25 = 42
4*4 + 2*2 = 16 + 4 = 20
2*2 + 0*0 = 4 + 0 = 4
4*4 + 0*0 = 16 + 0 = 16
1*1 + 6*6 = 1 + 36 = 37
3*3 + 7*7 = 9 + 49 = 58
5*5 + 8*8 = 25 + 64 = 89
8*8 + 9*9 = 64 + 81 = 145
1*1 + 4*4 + 5*5 = 1 + 16 + 25 = 42
4*4 + 2*2 = 16 + 4 = 20
2*2 + 0*0 = 4 + 0 = 4
4*4 + 0*0 = 16 + 0 = 16
1*1 + 6*6 = 1 + 36 = 37
...


this loops forever. 

now, we use set to check if the number was already derived or not. 


1. while the number is not in the set, 
2. add the number to the set. 
3. stringy the number
4. do the calculations
5. if the number is 1, return True
6. if it breaks the loop, that means it has duplicated. so, return false. 

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        

        s = set()

        while n not in s:
            s.add(n) # add the number to the set
            x = 0
            for i in str(n):
                x += int(i) ** 2
            
            n = x
            if n == 1: return True

        return False






