squares = [i**2 for i in range(1, 11)] 

evens = [i for i in range(1, 11) if i % 2 == 0]

fruits_upper = [i.upper() for i in ["apple","banana","cherry","date"]]

lengths = [len(i) for i in ["cat","dog","elephant","mouse"]]

greater_than_10 = [i for i in [5,12,8,20,3,15] if i > 10]

times_five = [i * 5 for i in [1,2,3,4]]

words = ["hello", "world", "python", "programming", "list"]

p_words = [i for i in words if i[0] == 'p']