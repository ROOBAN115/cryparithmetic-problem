# Cryptarithmetic Puzzle Game

A beginner-friendly Python project that solves the classic cryptarithmetic puzzle:

```text
  SEND
+ MORE
------
 MONEY
```

In a cryptarithmetic puzzle, each letter represents one digit (0–9). Different
letters must represent different digits, and a multi-digit number cannot begin
with zero.

## Requirements
- Python 3.8 or newer
- No third-party packages (uses Python's built-in `itertools` module)

## Files
- `cryptarithmetic.py` — puzzle solver and console game
- `requirements.txt` — dependency information

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python cryptarithmetic.py
   ```

4. Press Enter when prompted to display the solution.

## Expected solution

```text
  9567
+ 1085
------
 10652
```

Mapping: S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2.

## Algorithm
The program tries possible assignments of distinct digits using permutations.
It rejects assignments with a leading zero, converts the words to numbers,
and checks whether `SEND + MORE == MONEY`.

## GitHub upload
Create a new repository named `Cryptarithmetic-Puzzle-Game`, then upload
`cryptarithmetic.py`, `README.md`, and `requirements.txt`.
