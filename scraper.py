import requests
from bs4 import BeautifulSoup

"""

meant to populate databases



DISCLAIMER: This code was written under a tight time constraint, it (mostly) does not reflect my "neat" code. 

"""
base_url = "https://www.myedu.com"

def main():
	url = "https://www.myedu.com/University-of-Texas-at-Austin/school/2719/course/by-department/"
	r = requests.get(url)

	ab = "";
	nm = "";
	cnum = "";
	cnam = "";
	teach = "";

	soup = BeautifulSoup(r.text, 'html.parser')
	soup = soup.table
	#print soup.prettif

	#find_teacher("https://www.myedu.com/University-of-Texas-at-Austin/E-316L-British-Literature/course/8396013/", "er","er","er","er")

	
	for i in range(len(soup.find_all("td"))):
		try:
			#print i
			if soup.find_all("td")[i].a["class"] == ["abbreviation"]:
				ab = soup.find_all("td")[i].a.text.strip()
			if soup.find_all("td")[i].a["class"] == ["name"]:
				nm = soup.find_all("td")[i].a.text.strip()
				find_course(soup.find_all("td")[i].a["href"], ab, nm)
		except:
			#print "cant"
			pass


	"""
	for i in range(len(soup.find_all("td"))):
		try:
			print soup.find_all("td")[i].a["class"]
		except:
			pass"""


def find_course(url, ab, nm):
	print "course " + url + "    " + ab + "   " + nm

	r = requests.get(base_url + url)
	soup = BeautifulSoup(r.text, 'html.parser')
	soup = soup.table
	#print soup.prettify()

	for i in range(len(soup.find_all("td"))):
		try:
			#print str(i) + "uuuu"
			if soup.find_all("td")[i].a["class"] == ["abbreviation"]:
				cnum = soup.find_all("td")[i].a.text.strip()
			if soup.find_all("td")[i].a["class"] == ["name"]:
				cnam = soup.find_all("td")[i].a.text.strip()
				find_teacher(soup.find_all("td")[i].a["href"], ab, nm, cnum, cnam)
		except:
			#print "cant teach"
			pass

def find_teacher(url, ab, nm, cnum, cnam):
	print "teach " + url + "    " + ab + "   " + nm + " " + cnum + " " + cnam

	r = requests.get(base_url + url)
	soup = BeautifulSoup(r.text, 'html.parser')
	soup = soup.table

	for i in soup.find_all("td"):
		try:
			if i["class"] == ["name"]:
				tea = i.a.text.strip()
				make_course(ab, nm, cnum, cnam, tea)
		except:
			#print "cant"
			pass

def make_course(ab, nm, cnum, cnam, tea):
	print ab + " " + nm + " " + cnum + " " + cnam + " " + tea
	myCourse = Course(deptAb=ab, deptName=nm, courseNum=cnum, courseName=cnam, teacherName=tea)
	myCourse.save()
	


if __name__ == "__main__":
	main()