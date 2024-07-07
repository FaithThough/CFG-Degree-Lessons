patient_attend_times = [3, 2, 1, 2, 6]

def minimum_waiting_time(patient_attend_times):
    patient_attend_times.sort()
    total = 0

    for index, time in enumerate(patient_attend_times):
        patients_left = len(patient_attend_times) - (index + 1)
        total += time * patients_left

    return total

result = minimum_waiting_time(patient_attend_times)
print(result)


