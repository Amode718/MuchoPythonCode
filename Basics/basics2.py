x = 10
y = "10"

sum1 = x + x
sum2 = y + y
# clearprint(sum1, sum2)

monday_temp = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1,
                 "Sim": 8.8,
                 "John": 7.5}

mySum = sum(monday_temp)
length = len(monday_temp)
mean = mySum / length
summing = sum(student_grades.values())
len_of_grades = len(student_grades)
meann = summing / len_of_grades
print(mean)
print(meann)

def of_mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(of_mean([1,2,3,4]))

