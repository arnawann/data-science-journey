print("===== Challenge 5 =====")

quotes = [
    "Never stop learning.",
    "Small progress is still progress.",
    "Consistency beats intensity.",
    "Data tells a story."
]

print("===== Ada 3 cara biar jadi dua baris =====")

print("===== cara 1 =====")

import random
print("Today's Motivation:")
print(random.choice(quotes))

print("===== cara 2 (menyisakan satu space) =====")
print("Today's Motivation:\n", random.choice(quotes))

print("===== cara 3 (pake f string) =====")
quote = random.choice(quotes)
print(f"Today's Motivation:\n{quote}")

