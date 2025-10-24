students = ["ნინო", "გიორგი", "მარიამი", "ლაშა", "ანა"]


students.append("დავით")
print("დამატების შემდეგ:", students)


students.pop()  
print("pop()-ის შემდეგ:", students)


print("სიის სიგრძე არის:", len(students))


index = students.index("მარიამი")
print("მარიამი არის ინდექსზე:", index)


students.append("ანა")
print("ანა მეორდება:", students.count("ანა"))

