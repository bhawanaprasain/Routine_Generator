

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
    "BRT": ["Physics", "", " ", "DSAP"],
    "SS": ["", "ECT", "", ""],
    "HKC": ["", "", "COA", "Elective I"],
    "BRB": ["BEE", "", "", ""],
    "PP": ["Math", "", "PS", ""],
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
    "BRB": ["Engineering Drawing", "", "", ""]

}

teachers = ["HPB", "UB", "SRP", "ST", "HNT", "NL", "BRT", "SS", "HKC", "BRB", "PP", "BP", "KRK",
            "HT", "BN", "SN", "SRT", "BHP", "RPP", "RT", "TNU", "AA", "SSM", "AKS", "KRS", "KP", "BRB"]

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
print(teachersWhoHaveClassesInFirstYear)
print(teachersWhoHaveClassesInSecondYear)
print(teachersWhoHaveClassesInThirdYear)
print(teachersWhoHaveClassesInFourthYear)
