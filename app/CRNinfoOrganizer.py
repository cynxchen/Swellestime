# Alice Li
# WHACKS hack
# 10.03.2015

import HTMLscraper as scrape

# example dictionary sample:
# '11829':
# {'Distribution(s)': 'Historical Studies', 'Seats Available': '0 / 15',
# 'Title': 'Sem: WorldWarII as Memory&Myth;', 'Location(s)': 'Founders Hall 305',
# 'Course': 'HIST 302 - 01',
# 'Day/Time': {'Th': '02:50 pm - 05:20 pm'},        IS ITS OWN MAP!
# 'Instructor': 'Nina Tumarkin', 'CRN': '11829'}

wellesTable = scrape.BrowserScraper()
allcourses = wellesTable.getAllCourses()    #allcourses is a dictionary

def getInfoFromCRN(crn):
    for n in allcourses:
        if crn == n:
            return allcourses.get(n)

def getDist(crn):
    return getInfoFromCRN(crn).get('Distribution(s)')

def getAvailSeats(crn):
    return getInfoFromCRN(crn).get('Seats Available')

def getTitle(crn):
    return getInfoFromCRN(crn).get('Title')

def getLoc(crn):
    return getInfoFromCRN(crn).get('Location(s)')

def getCourseCode(crn):
    return getInfoFromCRN(crn).get('Course')

# gets the days the course is on
# returns a dictionary of {day: time}
# need just a list of times or days?
#

def getDayTimes(crn):
    return getInfoFromCRN(crn).get('Day/Time')

def getInstructor(crn):
    return getInfoFromCRN(crn).get('Instructor')
