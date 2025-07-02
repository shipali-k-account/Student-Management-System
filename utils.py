def calculate_total(s1, s2, s3):
    return s1 + s2 + s3

def calculate_average(total):
    return round(total / 3, 2)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"
