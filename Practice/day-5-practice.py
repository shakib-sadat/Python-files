# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# # total_height = 0
# # for height in student_heights:
# #     total_height += height

# # num_student = 0
# # for student in student_heights:
# #     num_student += 1

# # total_average = round(total_height/num_student)
# # print(total_average)

# total_height = sum(student_heights)
# total_student = len(student_heights)
# average = round(total_height/total_student)
# print(average)

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# heighest_score = 0
# for score in student_scores:
#     if score > heighest_score:
#         heighest_score = score
# print(f"The highest score is: {heighest_score}")

# # heighest_score = max(student_scores)
# # print(heighest_score)

# total = 0
# for even in range(2, 101, 2):
#     total += even
# print(total)

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz.")
    elif number % 3 == 0:
        print("Fizz.")
    elif number % 5 == 0:
        print("Buzz.")
    else:
        print(number)
