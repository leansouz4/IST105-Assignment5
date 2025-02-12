#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
number = int(form.getvalue('number'))
text = form.getvalue('text')

def process_number(number):
    result = {}
    result["odd"] = (number % 2 != 0)
    result["cube"] = number ** 3
    return result

def process_text(text):
    result = {}
    binary = ' '.join(format(ord(c), '08b') for c in text)
    result["binary"] = binary
    result["vowel_count"] = sum(1 for c in text.lower() if c in 'aeiou')
    return result

def treasure_hunt(secret_number=42):
    result = []
    attempts = 0
    guess = None
    while guess != secret_number:
        guess = int(input(f"Attempt {attempts + 1}: Guess the secret number: "))
        attempts += 1
        if guess < secret_number:
            result.append(f"Attempt {attempts}: {guess} (Too low!)")
        elif guess > secret_number:
            result.append(f"Attempt {attempts}: {guess} (Too high!)")
    result.append(f"Attempt {attempts}: {guess} (Correct!)")
    return result

number_result = process_number(number)
text_result = process_text(text)
treasure_result = treasure_hunt()

print("Content-Type: text/html\n")
print("<html><body>")

print("<h2>Number Puzzle:</h2>")
print(f"- The number {number} is {'odd' if number_result['odd'] else 'even'}. Its cube is {number_result['cube']}.<br>")

print("<h2>Text Puzzle:</h2>")
print(f"- Binary: {text_result['binary']}<br>")
print(f"- Vowel Count: {text_result['vowel_count']}<br>")

print("<h2>Treasure Hunt:</h2>")
for line in treasure_result:
    print(f"{line}<br>")

print("</body></html>")
