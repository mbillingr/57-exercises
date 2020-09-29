from python.exercise_04_madlib import construct_story


def test_story():
    story = construct_story(
        noun='dog',
        verb='walk',
        adjective='blue',
        adverb='quickly'
    )

    assert story == "Do you walk your blue dog quickly? That's hilarious!"


def test_different_story():
    story = construct_story(
        noun='spaceship',
        verb='wrestle',
        adjective='accidental',
        adverb='fiercely'
    )

    assert story == "Do you wrestle your accidental spaceship fiercely? That's hilarious!"
