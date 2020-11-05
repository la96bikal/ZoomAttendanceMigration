import pymysql
from Models import *
import json

def read_connection_string():
	with open('Config.json') as config_file:
		data = json.load(config_file)
	return DBConfiguration(data["host"], data["Database"], data["User"], data["Password"])


def execute_query(sql_query):
	configuration = read_connection_string()
	conn = pymysql.connect(host = configuration.host, user = configuration.username, passwd = configuration.password, db = configuration.database)
	myCursor = conn.cursor()    
	myCursor.execute(sql_query)
	conn.commit()
	conn.close()

def fetch_record(sql_query):
	configuration = read_connection_string()
	conn = pymysql.connect(host = configuration.host, user = configuration.username, passwd = configuration.password, db = configuration.database)
	myCursor = conn.cursor()    
	myCursor.execute(sql_query)    
	conn.commit()    
	conn.close()
	row = myCursor.fetchone()
	return row

class UserCRUD:
	def insert_record(self, user):        	        
	    sql_query = f"INSERT INTO zoomuser(Name, Email) VALUES('{user.name}', '{user.email}') ;"        
	    return execute_query(sql_query)    


	def record_exists(self, user):		
		sql_query = f"SELECT * FROM `zoomuser` WHERE email = '{user.email}';"
		user_row = fetch_record(sql_query)
		if user_row == None:
			return None
		else:
			return User(*user_row)

class AttendanceDetailCRUD:
	def insert_record(self, attendanceDetail):        
	    sql_query = "INSERT INTO attendancedetail(AlternativeScore, Duration, Email, JoinTime, LeaveTime) VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(attendanceDetail.alternative_score,attendanceDetail.duration, attendanceDetail.email, attendanceDetail.join_time,attendanceDetail.leave_time)        
	    return execute_query(sql_query)

	def record_exists(self, attendance_detail):
	    sql_query = f"SELECT * FROM `attendancedetail` WHERE Email = '{attendance_detail.email}' AND Duration = {attendance_detail.duration} AND JoinTime = '{attendance_detail.join_time}' AND LeaveTime = '{attendance_detail.leave_time}' AND AlternativeScore = {attendance_detail.alternative_score};"	    
	    attendance_row = fetch_record(sql_query)
	    if attendance_row == None:
	        return None
	    else:
	        return AttendanceDetail(*attendance_row[:-1])