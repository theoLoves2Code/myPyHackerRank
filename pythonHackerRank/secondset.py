# List comprhension challenge 
x,y,z,n = 1,1,2,3
#solution... first use comprehansion to generate a list of 3 by 3 matrices (new_list)
# then i use comprehension with a condition to remove those matrices that dont fit the condition 
new_list = [[opta,optb,optc] for opta in range(x+1) for optb in range(y+1) for optc in range(z+1)]
ans = [num for num in new_list if sum(num) != n ]
print(ans)  


# Find the Runner-Up Score challenge 
# I just convert the arr into a set cos they are no duplicates in a set
#next I just sort (a arr is returned) and return the second to the last element in the array
scores =  [2, 3, 6, 6, 5]
ans = sorted(set(scores))
print(ans[-2])


#Nested list challenge 
# for this challenge I am combining the techniques of sorting and comprehension
# I first ensure my values are saved in a combined list of names and scores as in var game below
# then using the sorted function with a lambda item I can re-arrange game in order of the scores 
# am now going to use a comprehension on the re-arranged game to score conditions that meet the re...
#... requirment of where the second lowest (newone[1][1]) is equal to instance num[0]
# finally using a for loop on the sorted list ans above, 
# I print out each name ...hence the ones with second lowest scores alphabetically
game = [["Harry", 37.21],["Tinas", 39.2],["Sere", 42.0],["Alice", 37.21],["Alice", 37.21],["Tina", 37.2],["Akriti", 41.0],["Harsh", 39.0]]
newone = sorted(game, key = lambda item: item[1])
ans = [num[0] for num in newone if num[1] == newone[1][1]]
for x in sorted(ans): print(x)


#Find the percentage
# given a dictionary with students and marks find the average of the student query_name to 2 decimal points
n = 3
student_marks = {
    'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60]
}
query_name = 'Malika'

solve = sum(student_marks[query_name]) / len(student_marks[query_name] )
ans = (format(solve, ".2f"))
print(ans)

