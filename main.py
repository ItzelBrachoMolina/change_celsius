
#nested lists with list comprehension

with open("file1.txt") as file1:
     file_1_data=file1.readlines()

 with open("file2.txt") as file2:
     file_2_data = file2.readlines()


result=[int(x) for x in file_1_data if x in file_2_data]
print(result)


#print(new_list)

#dictionary comprehension


import random
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

students_scores={student:random.randint(1,100) for student in names}
print(students_scores)

passed_students={k:v for (k,v) in students_scores.items() if v>60}
print(passed_students)


#List comprehension with a string

sentence="What is the airspeed velocity of an unladen swallow?"
sentence_list=sentence.split()
print(sentence_list)

result={numbers:len(numbers) for numbers in sentence_list}
print(result)


#Celsius to Farenheith

weather_c={
      "Monday":12,
      "Tuesday":14,
      "Wednesday":15,
      "Thursday":14,
      "Friday":21,
      "Saturday":22,
      "Sunday":24,
}

weather_f={k:(v*9/5)+32 for (k,v) in weather_c.items()}
print(weather_f)