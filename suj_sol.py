import random

ref_list = ["A", "B", "C", "D", "E"]
list = ["A", "B", "C", "D", "E"]

test_num = int(input("How many tests would you like to perform?"))
ref = 0
for i in range(0,test_num):
    random.shuffle(list)
    print(list)
    if list != ref_list:
        ref = ref + 1
print("There were",ref," uniquely random combinations.")
