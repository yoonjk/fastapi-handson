
fruits = ["apple", "banana", "cherry", "kiwi"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "kiwi", True]

print("fruits:",fruits)
print("numbers:",numbers)
print("mixed:", mixed)


print("===========================================================")

customer_list = {}
customer_array = []
customer = {"name": "kildong", "age": 20, "city": "Seoul"}
customer_list[1] = customer
customer_array.append(customer)
print(customer["name"])  # kildong
print(customer_list)
print(customer_array)

customer["email"] = "kildong@gmail.com"  # 새 항목 추가
customer["age"] = 30                     # 기존 항목 수정

print(customer)

del customer["city"]  # 키와 값을 제거
age = customer.pop("age")  # 값을 제거하고 그 값을 반환

print(customer)

customer = {"name": "soonshin", "age": 40, "city": "gyeonggi"}
customer_list[2] = customer
customer_array.append(customer)
print(customer_list)
print(customer_array)

print("===========================================================")
for key in customer.keys():
  print(key)

for value in customer.values():
  print(value)
  
for key, value in customer.items():
  print("key:{0}, value:{1}".format(key, value))
  