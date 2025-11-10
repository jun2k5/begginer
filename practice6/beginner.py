

name = "Alice"
age = 25
is_student = True
print()
print()

print(10 + 5)  # 15
print(10 > 5)  # True
print(True and False)  # False
print()
print()

num = 10
if num > 0:
  print("양수입니다.")
elif num < 0:
  print("음수입니다.")
else:
  print("0입니다.")
print()
print()

for i in range(1, 4):
  print("반복 중:", i)
print()
print()

count = 0
while count < 3:
  print("while 반복 중:", count)
  count += 1
print()
print()


def greet(name):
  return "안녕, " + name + "!"


print(greet("Alice"))
