

teachingHoursForASubject = {

    "Mathematics I": 4,
    "Computer Programming": 4,
    "Engineering Drawing I": 4,
    "Engineering Physics": 4,
    "Applied Mechanics": 4,
    "Basic Electrical Engineering": 4,
    "Mathematics II": 4,
    "Object Oriented Programming": 4,
    "Electrical Circuit Theory": 4,
    "Theory of Computation": 4,
    "Electronics Devices and Circuit": 4,
    "Digital Logic": 4,
    "Electromagnetism": 4,
    "Communication English": 4,
    "Probability and Statistics": 4,
    "Computer organization and Architecture": 4,
    "Software Engineering": 4,
    "Computer Graphics": 4,
    "Instrumentation II": 4,
    "Data Communication": 4,
    "ICT Project Management": 4,
    "Organization And Management": 4,
    "Energy Environment and Society": 4,
    "Distributed System": 4,
    "Computer Networks and Security": 4,
    "Digital Signal Analysis and Processing": 4,
    "Elective I": 4,


}
print(sum(teachingHoursForASubject.values()))

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
mappedSubjectsAndTeachers = {
    "Mathematics I": "TNU",
    "Computer Programming": "HPB",
    "Engineering Drawing I": "KP",
    "Engineering Physics": "AKS",
    "Applied Mechanics": "BP",
    "Basic Electrical Engineering": "BRB",

    "Mathematics II": "PP",
    "Object Oriented Programming": "SRP",
    "Electrical Circuit Theory": "SS",
    "Theory of Computation": "UB",
    "Electronics Devices and Circuit": "KRK",
    "Digital Logic": 'HNT',
    "Electromagnetism": "HRT",

    "Communication English": "SN",
    "Probability and Statistics": "PP",
    "Computer organization and Architecture": "HKC",
    "Software Engineering": "SRP",
    "Computer Graphics": "HPB",
    "Instrumentation II": "ST",
    "Data Communication": "HNT",

    "ICT Project Management": "NL",
    "Organization And Management": "RT",
    "Energy Environment and Society": "RPP",
    "Distributed System": "BHP",
    "Computer Networks and Security": "SRT",
    "Digital Signal Analysis and Processing": "BRT",
    "Elective I": "HKC",
}


# def remainingTeachingHoursOfSubjects():
#     for subjects in teachingHoursForASubject.keys():
#         print(subjects)
#         print(teachingHoursForASubject[subjects]-1)


firstYearSubjects = [
    "Mathematics I",
    "Computer Programming",
    "Engineering Drawing I",
    "Engineering Physics",
    "Applied Mechanics",
    "Basic Electrical Engineering",

]
THfor1styear = 4*len(firstYearSubjects)

secondYearSubjects = [
    "Mathematics II",
    "Object Oriented Programming",
    "Electrical Circuit Theory",
    "Theory of Computation",
    "Electronics Devices and Circuit",
    "Digital Logic",
    "Electromagnetism"

]
THfor2ndyear = 4*len(secondYearSubjects)
thirdYearSubjects = [
    "Communication English",
    "Probability and Statistics",
    "Computer organization and Architecture",
    "Software Engineering",
    "Computer Graphics",
    "Instrumentation II",
    "Data Communication"
]
THfor3rdyear = 4*len(thirdYearSubjects)
fourthYearSubjects = [
    "ICT Project Management",
    "Organization And Management",
    "Energy Environment and Society",
    "Distributed System",
    "Computer Networks and Security",
    "Digital Signal Analysis and Processing",
    "Elective I",

]
THfor4thyear = 4*len(fourthYearSubjects)-4
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


def remainingTeachingHoursOfCTIW(currentTeacher):

    teachingHoursForTeachersInAWeek[currentTeacher] = teachingHoursForTeachersInAWeek[currentTeacher]-2
    remainingTeachingHoursOfCTIW = teachingHoursForTeachersInAWeek[currentTeacher]
    print(" remaining teaching hours for {0} is {1}".format(
        currentTeacher, teachingHoursForTeachersInAWeek[currentTeacher]))
    return(remainingTeachingHoursOfCTIW)


def remainingTeachingHoursOfEachSubject(currentSubject):

    teachingHoursForASubject[currentSubject] = teachingHoursForASubject[currentSubject]-2
    remainingTeachingHours = teachingHoursForASubject[currentSubject]

    return remainingTeachingHours


def displayRTHOfEachSubject(currentSubject):
    classvalidity = remainingTeachingHoursOfEachSubject(
        currentSubject)
    if classvalidity < 0:

        return classvalidity
    else:

        print("RTH of {0}:  {1}".format(
            currentSubject,  teachingHoursForASubject[currentSubject])
        )
        return classvalidity


def remainingTeachingHoursInADayForCurrentTeacher(currentTeacher):
    teachingHoursForTeachersInADay[
        currentTeacher] = teachingHoursForTeachersInADay[
        currentTeacher]-2
    RTHOfcurrentTeacher = teachingHoursForTeachersInADay[
        currentTeacher]
    return RTHOfcurrentTeacher


