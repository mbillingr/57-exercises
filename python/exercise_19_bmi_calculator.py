
def calculate_bmi(weight: float, height: float) -> float:
    return 703.0 * weight / height**2


def classify_bmi(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi > 25:
        return 'overweight'
    else:
        return 'ideal'
