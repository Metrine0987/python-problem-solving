def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"

    return "Fail"

print(get_grade(85))
print(get_grade(64))
print(get_grade(45))
print(get_grade(35))