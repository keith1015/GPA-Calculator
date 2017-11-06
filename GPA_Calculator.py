course_credits = {
"CMPSC 122" : 3
}
course_grade = {
"CMPSC 122" : "A"
}

x = 0

y = [] # number of credits attempted
z = [] # number of points earned

for key1 in course_credits:
	for key2 in course_grade:
		if key1 == key2:
			a = course_credits[key1]
			b = course_grade[key2]
			#print(key1, a)
			#print(key2, b)
			if b == "A":
				x = 4.00 * a
				y.append(a)
				z.append(x)
			elif b == "A-":
				x = 3.67 * a
				y.append(a)
				z.append(x)
			elif b == "B+":
				x = 3.33 * a
				y.append(a)
				z.append(x)
			elif b == "B":
				x = 3.00 * a
				y.append(a)
				z.append(x)
			elif b == "B-":
				x = 2.67 * a
				y.append(a)
				z.append(x)
			elif b == "C+":
				x = 2.33 * a
				y.append(a)
				z.append(x)
			elif b == "C":
				x = 2.00 * a
				y.append(a)
				z.append(x)
			elif b == "D":
				x = 1.00 * a
				y.append(a)
				z.append(x)
			elif b == "F":
				x = 0.00 * a
				y.append(a)
				z.append(x)

#print(y)
#print(z)

y1 = sum(y)
z1 = sum(z)

GPA = z1 / y1

print(GPA)