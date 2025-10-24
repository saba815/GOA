'''Tuple — ეს არის შეკრული მონაცემების წყობა რომელიც შეცვლადი არ არის (immutable).

List — ესეც მონაცემების წყობაა, მაგრამ შეცვლადია (mutable).'''


my_tuple = ("ლეპტოპი", "მონიტორი", "მაუში", "კლავიატურა", "პრინტერი")

item1, item2, item3, item4, item5 = my_tuple


print(item1)  
print(item2) 
print(item3)  
print(item4) 
print(item5)  


my_tuple2 = ("ლეპტოპი", "მონიტორი", "მაუში", "ლეპტოპი", "პრინტერი", "მაუში")


print(my_tuple2.index("მაუში")) 


print(my_tuple2.count("ლეპტოპი"))  

