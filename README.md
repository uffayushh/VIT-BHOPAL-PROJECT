# Password Generator

A small interactive Python script that generates a strong password composed of lowercase, uppercase, digits, and punctuation.

**Features**
- **Purpose:**: Generates a randomized strong password based on a user-specified length.
- **Character sets:**: Lowercase, Uppercase, Digits, Punctuation (from Python's `string` module).

**Requirements**
- **Python:**: Python 3.6 or newer (no external packages required).

**Usage**
1. Open PowerShell in the project directory containing `main.py`.
2. Run the script:

```powershell
python .\main.py
```

3. When prompted, enter the desired number of characters (minimum 8).

**Example session**

```
How many characters do you want in your password? 12
Strong Password:  aB3$dE4&fG1!
```

**Notes**
- The script enforces a minimum length of 8 characters.
- The generator splits the requested length into portions (lower/upper/digits/punctuation) and then shuffles the result to increase randomness. Because of rounding, the exact distribution may vary by one character.
- If you plan to request very long passwords, be aware the script indexes into the 26-character alphabet lists; in extreme cases the logic may need adjusting.

**File**
- `main.py`: The password generator script.

--
If you'd like, I can also: add a `requirements.txt`, improve the distribution logic to avoid indexing issues for large lengths, or add a flag-based CLI (e.g., `--length 16`).

AUTHOR - Ayush Pandey
