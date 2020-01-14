

import random

teachingHoursForASubject = {

    "Mathematics I": 8,
    "Computer Programming": 8,
    "Engineering Drawing I": 8,
    "Engineering Physics": 8,
    "Applied Mechanics": 8,
    "Basic Electrical Engineering": 8,
    "Mathematics II": 8,
    "Object Oriented Programming": 8,
    "Electrical Circuit Theory": 8,
    "Theory of Computation": 8,
    "Electronics Devices and Circuit": 8,
    "Digital Logic": 8,
    "Electromagnetism": 8,
    "Communication English": 8,
    "Probability and Statistics": 8,
    "Computer organization and Architecture": 8,
    "Software Engineering": 8,
    "Computer Graphics": 8,
    "Instrumentation II": 8,
    "Data Communication": 8,
    "ICT Project Management": 8,
    "Organization And Management": 8,
    "Energy Environment and Society": 8,
    "Distributed System": 8,
    "Computer Networks and Security": 8,
    "Digital Signal Analysis and Processing": 8,
    "Elective I": 8,
    "Project I": 8

}

teachingHoursForTeachersInADay = {
    "HPB": 4,
    "UB": 4,
    "SRP": 4,
    "ST": 4,
    "HNT": 4,
    "NL": 4,
    "BRT": 4,
    "SS": 4,
    "HKC": 4,
    "BRB": 4,
    "PP": 4,
    "BP": 4,
    "KRK": 4,
    "HT": 4,
    "BN": 4,
    "SN": 4,
    "SRT": 4,
    "BHP": 4,
    "RPP": 4,
    "RT": 4,
    "TNU": 4,
    "AA": 4,
    "SSM": 4,
    "AKS": 4,
    "KRS": 4,
    "KP": 4,
    "BRBD": 4

}

teachingHoursForTeachersInAWeek = {
    "HPB": 8,
    "UB": 4,
    "SRP": 8,
    "ST": 4,
    "HNT": 8,
    "NL": 4,
    "BRT": 8,
    "SS": 4,
    "HKC": 8,
    "BRB": 4,
    "PP": 8,
    "BP": 4,
    "KRK": 4,
    "HT": 4,
    "BN": 4,
    "SN": 4,
    "SRT": 4,
    "BHP": 4,
    "RPP": 4,
    "RT": 4,
    "TNU": 8,
    "AA": 8,
    "SSM": 8,
    "AKS": 4,
    "KRS": 4,
    "KP": 4,
    "BRBD": 4

}


def remainingTeachingHoursOfSubjects():
    for subjects in teachingHoursForASubject.keys():
        print(subjects)
        print(teachingHoursForASubject[subjects]-2)


remainingTeachingHoursOfSubjects()


firstYearSubjects = [
    "Mathematics I",
    "Computer Programming",
    "Engineering Drawing I",
    "Engineering Physics",
    "Applied Mechanics",
    "Basic Electrical Engineering",

]
secondYearSubjects = [
    "Mathematics II",
    "Object Oriented Programming",
    "Electrical Circuit Theory",
    "Theory of Computation",
    "Electronics Devices and Circuit",
    "Digital Logic",
    "Electromagnetism"

]
thirdYearSubjects = [
    "Communication English",
    "Probability and Statistics",
    "Computer organization and Architecture",
    "Software Engineering",
    "Computer Graphics",
    "Instrumentation II",
    "Data Communication "
]
fourthYearSubjects = [
    "ICT Project Management",
    "Organization And Management",
    "Energy Environment and Society",
    "Distributed System",
    "Computer Networks and Security",
    "Digital Signal Analysis and Processing",
    "Elective I",
    "Project I"
]

