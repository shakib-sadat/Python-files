# user_f_name = input("Enter you first name.")
# user_l_name = input("Enter you last name.")


def format_name(f_name, l_name):
    """Take a first name and last name and format it to title case."""  # doc string, function documentation
    if f_name == "" or l_name == "":
        return "Please type valid inputs."
    fomatted_f_name = f_name.title()
    fomatted_l_name = l_name.title()
    return f"{fomatted_f_name} {fomatted_l_name}"


print(format_name(input("Enter you first name."), input("Enter you last name.")))

# print(f_name.title() + " " + l_name.title())

# format_name(f_name=user_f_name, l_name=user_l_name)


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year == True:
# if is_leap(year) and month == 2:
# leap_month = month_days[1] = 29
# return leap_month
#     return 29
# return month_days[month-1]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
