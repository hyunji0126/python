# 모듈 내에 존재하는 변수, 함수 , 클래스를 직접 임포트하는 방법
from math import factorial, gcd
# import math

print(factorial(6))
print(factorial(5))

print(gcd(12,18))

import statistics

li = [34,55,12,33,55,66,99]
print('평균 : ', statistics.mean(li))
print('분산 : ', statistics.variance(li))
print('표준편차 : ', statistics.stdev(li))

# 위에서 알려드린 두 가지 개념을 합쳐서도 사용이 가능합니다.
from math import factorial as fac

print(fac(10))