subjectteachers = {
    "HPB": ["Computer Programming", "",  "Computer Graphics", ""],
    "UB": ["", "Theory of Computation", "", ""],
    "SRP": ["", "Object Oriented Programming", "Software Engineering", ""],
    "ST": ["", "", "Instrumentation II", ""],
    "HNT": ["", "Digital Logic", "Data Communication", ""],
    "NL": ["", "", "", "ICT Project Management"],
    "BRT": ["Engineering Physics", "", "", "Digital Signal Analysis and Processing"],
    "SS": ["", "Electrical Circuit Theory", "", ""],
    "HKC": ["", "", "Computer organization and Architecture", "Elective I"],
    "BRB": ["Basic Electrical Engineering", "", "", ""],
    "PP": ["Mathematics I", "", "Probability and Statistics", ""],
    "BP": ["Applied Mechanics", "", "", ""],
    "KRK": ["", "Electronics Devices and Circuit", "", ""],
    "HT": ["", "Electromagnetism", "", ""],
    "BN": ["", "", "Communication English", ""],
    "SN": ["", "", "Communication English", ""],
    "SRT": ["", "", "", "Computer Networks and Security"],
    "BHP": ["", "", "", "Distributed System"],
    "RPP": ["", "", "", "Energy Environment and Society"],
    "RT": ["", "", "", "Organization And Management"],
    "TNU": ["Mathematics I", "Mathematics II", "", ""],
    "AA": ["Mathematics I", "Mathematics II", "", ""],
    "SSM": ["Mathematics I", "Mathematics II", "", ""],
    "AKS": ["Engineering Physics", "", "", ""],
    "KRS": ["Engineering Physics", "", "", ""],
    "KP": ["Engineering Drawing I", "", "", ""],
    "BRBD": ["Engineering Drawing I", "", "", ""]

}

teachers = ["HPB", "UB", "SRP", "ST", "HNT", "NL", "BRT", "SS", "HKC", "BRB", "PP", "BP", "KRK",
            "HT", "BN", "SN", "SRT", "BHP", "RPP", "RT", "TNU", "AA", "SSM", "AKS", "KRS", "KP", "BRBD"]

selectedteachers = []
firstPeriod = []
dayWiseSelection = []


def randomTeacherSelection():
    randomTeacher = random.choice(teachers)
    return randomTeacher


teachersWhoHaveClassesInFirstYear = []
teachersWhoHaveClassesInSecondYear = []
teachersWhoHaveClassesInThirdYear = []
teachersWhoHaveClassesInFourthYear = []

for teachers in subjectteachers.keys():

    if(len(subjectteachers[teachers][0]) != 0):
        teachersWhoHaveClassesInFirstYear.append(
            teachers)
    if(len(subjectteachers[teachers][1]) != 0):
        teachersWhoHaveClassesInSecondYear.append(
            teachers)
    if(len(subjectteachers[teachers][2]) != 0):
        teachersWhoHaveClassesInThirdYear.append(
            teachers)
    if(len(subjectteachers[teachers][3]) != 0):
        teachersWhoHaveClassesInFourthYear.append(
            teachers)


def generateDailyRoutine():
    print("under construction")


def teacherSelectionForFirstYear(period):
    currentSubjectof1stYear = subjectteachers[teachersWhoHaveClassesInFirstYear[period]][0]
    print("Mr {0} go to first year bct and teach them {1}".format(
        teachersWhoHaveClassesInFirstYear[period], currentSubjectof1stYear))
    remaingTeachingHoursInADayForCurrentTeacher = teachingHoursForTeachersInADay[
        teachersWhoHaveClassesInFirstYear[period]]-2
    print(remaingTeachingHoursInADayForCurrentTeacher)
    teachingHoursForTeachersInADay[teachersWhoHaveClassesInFirstYear[period]
                                   ] = remaingTeachingHoursInADayForCurrentTeacher

    remainingTeachingHoursOfCurrentSubject1stYear = teachingHoursForASubject[
        currentSubjectof1stYear]-2
    teachingHoursForASubject[currentSubjectof1stYear] = teachingHoursForASubject[currentSubjectof1stYear]-2
    print(remainingTeachingHoursOfCurrentSubject1stYear)
    return teachersWhoHaveClassesInFirstYear[period]


