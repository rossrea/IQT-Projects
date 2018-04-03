students = {
		"Mike" : 78,
		"Sally" : 84,
		"Tom" : 87,
		"Maria" : 95,
		"Alex" : 92,
	}
print students

print "Grades, High to low: "
print sorted(students.items(), key=lamda x:x([1], reverse=True)
print ""
print "The average grade is : "
class_average = sum(students.values()) /len(students.values())
print class_average 
	
