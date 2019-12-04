from django.db import connection
from django.contrib.auth.hashers import make_password

from website.models import Schools, User

def getSchools(seachType, inorout, state, tuition, size, degree, gender):
    
    query = "SELECT * FROM CollegeData WHERE "
    if(state != "--"):
        query += "state = '{0}' ".format(state)
    else:
        query += "state <> '{0}' ".format("ZZ")
    
    if(inorout == "0"):
        query += "AND tuitionInState < {0} ".format(tuition)
    elif(inorout == "1"):
        query += "AND tuitionOutState < {0} ".format(tuition)
    
    query += "AND size < {0} ".format(size)

    if(degree == "1"):
        query += "AND highestDegree = 1 "
    elif(degree == "2"):
        query += "AND highestDegree = 2 "
    elif(degree == "3"):
        query += "AND highestDegree = 3 "
    elif(degree == "4"):
        query += "AND highestDegree = 4 "

    if(gender == "0"):
        query += "AND menOnly = 1 AND womenOnly = 0"
    elif(gender == "1"):
        query += "AND menOnly = 0 AND womenOnly = 1"
    
    
    schoolsIn = Schools.objects.raw(query)
    #schoolsOut = Schools.objects.raw("select CollegeName, State, URL, TuitionOutState, Size, averageACT from SCHOOL_INFO")
    return list(schoolsIn)

def getUsers():
    users = User.objects.raw("select * from users")
    return list(users)

def updateSchoolName():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE CollegeData SET name = 'U of SQL' WHERE id = 100663;COMMIT;") 
        cursor.execute("Select * from CollegeData LIMIT 10;COMMIT;")
        row = cursor.fetchall() 
    return "test"

def restoreSchoolName():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE CollegeData SET name = 'University of Alabama at Birmingham' WHERE id = 100663;COMMIT;")
    return "test"

def registerUser(first_name, last_name, email, password):
    passwordHash = make_password(password, salt=None, hasher="sha1")
    print(len(passwordHash))
    print(passwordHash)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users (first_name, last_name, email, passwordHash) VALUES ('{0}', '{1}', '{2}', '{3}')".format(first_name, last_name, email, passwordHash))
    users = User.objects.raw("select * from users where email='{0}'".format(email))
    user = list(users)[0]
    return user

def loginUser(email, password):
    users = User.objects.raw("select * from users where email='{0}'".format(email))
    user = list(users)[0]
    return user

def getUser(id):
    users = User.objects.raw("select * from users where id='{0}'".format(id))
    user = list(users)[0]
    return user
#def updateCollegeData():
#    data = None
#    with open(ciphertext_filename) as f:
#        data = f.readlines()
#    for line in data:
#        fields = line.split(",")
#        with connection.cursor() as cursor:
#            sql = "INSERT INTO CollegeData (name, location) VALUES ('{0}', '{1}');COMMIT;".format(fields)
#            cursor.execute(sql)
