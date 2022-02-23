'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여
li 안에 있는 정수가 li2에도 담겨 있다면 그 정수를 배제하세요.
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해 보세요.
'''
from unittest import result


li = [1, 2, 3, 4, 5, 6, 7]
li2 = [1, 3, 8, 4, 5, 7, 101]
'''
# 내풀이**
A = set(li)
B = set(li2)
print(A)
print(B)

C=(A&B)
print(C)
list = (A-C) | (B-C)
print('서로 겹치지 않는 정수만 담긴 새로운 리스트 : ',list)
'''

'''
집합연산자 모를경우의 풀이
li3 = []
for n in li:
  if n not in li2:
    li3.append(n)

for n in li2:
  if n not in li:
    li3.append(n)

print(li3)
'''
result = set(li) ^ set(li2)
print(result)
