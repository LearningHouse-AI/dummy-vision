# --- Simple Class yang mungkin tidak dipakai ----
# class myClass :
#     x = 5

# p1 = myClass()
# print(p1.x)

# Simple Class dengan function
class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

val = person("Any", 20)

print(val.name)
print(val.age)

