# -*- coding: utf-8 -*-
"""python_05_for 반복문.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jGwj48_uZsnNb_93q34mPOHR0_3fJIyD

원소로 반복하기 for()
"""

my_sum = 0 # 초기화

nums = [1,2,3]

for i in nums:
    my_sum = my_sum + i

    #print(my_sum)

print(my_sum)

nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
    print(i)

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# 변수 mix 에 있는 "쌀" 개수 세어볼께요

mix = "쌀"
mix = '쌀'*100

# print(mix)

count = 0 #초기화

for i in mix:
    if i == '쌀':
        count += 1 # count = count + 1
        # print(count)


print(count)

mix = ["쌀", "보리","쌀"]


mix[1]

mix_100 = mix *100

count = 0 #초기화

for i in mix_100:
    if i == '쌀':
        count += 1 # count = count + 1
        # print(count)


print(count)

"""반복할 숫자의 범위"""

range(10)
# range(strat, end) >> [start, strat+1...., end-1]

list(range(10))

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(5):
    print("안녕")

print("자기야(너) 모해?")

for i in range(10):
    print("너 생각!")

"""구구단 9단 출력
- for - range() 활용
"""

for i in range(1,10):
    print('9 *', i,'=', 9*i)

list(range(1,10))

