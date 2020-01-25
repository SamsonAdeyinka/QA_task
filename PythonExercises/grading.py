def StudentName():
    Firstname = str(input("Fristname?: "))
    Lastname = str(input("Lastname?: "))                
    name = Firstname + " " + Lastname
    return name

def Homework():
    hw = int(input("Homework Score?: "))
    return hw

def Assessment():
    assess = int(input("Assessment Score?: "))
    return assess

def Exam():
    exam = int(input("Exam score?: "))
    return exam

def Grade(x, y, z):
    total = ((x + y + z) / 175)*100
    return total

#------------------------------------------------
name = StudentName()
hw = Homework()
assess = Assessment()
exam = Exam()



print("Overall Percentage: ",Grade(hw, assess, exam))

#total = hw + assess + exam
#average = total / 3
#print(total)


