from flask import Flask, jsonify
from flask.ext.mongoalchemy import MongoAlchemy
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'hacktx'
db = MongoAlchemy(app)

class Course(db.Document):
    deptAb = db.StringField()
    deptName = db.StringField()
    courseNum = db.StringField()
    courseName = db.StringField()
    teacherName = db.StringField()

class StudyInstance(db.Document):
	building = db.StringField()
	gpsCoords = db.StringField()
	courseID = db.DocumentField(Course)
	notes = db.StringField()


@app.route('/search/dept/<ab>')
def search_dept(ab):
 	c = Course.query.filter(Course.deptAb == ab).all()
 	l = []
 	for course in c:
 		l.append([course.courseNum, course.courseName])
	return jsonify(l)

@app.route('/search/course/<num>')
def search_course(num):
 	c = Course.query.filter(Course.courseNum == num).all()
 	l = []
 	for course in c:
 		l.append([course.teacherName, ObjectId(course)])
	return jsonify(l)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)