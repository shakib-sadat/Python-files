# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# "Loop": "The action of doing something over and over again.",
# }
# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# empty_dictionary = {}

# programming_dictionary = {}

# programming_dictionary["Bug"] = "A moth in your device."

# # print(programming_dictionary)

# for (key) in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for (key) in student_scores:
#     if student_scores[key] > 90 and student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
# print(key)
# print(student_scores[key])
#     if student_scores[key] > 80 and student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     if student_scores[key] > 70 and student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     if student_scores[key] <= 70:
#         student_grades[key] = "Fail"

# print(student_grades)

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Munich"], "total_visits": 16},
# }

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Munich"],
#         "total_visits": 16
#     },
# ]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_new, visits_new, cities_new):
    new_dic = {}
    new_dic["country"] = country_new
    new_dic["visits"] = visits_new
    new_dic["cities"] = cities_new
    travel_log.append(new_dic)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
