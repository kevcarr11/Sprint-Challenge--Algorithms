#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
this snippet has a O(n) runtime because as we increase the value of n
the while loop will have to loop n more times. The speed of the algorithm will increase at the same rate as n. 


b) O(2^n)
this snippet has a O(2^n) runtime because for an input size of n, we have to print n * n times or 2^n times.


c) O(n)
this snippet also has a runtime of O(n) because this function will recurse bunnies amount of times until bunnies is equal to 0.
as bunnies grow the recursion increases at an linear ratio 

## Exercise II
Go to the middle floor of the building and drop an egg
if egg breaks, go down one floor at a time and drop egg until egg doesn't break then return that floor
if egg does not break, go up one floor at a time and drop egg until egg does break then return that floor
if we reach the top of building and egg never broke then the building is not tall enough to break egg 

runtime complexity of this solution would be O(n log n) because as the size of the input increases, the runtime will grow at a slightly faster rate; this solution is usable, but might not be ideal

