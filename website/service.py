from django.db import connection

from website.models import Schools, User

def getSchools(seachType, inorout, state, tuition, size, degree, gender):
    schoolsIn = Schools.objects.raw("select * from SCHOOL_INFO")
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

#def updateCollegeData():
#    data = None
#    with open(ciphertext_filename) as f:
#        data = f.readlines()
#    for line in data:
#        fields = line.split(",")
#        with connection.cursor() as cursor:
#            sql = "INSERT INTO CollegeData (name, location) VALUES ('{0}', '{1}');COMMIT;".format(fields)
#            cursor.execute(sql)
