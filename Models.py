import datetime

class User:
    name : str
    email : str

    def __init__(self, name, email):
        self.name = name
        self.email = email    

    def __eq__(self, obj):
        if (isinstance(obj, User) and obj.name == self.name and obj.email == self.email):
            return True
        else:
            return False

    def __str__(self):
        return str(self.name) + " " + str(self.email)
        
class AttendanceDetail:   
    join_time : datetime.date
    leave_time: datetime.date
    duration : int
    alternative_score : int
    email : str  
    course_id : str  

    def __init__(self, join_time, leave_time, duration, alternative_score, email, course_id):
        self.join_time = join_time
        self.leave_time = leave_time
        self.duration = duration
        self.alternative_score = alternative_score
        self.email = email        
        self.course_id = course_id

    def __eq__(self, obj):
        if (isinstance(obj, AttendanceDetail) and obj.join_time == self.join_time
            and obj.leave_time == self.leave_time
            and obj.duration == self.duration
            and obj.alternative_score == self.alternative_score
            and obj.email == self.email
            and obj.course_id == self.course_id):           
            return True
        else:
            return False

    def __str__(self):
        return str(self.join_time) + " " + str(self.leave_time) + " " + str(self.duration) + " " + str(self.alternative_score) + " " + str(self.email) + " " + str(self.course_id)

class CourseInfo:
    course_id : str
    section : str
    schedule : str

    def __init__(self, course_id, section, schedule):
        self.course_id = course_id
        self.section = section
        self.schedule = schedule

    def __eq__(self, obj):
        if (isinstance(obj, CourseInfo) and obj.course_id == self.course_id
            and obj.schedule == self.schedule
            and obj.section == self.section):     
            return True
        else:
            return False


class DBConfiguration:
    host : str
    username : str
    database : str
    password : str

    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password