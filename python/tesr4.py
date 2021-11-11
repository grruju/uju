'''
1번
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
'''
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print("1번문제 :",result)


# 2. 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합
'''
피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?
'''
result = 0
num1 = 0
num2 = 1
num3 = num1 + num2
while num3 <= 4000000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 % 2 == 0:
        result += num3
print("2번문제 :",result)