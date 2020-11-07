import pandas as pd
from DataAccessLayer import *
from Models import User
from Models import AttendanceDetail
import datetime
from tqdm import tqdm
import os
import argparse

def migrate_to_db(data):

	userDBOPS = UserCRUD()
	attendanceDBOPS = AttendanceDetailCRUD()	
	
	for i in range(len(data)):
	    name = data.loc[i]['Name']
	    email = data.loc[i]['Email']    
	    join_time = data.loc[i]['Join Time']
	    leave_time = data.loc[i]['Leave Time']
	    duration = data.loc[i]['Duration(Minutes)']
	    alternative_score = data.loc[i]['Alternative Score']
	    course_id = data.loc[i]['CourseID']	    
	    
	    user = User(name, email)
	    
	    attendance_detail = AttendanceDetail(join_time,
	                                               leave_time,
	                                               duration, 
	                                               alternative_score,
	                                               email,
	                                               course_id                                                
	                                        )
	    

	    user_db = userDBOPS.record_exists(user)	    


	    if user_db == None:
	        userDBOPS.insert_record(user)	   

	    if attendanceDBOPS.record_exists(attendance_detail) == None:
	        attendanceDBOPS.insert_record(attendance_detail)

def getFileNames(path):
	files = os.listdir(path)
	return files

def main():
	parser = argparse.ArgumentParser(description='Zoom CSV to MySQL Migration')
	parser.add_argument('--path_to_csv', default = './CSVs/', type=str, help='Path to the folder where CSV files reside')
	parser.add_argument('--CourseID', type=str, help='CourseID for the course')
	parser.add_argument('--Section', type=str, help='Section Info')
	parser.add_argument('--Schedule', type=str, help='Class Schedule')

	arguments = parser.parse_args()

	# Arguments passed in through the command line
	path_to_csv = arguments.path_to_csv
	course_id = arguments.CourseID
	section = arguments.Section
	schedule = arguments.Schedule

	csv_files = getFileNames(path_to_csv)

	for i in csv_files:
		file_path = path_to_csv[:-1] + '/' + i
		print(file_path)	

		data = pd.read_csv(file_path)

		data['Name'] = data.Name.str.split(" ").str[::-1].str.join(" ")
		data['Join Time'] = pd.to_datetime(data['Join Time'], format='%m/%d/%Y %H:%M')
		data['Leave Time'] = pd.to_datetime(data['Leave Time'], format='%m/%d/%Y %H:%M')
		data['Alternative Score'] = data['Alternative Score'].fillna(-1)
		data['CourseID'] = course_id

		courseInfoDBOPS = CourseInfoCRUD()

		course_info = CourseInfo(course_id, section, schedule)

		if courseInfoDBOPS.record_exists(course_info) == None:
			courseInfoDBOPS.insert_record(course_info)

		migrate_to_db(data)

	print('Succesfully migrated all data to the MySQL Database.')

if __name__ == '__main__':
    main()