def teacherSelectionForSecondYear(period):
    currentSubjectof2ndYear = subjectteachers[teachersWhoHaveClassesInSecondYear[period]][1]
    print(currentSubjectof2ndYear)
    print("Mr {0} go to second year bct and teach them {1}".format(
        teachersWhoHaveClassesInSecondYear[period], currentSubjectof2ndYear))
    remaingTeachingHoursInADayForCurrentTeacher = teachingHoursForTeachersInADay[
        teachersWhoHaveClassesInSecondYear[period]]-2
    print(remaingTeachingHoursInADayForCurrentTeacher)
    teachingHoursForTeachersInADay[teachersWhoHaveClassesInSecondYear[period]
                                   ] = remaingTeachingHoursInADayForCurrentTeacher

    remainingTeachingHoursOfCurrentSubject2ndYear = teachingHoursForASubject[
        currentSubjectof2ndYear]-2
    teachingHoursForASubject[currentSubjectof2ndYear] = teachingHoursForASubject[currentSubjectof2ndYear]-2
    print(remainingTeachingHoursOfCurrentSubject2ndYear)
    return(teachersWhoHaveClassesInSecondYear[period])


def teacherSelectionForThirdYear(period):
    currentSubjectof3rdYear = subjectteachers[teachersWhoHaveClassesInThirdYear[period]][2]

    print("Mr {0} go to third year bct and teach them {1}".format(
        teachersWhoHaveClassesInThirdYear[period], subjectteachers[teachersWhoHaveClassesInThirdYear[period]][2]))
    remaingTeachingHoursInADayForCurrentTeacher = teachingHoursForTeachersInADay[
        teachersWhoHaveClassesInThirdYear[period]]-2
    teachingHoursForTeachersInADay[teachersWhoHaveClassesInThirdYear[period]
                                   ] = remaingTeachingHoursInADayForCurrentTeacher
    print(remaingTeachingHoursInADayForCurrentTeacher)
    remainingTeachingHoursOfCurrentSubject3rdYear = teachingHoursForASubject[
        currentSubjectof3rdYear]-2
    teachingHoursForASubject[currentSubjectof3rdYear] = teachingHoursForASubject[currentSubjectof3rdYear]-2
    print(remainingTeachingHoursOfCurrentSubject3rdYear)
    return(teachersWhoHaveClassesInThirdYear[period])


def teacherSelectionForFourthYear(period):
    currentSubjectof4thYear = subjectteachers[teachersWhoHaveClassesInFourthYear[period]][3]

    print("Mr {0} go to fourth year bct and teach them  {1}".format(
        teachersWhoHaveClassesInFourthYear[period], subjectteachers[teachersWhoHaveClassesInFourthYear[period]][3]))
    remaingTeachingHoursInADayForCurrentTeacher = teachingHoursForTeachersInADay[
        teachersWhoHaveClassesInFourthYear[period]]-2
    teachingHoursForTeachersInADay[teachersWhoHaveClassesInFourthYear[period]
                                   ] = remaingTeachingHoursInADayForCurrentTeacher
    print(remaingTeachingHoursInADayForCurrentTeacher)
    remainingTeachingHoursOfCurrentSubject4thYear = teachingHoursForASubject[
        currentSubjectof4thYear]-2
    teachingHoursForASubject[currentSubjectof4thYear] = teachingHoursForASubject[currentSubjectof4thYear]-2
    print(remainingTeachingHoursOfCurrentSubject4thYear)
    return(teachersWhoHaveClassesInFourthYear[period])


def routineMaker(period):
    periodsForFirstYear = period % totalTeachersAvailableForFirstYear
    periodsForSecondYear = period % totalTeachersAvailableForSecondYear
    periodsForThirdYear = period % totalTeachersAvailableForThirdYear
    periodsForFourthYear = period % totalTeachersAvailableForFourthYear

    teacherSelectionForFirstYear(periodsForFirstYear)
    teacherSelectionForSecondYear(periodsForSecondYear)
    teacherSelectionForThirdYear(periodsForThirdYear)
    teacherSelectionForFourthYear(periodsForFourthYear)
    print("  ")


def checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(period):
    periodsForFirstYear = period % totalTeachersAvailableForFirstYear
    periodsForSecondYear = period % totalTeachersAvailableForSecondYear
    periodsForThirdYear = period % totalTeachersAvailableForThirdYear
    periodsForFourthYear = period % totalTeachersAvailableForFourthYear
    teacherInFirstYear = teachersWhoHaveClassesInFirstYear[periodsForFirstYear]
    teacherInSecondYear = teachersWhoHaveClassesInSecondYear[periodsForSecondYear]
    teacherInThirdYear = teachersWhoHaveClassesInThirdYear[periodsForThirdYear]
    teacherInFourthYear = teachersWhoHaveClassesInFourthYear[periodsForFourthYear]
    if(teacherInFirstYear == teacherInSecondYear or teacherInFirstYear == teacherInThirdYear or teacherInFirstYear == teacherInFourthYear or teacherInSecondYear == teacherInThirdYear or teacherInSecondYear == teacherInFourthYear or teacherInThirdYear == teacherInFourthYear):
        if(teacherInFirstYear == teacherInSecondYear):
            teacherSelectionForFirstYear(periodsForFirstYear)
            teacherSelectionForSecondYear(periodsForSecondYear+1)
            teacherSelectionForThirdYear(periodsForThirdYear)
            teacherSelectionForFourthYear(periodsForFourthYear)
        elif(teacherInFirstYear == teacherInThirdYear):
            teacherSelectionForFirstYear(periodsForFirstYear)
            teacherSelectionForSecondYear(periodsForSecondYear)
            teacherSelectionForThirdYear(periodsForThirdYear+1)
            teacherSelectionForFourthYear(periodsForFourthYear)
        elif(teacherInFirstYear == teacherInFourthYear):
            teacherSelectionForFirstYear(periodsForFirstYear)
            teacherSelectionForSecondYear(periodsForSecondYear)
            teacherSelectionForThirdYear(periodsForThirdYear)
            teacherSelectionForFourthYear(periodsForFourthYear+1)
        elif(teacherInSecondYear == teacherInThirdYear):
            teacherSelectionForFirstYear(periodsForFirstYear)
            teacherSelectionForSecondYear(periodsForSecondYear)
            teacherSelectionForThirdYear(periodsForThirdYear+1)
            teacherSelectionForFourthYear(periodsForFourthYear)
        elif(teacherInSecondYear == teacherInFourthYear):
            teacherSelectionForFirstYear(periodsForFirstYear)
            teacherSelectionForSecondYear(periodsForSecondYear)
            teacherSelectionForThirdYear(periodsForThirdYear)
            teacherSelectionForFourthYear(periodsForFourthYear+1)
        elif(teacherInThirdYear == teacherInFourthYear):
            teacherSelectionForFirstYear(periodsForFourthYear)
            teacherSelectionForSecondYear(periodsForSecondYear)
            teacherSelectionForThirdYear(periodsForThirdYear)
            teacherSelectionForFourthYear(periodsForFourthYear+1)
    else:
        routineMaker(period)


def countTeachingHoursOfASubject():
    print("lets start")


def teachingHoursBasedRoutine():
    print("hard one")


totalTeachersAvailableForFirstYear = len(teachersWhoHaveClassesInFirstYear)
totalTeachersAvailableForSecondYear = len(teachersWhoHaveClassesInSecondYear)
totalTeachersAvailableForThirdYear = len(teachersWhoHaveClassesInThirdYear)
totalTeachersAvailableForFourthYear = len(teachersWhoHaveClassesInFourthYear)

Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for daysOfWeek in range(0, 6):
    print("   ")

    print("ROUTINE FOR {0}".format(
        Days[daysOfWeek]
    ))
    print("   ")
    for periodsInAday in range(daysOfWeek*4, daysOfWeek*4+4):

        print("PERIOD : {0}".format(periodsInAday))
        checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(
            periodsInAday)


for days in range(0, 6):
    for inner in range(days*4, days*4+4):
        print(
            teachersWhoHaveClassesInFirstYear[inner % totalTeachersAvailableForFirstYear])
        print(
            teachersWhoHaveClassesInSecondYear[inner % totalTeachersAvailableForSecondYear])
        print(
            teachersWhoHaveClassesInThirdYear[inner % totalTeachersAvailableForThirdYear])
        print(teachersWhoHaveClassesInFourthYear[inner %
                                                 totalTeachersAvailableForFourthYear])
