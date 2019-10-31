from django.db import connection

from website.models import Schools, User

def getSchools():
    schools = Schools.objects.raw("select CollegeID, CollegeName from SCHOOL_INFO")
    return list(schools)

def getUsers():
    users = User.objects.raw("select * from users")
    return list(users)

#def updateCollegeData():
#    data = None
#    with open(ciphertext_filename) as f:
#        data = f.readlines()
#    for line in data:
#        fields = line.split(",")
#        with connection.cursor() as cursor:
#            sql = "INSERT INTO CollegeData (name, location) VALUES ('{0}', '{1}');COMMIT;".format(fields)
#            cursor.execute(sql)
