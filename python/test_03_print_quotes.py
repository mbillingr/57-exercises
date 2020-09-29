from python.exercise_03_print_quotes import construct_quote


def test_full_program():
    quote = "These aren't the droids you're looking for."
    author = "Obi-Wan Kenobi"

    quotation = construct_quote(author, quote)

    assert quotation == "Obi-Wan Kenobi says, \"These aren't the droids you're looking for.\""
