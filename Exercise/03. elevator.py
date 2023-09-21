from math import ceil

num_of_the_people = int(input())
capacity = int(input())
courses = ceil(num_of_the_people / capacity)
print(courses)