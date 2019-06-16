weight = 95.254398
height = 1.82

def bmi_new():
    return 1.3 * weight / (height ** 2.5)


def bmi_old():
    return weight / (height ** 2)

print(bmi_old(), bmi_new())

