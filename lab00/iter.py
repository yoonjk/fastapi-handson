stars = {
  "star1" : "Neutron",
  "star2" : "Leo",
  "Star3" : "Vega",
  "Star4" : "Rigel"
}

for item in stars:
  print(item)

print("====================")
# key, value
for (key, val) in stars.items():
  print(key, val)
  
for i in range(len(stars)):
  print(i)