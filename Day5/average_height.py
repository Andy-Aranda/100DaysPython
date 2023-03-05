# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
#print(type(student_heights[1])) #lo de arriba es una cadena de strings
#print(len(student_heights))
for n in range(0, len(student_heights)): #acá los convierte a int
    student_heights[n] = int(student_heights[n])
    #print(type(student_heights[n])) acá ya todos los elementos están convertidos a int
    #print(student_heights[n])

total_height = 0
i = 0 #no usé len para contar a los estudiantes porque es una de las reglas de la clase
for height in student_heights:
    total_height += height
    i += 1
total_height = round(total_height / i)
#print(i)
print(total_height)
