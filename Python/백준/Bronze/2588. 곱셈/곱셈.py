num1 = int(input())
num2 = int(input())
x = num2%10
y = num2%100//10
z = num2//100
X = num1*x
Y = num1*y
Z = num1*z
print(X)
print(Y)
print(Z)
print(X+(Y*10)+(Z*100))