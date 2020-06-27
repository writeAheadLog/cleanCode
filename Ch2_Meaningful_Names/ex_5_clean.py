realDaysPerIdealDay = 4
WORK_DAYS_PER_WEEK = 5
NUMBER_OF_TASKS = 34
sum = 0

taskEstimate = list()

for j in range(NUMBER_OF_TASKS):
    realTaskDays = taskEstimate[j] * realDaysPerIdealDay
    realTaskWeeks = (realTaskDays / WORK_DAYS_PER_WEEK)
    sum += realTaskWeeks



