from python.exercise_17_alcotest import Person, legal_to_drive


def test_bac_is_zero_after_no_drinks():
    person = Person(alcohol_consumed=0)

    bac = person.compute_bac()

    assert bac == 0


def test_bac_right_after_drink():
    person = Person(body_weight=1, alcohol_distribution_ratio=1.0).consume(1)

    bac = person.compute_bac()

    assert bac == 5.14


def test_bac_depends_on_time():
    time_passed = 1
    person = Person(body_weight=1, alcohol_distribution_ratio=1.0).consume(1).pass_time(time_passed)

    bac = person.compute_bac()

    assert bac == 5.14 - 0.015 * time_passed


def test_bac_depends_on_consumed_amount():
    alcohol_consumed = 2
    person = Person(body_weight=1, alcohol_distribution_ratio=1.0).consume(alcohol_consumed)

    bac = person.compute_bac()

    assert bac == 5.14 * alcohol_consumed


def test_bac_depends_on_weight():
    body_weight = 2
    person = Person(body_weight=body_weight, alcohol_distribution_ratio=1.0).consume(1)

    bac = person.compute_bac()

    assert bac == 5.14 / body_weight


def test_bac_depends_on_distribution_ratio():
    alcohol_distribution_ratio = 0.5
    person = Person(body_weight=1, alcohol_distribution_ratio=alcohol_distribution_ratio).consume(1)

    bac = person.compute_bac()

    assert bac == 5.14 / alcohol_distribution_ratio


def test_bac_for_male():
    person = Person.male(body_weight=1).consume(1)

    bac = person.compute_bac()

    assert bac == 5.14 / 0.73


def test_bac_for_female():
    person = Person.female(body_weight=1).consume(1)

    bac = person.compute_bac()

    assert bac == 5.14 / 0.66


def test_not_legal_to_drive():
    assert not legal_to_drive(bac=0.08)


def test_legal_to_drive():
    assert legal_to_drive(bac=0.0799)


def test_person_legal_to_drive():
    person = Person.female(body_weight=120)
    assert person.legal_to_drive()


def test_person_illegal_to_drive():
    person = Person.male(body_weight=210).consume(42)
    assert not person.legal_to_drive()
