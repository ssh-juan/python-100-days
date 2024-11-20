#Challenge 1
#Check the highest score via the 'for loop'

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
sum_scores = 0

for score in student_scores:
    sum_scores += score         #suming via a 'for loop', instead of using sum() function (just to practice)
    if score > highest_score:
        highest_score = score   #setting highest

print(f"The sum of the scores is {sum_scores}")
print(f"The highest score is {highest_score}")