def displayRTHInADayForCurrentTeacher(currentTeacher):
    print("RTH of {0}: {1}".format(
        currentTeacher, remainingTeachingHoursInADayForCurrentTeacher(currentTeacher)))


def displayTeacherAndSubject(currentTeacher, year, currentSubject):
    print("Mr {0} go to {1} year bct and teach them {2}".format(
        currentTeacher, year, currentSubject))


def teacherSelectionForFirstYear(period):
    currentSubjectof1stYear = subjectteachers[teachersWhoHaveClassesInFirstYear[period]][0]
    currentTeacher = teachersWhoHaveClassesInFirstYear[period]
    year = "first"

    RTHofCurrentSub = displayRTHOfEachSubject(currentSubjectof1stYear)

    if(RTHofCurrentSub >= 0):
        displayTeacherAndSubject(currentTeacher, year, currentSubjectof1stYear)
        remainingTeachingHoursOfCTIW(currentTeacher)
        remainingTeachingHoursInADayForCurrentTeacher(currentTeacher)

    else:
        teachingHoursForASubject[currentSubjectof1stYear] = teachingHoursForASubject[currentSubjectof1stYear]+2
        RTHofBCT1stYear()
    return teachersWhoHaveClassesInFirstYear[period]


def teacherSelectionForSecondYear(period):
    currentSubjectof2ndYear = subjectteachers[teachersWhoHaveClassesInSecondYear[period]][1]
    currentTeacher = teachersWhoHaveClassesInSecondYear[period]
    year = "second"

    RTHofCurrentSub = displayRTHOfEachSubject(currentSubjectof2ndYear)

    if(RTHofCurrentSub >= 0):
        displayTeacherAndSubject(currentTeacher, year, currentSubjectof2ndYear)
        remainingTeachingHoursOfCTIW(currentTeacher)
        remainingTeachingHoursInADayForCurrentTeacher(currentTeacher)

    else:
        teachingHoursForASubject[currentSubjectof2ndYear] = teachingHoursForASubject[currentSubjectof2ndYear]+2
        RTHofBCT2ndYear()
    return(teachersWhoHaveClassesInSecondYear[period])


def teacherSelectionForThirdYear(period):
    currentSubjectof3rdYear = subjectteachers[teachersWhoHaveClassesInThirdYear[period]][2]
    currentTeacher = teachersWhoHaveClassesInThirdYear[period]
    year = "third"

    RTHofCurrentSub = displayRTHOfEachSubject(currentSubjectof3rdYear)

    if(RTHofCurrentSub >= 0):
        displayTeacherAndSubject(currentTeacher, year, currentSubjectof3rdYear)
        remainingTeachingHoursOfCTIW(currentTeacher)
        remainingTeachingHoursInADayForCurrentTeacher(currentTeacher)

    else:
        teachingHoursForASubject[currentSubjectof3rdYear] = teachingHoursForASubject[currentSubjectof3rdYear]+2
        RTHofBCT3rdYear()
    return(teachersWhoHaveClassesInThirdYear[period])


def teacherSelectionForFourthYear(period):
    currentSubjectof4thYear = subjectteachers[teachersWhoHaveClassesInFourthYear[period]][3]
    currentTeacher = teachersWhoHaveClassesInFourthYear[period]
    year = "fourth"

    RTHofCurrentSub = displayRTHOfEachSubject(currentSubjectof4thYear)

    if(RTHofCurrentSub >= 0):
        displayTeacherAndSubject(currentTeacher, year, currentSubjectof4thYear)
        remainingTeachingHoursOfCTIW(currentTeacher)
        remainingTeachingHoursInADayForCurrentTeacher(currentTeacher)

    else:
        teachingHoursForASubject[currentSubjectof4thYear] = teachingHoursForASubject[currentSubjectof4thYear]+2
        RTHofBCT4thYear()
    return(teachersWhoHaveClassesInFourthYear[period])


def routineMaker(period):
    periodsForFirstYear = period % totalTeachersAvailableForFirstYear
    periodsForSecondYear = period % totalTeachersAvailableForSecondYear
    periodsForThirdYear = period % totalTeachersAvailableForThirdYear
    periodsForFourthYear = period % totalTeachersAvailableForFourthYear

    teacherSelectionForFirstYear(periodsForFirstYear)
    print("  ")

    teacherSelectionForSecondYear(periodsForSecondYear)
    print("  ")

    teacherSelectionForThirdYear(periodsForThirdYear)
    print("  ")

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


totalTeachersAvailableForFirstYear = len(teachersWhoHaveClassesInFirstYear)
totalTeachersAvailableForSecondYear = len(teachersWhoHaveClassesInSecondYear)
totalTeachersAvailableForThirdYear = len(teachersWhoHaveClassesInThirdYear)
totalTeachersAvailableForFourthYear = len(teachersWhoHaveClassesInFourthYear)


def updateRTHOfEachSubject():
    print(teachingHoursForASubject)


def filterRemainingSubjects():
    remainingSubjects = []
    for key, value in teachingHoursForASubject.items():
        if(value > 0):
            print(key, value)
            remainingSubjects.append(key)
            remainingSubjects.append(value)


