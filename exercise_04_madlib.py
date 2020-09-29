from myio import IO


def main(io):
    io.println(construct_story(
        noun=io.input("Enter a noun: "),
        verb=io.input("Enter a verb: "),
        adjective=io.input("Enter a adjective: "),
        adverb=io.input("Enter a adverb: "),
    ))


def construct_story(noun, verb, adjective, adverb):
    return f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"


if __name__ == '__main__':
    main(IO())
