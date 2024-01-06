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

// Returns the area of a trapezoidal with length h and h - l + 1 and height l.
int64_t S(int64_t h, int64_t l) {
  return (2 * h - l + 1) * l / 2;
}

// Returns the max n such that the sum of arithemetic sequence:
//   * started as `start`
//   * with `increment`
//   * in total n items
//   * the sum does not exceed `max_sum`
int FindExtra(int start, int increment, int max_sum) {
  // (start * 2 + (n - 1) * increment) * n / 2 <= max_sum
  int64_t b = start * 2 / increment - 1;  // increment is 1 or 2 so it always divides fine.
  int64_t c = 2 * max_sum / increment;
  // Now we have n^2 + bn <= c
  
  int64_t d = std::sqrt(b * b + 4 * c);
  int n = (d - b) / 2;
  return n;
}

class Solution {
public:
  int maxValue(int n, int index, int maxSum) {
    maxSum -= n;  // Now nums[i] can be 0. We just need to add 1 at the end.
    int left = index + 1;
    int right = n - index;
    auto [small, large] = std::minmax(left, right);
    
    const int64_t A = S(large, large) + S(large, small) - large;
    if (maxSum >= A) {
      // This is the case of two trapezoidal.
      // When we "raise" them the sum increases by a constant
      // factor `n`.
      return large + (maxSum - A) / n + 1;
    }
    const int64_t B = S(small, small) * 2 - small;
    if (maxSum >= B) {
      // This is the case of One Trapezoidal + One Triangle.
      // When we "raise" them the sum increases by a arithemtic
      // sequence of common difference 1.
      return small + FindExtra(small * 2, 1, maxSum - B) + 1;
    }
    // This is the case of two triangles.
    // When we "raise" them the sum increases by a arithemtic
    // sequence of common difference 2.
    return FindExtra(1, 2, maxSum) + 1;
  }
};

Approach
Complexity
Time complexity:
Θ(1)\Theta(1)Θ(1)
This assumes std::sqrt() is O(1)O(1)O(1). In reality though, it is likely a Θ(log⁡N)\Theta(\log N)Θ(logN) operation. Nevertheless, it is a very fast fast builtin function.

Space complexity:
Θ(1)\Theta(1)Θ(1)


code running explain:
ms = 6 index = 2 n = 4 Ans = 2
max_sum = max_sum - n  => 2

left = index + 1 => 3

right = n - index => 2

small = min(left, right) = > (3, 2) => 2
large = max(left, right) = > (3, 2) => 3

A = S(large, large) + S(large, small) - large => S(3, 3) + S(3, 2) - 3

S(3, 3) => (2 * 3 - 3 + 1) * 3 /2 => 4 * 3 / 2 = > 6
S(3, 2) => (2 * 3 - 2 + 1) * 2 /2 => 10/2 => 5

A = 6 + 5 - 3 = 8

if ms > = A => 6>=8 Fails

B = S(small, small) * 2 -small = S(2, 2) * 2 - small
S(2, 2) => (2 * 2 - 2 + 1) * 2/2 => 6/2 => 3

B = 3 * 2 - 2 = 4

if ms > = B => 6>=4 Pass
return small + FindExtra(small * 2, 1, max_sum - B) + 1 => 2 + FindExtra (3 * 2, 1, 6 - 4)

FindExtra(6, 1, 2)
=> b = 6 * 2 // 1 - 1 = 11
c = 2 * 2 // 1 = 4
d = sqrt(11 * 11 + 4 * 4) = 11.704
n = (11.704 - 11) // 2 = 0.704//2 = 0.0 (floor division will round to nearest number)

return 2+0 = 2 

I hate this!

