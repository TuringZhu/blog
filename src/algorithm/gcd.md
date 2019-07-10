# get greatest common divisor(GCD) by Euclidean algorithm

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Turing<qishiwenjun@163.com>
Date: 2018-07-01 09:37
Desc: 辗转相除法求最大公因式
最小公倍数: 两个数的积除以最大公因式就得到最小公倍数
GCD;the greatest common divisor
"""

def gcd(num1, num2):
    (_max, _min) = (max(num1, num2), min(num1, num2))
    if _min == 0:
        return _max
    r = _max % _min
    return gcd(_min, r)


def lcm(num1, num2):
    if num1 == 0 or 0 == num2:
        return 0
    return num1 * num2 / gcd(num2, num1)

print(gcd(60, 40))


```
