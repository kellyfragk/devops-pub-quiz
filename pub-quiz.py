from enum import Enum
# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

class QuestionType(Enum):
    MULTIPLE_CHOICE = 1,
    TRUE_FALSE = 2,
    OPEN_RESPONSE = 3,

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What number was the Apollo mission that successfully put a man on the moon for the first time in human history?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Apollo 11", "B) Apollo 12", "C) Apollo 13"],
        "answer": ["A"]
    },
   {
       "question": "Our solar system is located in what galaxy?",
       "type": QuestionType.OPEN_RESPONSE,
       "answer": ["Milky Way", "milky way", "The Milky Way"]
   },
    {
        "question": "Who sang the title song for the latest Bond film, No Time to Die?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Adele", "B) Sam Smith", "C) Billie Eilish"],
        "answer": ["C"]
    },
    {
        "question": "Where was the first example of paper money used??",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) China", "B) Turkey", "C) Greece"],
        "answer": ["A"]
    },
    {
        "question": "Who is generally considered the inventor of the motor car?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Henry Ford", "B) Karl Benz", "C) Henry M. Leland"],
        "answer": ["B"]
    },
   {
       "question": "The United States is the biggest producer of oil",
       "type": QuestionType.TRUE_FALSE,
       "answer": ["True", "T"]
   },
    {
        "question": "What is the longest-running Broadway show ever?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Les Miserable", "B) The Lion King", "C) The Phantom of the Opera"],
        "answer": ["C"]
    },
]

# Initialize score and streak tracking
score = 0
total_questions = len(quiz_questions)
current_streak = 0
best_streak = 0

def multiple_choice(question):
    for option in question["options"]:
        print(option)
    return input("Your answer (A, B, C): ").strip().upper() # Ensuring the input is uppercase for comparison
def true_false(question):
    print("True (T) or False (F)?")
    return input("Your answer (T, F): ").strip().upper() # Ensuring the input is uppercase for comparison

def open_response(question):
    return input("Your answer: ").strip().upper() # Ensuring the input is uppercase for comparison


# Loop through each question
for question_num, question in enumerate(quiz_questions, 1):
    print(f"\nQuestion {question_num}/{total_questions}")
    # Display the question and options
    print(question["question"])

    if question["type"] == QuestionType.MULTIPLE_CHOICE:
        user_answer = multiple_choice(question)
    elif question["type"] == QuestionType.TRUE_FALSE:
        user_answer = true_false(question)
    else:
        user_answer = open_response(question)

     # Check if the answer is correct and update score
    if any(x.upper() == user_answer for x in question["answer"]):
        print("CORRECT!")
        score += 1
        current_streak += 1
        best_streak = max(current_streak, best_streak)
        print(f"Correct! 🎯 Current streak: {current_streak}!")
    else:
        print(f"WRONG! Clearly the correct answer was {question['answer'][0]}.")
        current_streak = 0

# Display final score with additional stats
print("\n=== Final Score ===")
print(f"You got {score} out of {total_questions} questions correct!")
percentage = (score / total_questions) * 100
print(f"That's {percentage:.1f}%!")
print(f"Best streak: {best_streak} questions in a row! 🔥")

# Add a performance message
if percentage == 100:
    print("Perfect score! 🏆")
elif percentage >= 70:
    print("Great job! 🌟")
elif percentage >= 50:
    print("Good effort! 👍")
else:
    print("Keep practicing! 📚")

# Goodbye message
print("\nThanks for playing our Pub Quiz!")
