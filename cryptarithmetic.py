from itertools import permutations

def solve_send_more_money():
    """Solve SEND + MORE = MONEY using unique digits for each letter."""
    letters = "SENDMORY"

    for digits in permutations("0123456789", len(letters)):
        mapping = dict(zip(letters, digits))

        # A multi-digit number cannot start with zero.
        if mapping["S"] == "0" or mapping["M"] == "0":
            continue

        send = int("".join(mapping[ch] for ch in "SEND"))
        more = int("".join(mapping[ch] for ch in "MORE"))
        money = int("".join(mapping[ch] for ch in "MONEY"))

        if send + more == money:
            return mapping, send, more, money

    return None


def main():
    print("=" * 42)
    print("       CRYPTARITHMETIC PUZZLE GAME")
    print("=" * 42)
    print("\nSolve this puzzle:")
    print("      SEND")
    print("    + MORE")
    print("    ------")
    print("     MONEY")

    input("\nPress Enter to reveal the computer's solution...")

    result = solve_send_more_money()
    if result is None:
        print("No solution was found.")
        return

    mapping, send, more, money = result
    print("\nSolution:")
    print(f"      {send}")
    print(f"    + {more}")
    print("    ------")
    print(f"     {money}")

    print("\nLetter-to-digit mapping:")
    for letter in sorted(mapping):
        print(f"{letter} = {mapping[letter]}")

    print("\nRule: Each letter has a different digit, and S and M cannot be zero.")


if __name__ == "__main__":
    main()
