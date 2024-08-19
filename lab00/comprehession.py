employees = [
  {"이름": "Bryan", "연봉": 1000000, "성별": "남"},
  {"이름": "Sally", "연봉": 5000000, "성별": "여"}, 
  {"이름": "Chris", "연봉": 4000000, "성별": "남"},
  {"이름": "Susan", "연봉": 5000000, "성별": "여"},
  {"이름": "Jimmy", "연봉": 9000000, "성별": "남"}
]

def ismale(emp):
  return emp['성별'] == '남' 

male = filter(ismale, employees)

print('성별', list(male))

female = [ emp for emp in employees if emp['성별'] == '여']

print(female)
print("===================")

male_employees = {emp['이름'] : emp['연봉'] for emp in employees if emp['성별'] == '남'}

print(male_employees)
print("===================")

money = [[emp['이름'], '돈많음'] if emp['연봉'] > 4000000 else [emp['이름'], '돈적음'] for emp in employees ]

print(money)