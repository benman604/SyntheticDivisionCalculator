An old program from back when I was in Precalc to factor, divide, and find upper and lower bounds to a polynomial.

## Usage
Enter the coeficients of a polynomial like so
```
5 2 0 1
```
This is the equivalent of $5x^3 + 2x^2 + 1$

Sample output:
```
Coeficients : 2 1 0 0 -2 -1

        [d] divide  [z] find real zeros  
        [u] upper bound [l] lower bound  
        [r] reenter coeficients [q] quit
    z
---  -  -  -  -  --  --
1.0  2  1  0  0  -2  -1
        2  3  3   3   1
     2  3  3  3   1   0
---  -  -  -  -  --  --

******* 1.0 is a zero *******
---  -  -  -  --  --
1.0  2  3  3   3   1
        2  5   8  11
     2  5  8  11  12
---  -  -  -  --  --

---  -  -  -  ---  ----
0.5  2  3  3  3    1
        1  2  2.5  2.75
     2  4  5  5.5  3.75
---  -  -  -  ---  ----

----  -  --  --  --  --
-1.0  2   3   3   3   1
         -2  -1  -2  -1
      2   1   2   1   0
----  -  --  --  --  --

******* -1.0 is a zero *******
---  -  -  -  -
1.0  2  1  2  1
        2  3  5
     2  3  5  6
---  -  -  -  -

---  -  -  -  ---
0.5  2  1  2  1
        1  1  1.5
     2  2  3  2.5
---  -  -  -  ---

----  -  --  -  --
-1.0  2   1  2   1
         -2  1  -3
      2  -1  3  -2
----  -  --  -  --

----  -  --  --  --
-0.5  2   1   2   1
         -1  -0  -1
      2   0   2   0
----  -  --  --  --

******* -0.5 is a zero *******
Down to 2nd degree, use the quadratic formula
2x^2 + 0.0x + 2.0
No more real zeros
Here are your zeros!
[1.0, -1.0, -0.5]
```