We are basically handling 3 cases:

Two triangles
For example: [0, 0, 1, 2, 3, 4, 3, 2, 1, 0]
The "triangle" is the histogram shape of 1, 2, 3, 4.
One trapezoidal and one triangle
For example: [2, 3, 4, 3, 2, 1, 0]
The "trapezoidal" is the histogram shape of 2, 3, 4
Two trapezoidals
For example: [2, 3, 4, 5, 4, 3]
Note that we modifed the problem to allow 0s so that we have less edge cases to handle. The end result is only off by 1.

Once we figured out which case we are handling, we can imagine that we are "raising" the histogram by some extra height. For example:
"Raise" [2, 3, 2, 1, 0, 0] by 1 we get [3, 4, 3, 2, 1, 0]

We use quadratic equation to solve the problem of FindExtra() (see comments in the code) and that can be called once we figure out which case we are handling.

Approach
Complexity
Time complexity:
Θ(1)\Theta(1)Θ(1)
This assumes std::sqrt() is O(1)O(1)O(1). In reality though, it is likely a Θ(log⁡N)\Theta(\log N)Θ(logN) operation. Nevertheless, it is a very fast fast builtin function.

Space complexity:
Θ(1)\Theta(1)Θ(1)

