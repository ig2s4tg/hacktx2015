from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy


app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'hacktx'
db = MongoAlchemy(app)

class Course(db.Document):
    deptName = db.StringField()
    courseNum = db.StringField()
    courseNum = db.StringField()
    teacherName = db.StringField()

class StudyInstance(db.Document):
	building = db.StringField()
	gpsCoords = db.StringField()
	courseID = db.DocumentField(Course)
	notes = db.StringField()




if __name__ == '__main__':
    app.run(host='0.0.0.0')