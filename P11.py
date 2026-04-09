#tyler nguyen

from datetime import datetime

print("Program started at", datetime.now())

infile = open("C:/temp/P11/points.txt", "r")
gradefile = open("C:/temp/P11/grades.txt", "w")
errorfile = open("C:/temp/P11/error.txt", "w")

line = infile.readline()

records = 0
graded = 0
errors = 0

countA = 0
countB = 0
countC = 0
countD = 0
countF = 0

while line != "":
    records = records + 1

    parts = line.strip().split(",")

    idnum = parts[0]
    name = parts[1]
    pts = parts[2]

    try:
        points = int(pts)

        if points < 0:
            errorfile.write(idnum + "," + name + "," + pts + ",Points can not be negative\n")
            errors = errors + 1

        elif points > 1000:
            errorfile.write(idnum + "," + name + "," + pts + ",Points exceed maximum\n")
            errors = errors + 1

        else:

            percent = points / 1000 * 100

            if percent >= 90:
                grade = "A"
                countA = countA + 1
            elif percent >= 80:
                grade = "B"
                countB = countB + 1
            elif percent >= 70:
                grade = "C"
                countC = countC + 1
            elif percent >= 60:
                grade = "D"
                countD = countD + 1
            else:
                grade = "F"
                countF = countF + 1

            gradefile.write(idnum + "," + name + "," + str(points) + "," + grade + "\n")
            graded = graded + 1

    except:
        errorfile.write(idnum + "," + name + "," + pts + ",Points must be numeric\n")
        errors = errors + 1

    line = infile.readline()

infile.close()
gradefile.close()
errorfile.close()

print("Number of records read:", records)
print("Number of A's:", countA)
print("Number of B's:", countB)
print("Number of C's:", countC)
print("Number of D's:", countD)
print("Number of F's:", countF)
print("Number of graded records:", graded)
print("Number of error records:", errors)

print("Program ended at", datetime.now())
