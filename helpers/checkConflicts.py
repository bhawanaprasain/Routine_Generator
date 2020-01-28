

import random

firstYearSubjects = [
    "Mathematics I",
    "Computer Programming",
    "Engineering Drawing I",
    "Engineering Physics",
    "Applied Mechanics",
    "Basic Electrical Engineering"
]
secondYearSubjects = [
    " Mathematics III ",
    "Object Oriented Programming ",
    "Electrical Circuit Theory ",
    "Theory of Computation",
    "Electronics Devices and Circuit",
    "Digital Logic ",
    "Electromagnetism "

]
thirdYearSubjects = [
    "Communication English ",
    "Probability and Statistics",
    "Computer organization and Architecture",
    "Software Engineering",
    "Computer Graphics",
    "Instrumentation II ",
    "Data Communication "
]
fourthYearSubjects = [
    " ICT Project Management",
    "Organization and Management",
    "Energy Environment and Society",
    "Distributed System",
    "Computer Networks and Security",
    "Digital Signal Analysis and Processing",
    "Elective I",
    "Project I"
]

subjectteachers = {
    "HPB": ["C Programming", "",  "Computer Graphics", ""],
    "UB": ["", "TOC", "", ""],
    "SRP": ["", "OOP", "Software Engineering", ""],
    "ST": ["", "", "Instrumentation II", ""],
    "HNT": ["", "Digital Logic", "Data Communication", ""],
    "NL": ["", "", "", "ICT Project Management"],
    "BRT": ["Physics", "", "", "DSAP"],
    "SS": ["", "ECT", "", ""],
    "HKC": ["", "", "COA", "Elective I"],
    "BRB": ["BEE", "", "", ""],
    "PP": ["Mathematics I", "", "PS", ""],
    "BP": ["Applied Mechanics", "", "", ""],
    "KRK": ["", "EDC", "", ""],
    "HT": ["", "EM", "", ""],
    "BN": ["", "", "Communication English", ""],
    "SN": ["", "", "Communication English", ""],
    "SRT": ["", "", "", "CNS"],
    "BHP": ["", "", "", "Distributed System"],
    "RPP": ["", "", "", "Energy Environment and Society"],
    "RT": ["", "", "", "Organization And Management"],
    "TNU": ["Mathematics I", "Mathematics II", "", ""],
    "AA": ["Mathematics I", "Mathematics II", "", ""],
    "SSM": ["Mathematics I", "Mathematics II", "", ""],
    "AKS": ["Physics", "", "", ""],
    "KRS": ["Physics", "", "", ""],
    "KP": ["Engineering Drawing", "", "", ""],
    "BRBD": ["Engineering Drawing", "", "", ""]

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
    print("Mr {0} go to first year bct and teach them {1}".format(
        teachersWhoHaveClassesInFirstYear[period], subjectteachers[teachersWhoHaveClassesInFirstYear[period]][0]))
    return teachersWhoHaveClassesInFirstYear[period]


def teacherSelectionForSecondYear(period):
    print("Mr {0} go to second year bct and teach them {1}".format(
        teachersWhoHaveClassesInSecondYear[period], subjectteachers[teachersWhoHaveClassesInSecondYear[period]][1]))
    return(teachersWhoHaveClassesInSecondYear[period])


def teacherSelectionForThirdYear(period):

    print("Mr {0} go to third year bct and teach them {1}".format(
        teachersWhoHaveClassesInThirdYear[period], subjectteachers[teachersWhoHaveClassesInThirdYear[period]][2]))
    return(teachersWhoHaveClassesInThirdYear[period])


def teacherSelectionForFourthYear(period):
    print("Mr {0} go to fourth year bct and teach them  {1}".format(
        teachersWhoHaveClassesInFourthYear[period], subjectteachers[teachersWhoHaveClassesInFourthYear[period]][3]))


def routineMaker(period):

    teacherSelectionForFirstYear(period)
    teacherSelectionForSecondYear(period)
    teacherSelectionForThirdYear(period)
    teacherSelectionForFourthYear(period)
    print("  ")


def checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(period):
    teacherInFirstYear = teachersWhoHaveClassesInFirstYear[period]
    teacherInSecondYear = teachersWhoHaveClassesInSecondYear[period]
    teacherInThirdYear = teachersWhoHaveClassesInThirdYear[period]
    teacherInFourthYear = teachersWhoHaveClassesInFourthYear[period]
    if(teacherInFirstYear == teacherInSecondYear or teacherInFirstYear == teacherInThirdYear or teacherInFirstYear == teacherInFourthYear or teacherInSecondYear == teacherInThirdYear or teacherInSecondYear == teacherInFourthYear or teacherInThirdYear == teacherInFourthYear):
        if(teacherInFirstYear == teacherInSecondYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period+1)
            teacherSelectionForThirdYear(period)
            teacherSelectionForFourthYear(period)
        elif(teacherInFirstYear == teacherInThirdYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period)
            teacherSelectionForThirdYear(period+1)
            teacherSelectionForFourthYear(period)
        elif(teacherInFirstYear == teacherInFourthYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period)
            teacherSelectionForThirdYear(period)
            teacherSelectionForFourthYear(period+1)
        elif(teacherInSecondYear == teacherInThirdYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period)
            teacherSelectionForThirdYear(period+1)
            teacherSelectionForFourthYear(period)
        elif(teacherInSecondYear == teacherInFourthYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period)
            teacherSelectionForThirdYear(period)
            teacherSelectionForFourthYear(period+1)
        elif(teacherInThirdYear == teacherInFourthYear):
            teacherSelectionForFirstYear(period)
            teacherSelectionForSecondYear(period)
            teacherSelectionForThirdYear(period)
            teacherSelectionForFourthYear(period+1)
    else:
        routineMaker(period)


# for period in range(1, 7):
#     checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(period)


Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for daysOfWeek in range(1, 7):
    print("   ")

    print("ROUTINE FOR {0}".format(
        Days[daysOfWeek-1]
    ))
    print("   ")
    for periodsInAday in range(1, 7):

        print("PERIOD : {0}".format(periodsInAday))
        checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(
            periodsInAday)
