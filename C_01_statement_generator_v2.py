def statement_generator(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line)"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    print(f"{decoration * 3} {statement} {decoration * 3}")
    outer = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(outer)
    else:
        print(outer)
        print(middle)
        print(outer)