def filterRemainingTeachers():
    remainingTeachers = []
    for key, value in teachingHoursForTeachersInAWeek.items():
        print(key, value)
        if(value > 0):
            remainingTeachers.append(key)
    print(remainingTeachers)
    print(len(remainingTeachers))


def returnRemSub(RTHdata, remainingTimeOfEverySubject):
    count = 0
    for data in RTHdata:
        if data != 0:

            subject = remainingTimeOfEverySubject[count*2]
            return subject
        else:
            count += 1


def RTHofBCT1stYear():
    remainingTimeOfEverySubject = []
    RTHdata = []
    year = "first"

    for subjects in firstYearSubjects:
        RTH = teachingHoursForASubject[subjects]
        remainingTimeOfEverySubject.append(subjects)
        remainingTimeOfEverySubject.append(RTH)
        RTHdata.append(RTH)

    print(RTHdata)
    print(remainingTimeOfEverySubject)
    if(RTHdata.count(0) != len(firstYearSubjects)):
        subject = returnRemSub(RTHdata, remainingTimeOfEverySubject)
        teacher = mappedSubjectsAndTeachers[subject]
        teachingHoursForTeachersInAWeek[teacher] = teachingHoursForTeachersInAWeek[teacher] - 2
        teachingHoursForASubject[subject] = teachingHoursForASubject[subject]-2

        displayTeacherAndSubject(
            mappedSubjectsAndTeachers[subject], year, subject)

    else:
        print("LESIURE PERIOD in {0} year".format(year))


def RTHofBCT2ndYear():
    remainingTimeOfEverySubject = []
    RTHdata = []
    year = "second"

    for subjects in secondYearSubjects:
        RTH = teachingHoursForASubject[subjects]
        remainingTimeOfEverySubject.append(subjects)
        remainingTimeOfEverySubject.append(RTH)
        RTHdata.append(RTH)

    print(RTHdata)
    if(RTHdata.count(0) != len(secondYearSubjects)):
        subject = returnRemSub(RTHdata, remainingTimeOfEverySubject)
        teacher = mappedSubjectsAndTeachers[subject]
        teachingHoursForTeachersInAWeek[teacher] = teachingHoursForTeachersInAWeek[teacher] - 2
        teachingHoursForASubject[subject] = teachingHoursForASubject[subject]-2
        displayTeacherAndSubject(
            mappedSubjectsAndTeachers[subject], year, subject)
    else:
        print("LESIURE PERIOD in {0} year".format(year))


def RTHofBCT3rdYear():
    remainingTimeOfEverySubject = []
    RTHdata = []
    year = "third"
    for subjects in thirdYearSubjects:
        RTH = teachingHoursForASubject[subjects]
        remainingTimeOfEverySubject.append(subjects)
        remainingTimeOfEverySubject.append(RTH)
        RTHdata.append(RTH)

    print(RTHdata)
    if(RTHdata.count(0) != len(thirdYearSubjects)):
        subject = returnRemSub(RTHdata, remainingTimeOfEverySubject)
        teachingHoursForASubject[subject] = teachingHoursForASubject[subject]-2
        teacher = mappedSubjectsAndTeachers[subject]
        teachingHoursForTeachersInAWeek[teacher] = teachingHoursForTeachersInAWeek[teacher] - 2
        displayTeacherAndSubject(
            mappedSubjectsAndTeachers[subject], year, subject)
    else:
        print("LESIURE PERIOD in {0} year".format(year))


def RTHofBCT4thYear():
    remainingTimeOfEverySubject = []
    RTHdata = []
    year = "fourth"

    for subjects in fourthYearSubjects:
        RTH = teachingHoursForASubject[subjects]
        remainingTimeOfEverySubject.append(subjects)
        remainingTimeOfEverySubject.append(RTH)
        RTHdata.append(RTH)

    print(RTHdata)
    if(RTHdata.count(0) != len(fourthYearSubjects)):
        subject = returnRemSub(RTHdata, remainingTimeOfEverySubject)
        teacher = mappedSubjectsAndTeachers[subject]
        teachingHoursForTeachersInAWeek[teacher] = teachingHoursForTeachersInAWeek[teacher] - 2
        teachingHoursForASubject[subject] = teachingHoursForASubject[subject]-2
        displayTeacherAndSubject(
            mappedSubjectsAndTeachers[subject], year, subject)
    else:
        print("LESIURE PERIOD in {0} year".format(year))


Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


for daysOfWeek in range(0, 6):
    period = 1

    selectedTeachersForADay = []

    for periodsInAday in range(daysOfWeek*3, daysOfWeek*3+3):
        Day = Days[daysOfWeek]
        print("ROUTINE FOR {0} PERIOD : {1}".format(
            Days[daysOfWeek], period))
        checkForDuplicationOfTeacherInMultipleClassesInSamePeriod(
            periodsInAday)
        period += 1
        print(" ")
    RTHofBCT1stYear()
    RTHofBCT2ndYear()
    RTHofBCT3rdYear()
    RTHofBCT4thYear()

    # print(teachingHoursForASubject)
    # filterRemainingSubjects()
    # filterRemainingTeachers()
