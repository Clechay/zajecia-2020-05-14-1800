import psycopg2
import random
print("yay")
conn = psycopg2.connect("dbname=mydb user=postgres password=pass") # to samo hasło które wybieraliśmy przy instalacji
cur = conn.cursor()

def randomStudent():
    firstname = random.choice(['Marek', 'Darek', 'Jacek', 'Antoni', 'Piotr'])
    lastname = random.choice(['Kwiatkowski','Kowalski','Malysz','Kubica','Gates'])
    avg = random.randrange(2,6)
    nr = random.randint(1000,9999)
    class_name = random.choice(['1c'])
    return (nr, firstname+' '+lastname, class_name, avg)

print(randomStudent())

def addRandomStudend():
    student = randomStudent()
    cur.execute("INSERT INTO uczniowie VALUES (%s, %s, %s, %s);", student)
    conn.commit()

def addManyStudents():
    for i in range(30):
        addRandomStudend()
# addManyStudents()
def printStudents():
    print(cur.execute("SELECT * FROM uczniowie;"))
    rows = cur.fetchall()
    print(rows)

def initClasses():
    cur.execute("INSERT INTO klasy VALUES ('1a',101,'Kwiatkowski');")
    cur.execute("INSERT INTO klasy VALUES ('1b',100,'Kowalski');")
    cur.execute("INSERT INTO klasy VALUES ('1c',101,'Kwiatkowski');")

def studentsInRoom(room):
    cur.execute("SELECT uczniowie.name FROM uczniowie , klasy WHERE uczniowie.class = klasy.name AND klasy.room = "+str(room)+";")
    rows = cur.fetchall()
    print(rows)

def studentsByTeacher(teacher):
    cur.execute("SELECT uczniowie.name FROM uczniowie , klasy WHERE uczniowie.class = klasy.name AND klasy.teacher = '"+str(teacher)+"';")
    rows = cur.fetchall()
    print(rows)
# studentsByTeacher('Kwiatkowski')

# initClasses()
conn.commit()
cur.close()
conn.close()
print("all done")