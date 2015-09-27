import requests
from bs4 import BeautifulSoup

"""

meant to populate databases

"""


def main():
	url = "https://www.myedu.com/University-of-Texas-at-Austin/school/2719/course/by-department/"
	r = requests.get(url)

	ab = "";
	nm = "";
	cnum = "";
	cnam = "";
	teach = "";

	soup = BeautifulSoup(r.text, 'html.parser').find("tbody")
	for link in soup.find_all("tr"):
		for linkd in soup.find_all("td"):
			for linkd in soup.find_all("a"):
				print linkd.get("class")








if __name__ == "__main__":
	main()