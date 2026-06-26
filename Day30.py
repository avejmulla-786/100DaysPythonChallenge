# KBC Game 

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B",
        "prize": 1000
    },
    {
        "question": "2. Which language is used for AI and Data Science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. XML"],
        "answer": "A",
        "prize": 5000
    },
    {
        "question": "3. Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C",
        "prize": 10000
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
        "prize": 50000
    },
    {
        "question": "5. What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Power Unit",
            "D. Control Processing Unit"
        ],
        "answer": "A",
        "prize": 100000
    }
]

money = 0

print("=" * 50)
print("      WELCOME TO KBC")
print("=" * 50)

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        money = q["prize"]
        print(" Correct!")
        print(f"You won ₹{money}")
    else:
        print(" Wrong Answer!")
        print(f"Correct Answer: {q['answer']}")
        print(f"Game Over! You take home ₹{money}")
        break

else:
    print("\n Congratulations!")
    print(f"You became the KBC Champion and won ₹{money}")