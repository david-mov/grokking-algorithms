# classroom scheduling problem

schedule: dict[str, tuple[str, str]] = {
    'art': ('08:00', '10:00'),
    'eng': ('09:30', '10:30'),
    'math': ('10:00', '11:00'),
    'cs': ('10:30','11:30'),
    'music': ('11:00', '12:00')
}

# get the biggest set of courses possible

def greedy_schedule_solution(schedule: dict[str, tuple[str, str]]) -> list[str]:
    solution: list[str] = []
    courses: list[str] = list(schedule.keys())

    while courses:
        solution.append(soonest_finished(courses))
        filtered_courses: list[str] = courses_after(schedule[solution[-1]][1], courses)
        if filtered_courses == courses: break
        else: courses = filtered_courses
    
    return solution

def soonest_finished(courses: list[str]) -> str:
    end_soonest: str = courses[0]
    for course in courses:
        if schedule[course][1] < schedule[end_soonest][1]:
            end_soonest = course
    return end_soonest

def courses_after(time: str, courses: list[str]) -> list[str]:
    filtered_courses: list[str] = []
    for course in courses:
        if schedule[course][0] >= time:
            filtered_courses.append(course)
    return filtered_courses


print(greedy_schedule_solution(schedule))