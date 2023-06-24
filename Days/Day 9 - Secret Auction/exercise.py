# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "function": "A piece of code that you can easily call over and over again.",
#     "loop": "The action of doing something over and over again."
# }
#
# programming_dictionary["mug"] = "Kind of cup that it's used to drink coffee."
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#Exercise 1 - Grading Program
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)
#
# # Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#     "England": "London",
#     "Canada": "Ottawa",
# }
# #nesting dicitionary in a dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris",],"total_visits": 1},
#     "Germany": {"cities_visited": ["Heidelberg",],"total_visits": 1},
#     "England": {"cities_visited": ["London",],"total_visits": 1},
#     "USA": {"cities_visited": ["Orlando","New York","El Paso","Albuquerque","Phoenix","Silver City", "Chicago"],"total_visits": 3},
#     "Canada": {"cities_visited": ["Toronto","Niagra"],"total_visits": 1},
# }
#
# print(travel_log)
#
# #nesting dicitionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris",],
#         "total_visits": 1
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Heidelberg",],
#         "total_visits": 1
#     },
#     {
#         "country": "England",
#         "cities_visited": ["London",],
#         "total_visits": 1
#     },
#     {
#         "country": "USA",
#         "cities_visited": ["Orlando","New York","El Paso","Albuquerque","Phoenix","Silver City", "Chicago"],
#         "total_visits": 3
#     },
#     {
#         "country": "Canada",
#         "cities_visited": ["Toronto","Niagra"],
#         "total_visits": 1
#     },
# ]
# print(travel_log)

# Exercise 2 - Dictionary in List
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

def add_new_country(country,visits, cities):
    new_country = {
    }
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
