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
        "question": "Who sang the title song for the latest Bond film, No Time to Die?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Adele", "B) Sam Smith", "C) Billie Eilish"],
        "answer": "C"
    },
    {
        "question": "Where was the first example of paper money used??",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) China", "B) Turkey", "C) Greece"],
        "answer": "A"
    },
    {
        "question": "Who is generally considered the inventor of the motor car?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Henry Ford", "B) Karl Benz", "C) Henry M. Leland"],
        "answer": "B"
    },
    {
        "question": "What is the longest-running Broadway show ever?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A) Les Miserable", "B) The Lion King", "C) The Phantom of the Opera"],
        "answer": "C"
    },
#    {
#        "question": "What is the name of this question's author?",
#        "type": QuestionType.OPEN_RESPONSE,
#        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
#        "answer": ["Glenn", "Glenn Clarke"]
#    },
#    {
#        "question": "What is the answer for True?",
#        "type": QuestionType.TRUE_FALSE,
#        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
#        "answer": ["True", "T"]
#    },
]

def multiple_choice(question):
    for option in question["options"]:
        print(option)
    return input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
def true_false(question):
    print("True (T) or False (F)?")
    return input("Your answer (T, F): ").strip().upper() # Ensuring the input is uppercase for comparison

def open_response(question):
    return input("Your answer: ").strip().upper() # Ensuring the input is uppercase for comparison

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])

    if question["type"] == QuestionType.MULTIPLE_CHOICE:
        user_answer = multiple_choice(question)
    elif question["type"] == QuestionType.TRUE_FALSE:
        user_answer = true_false(question)
    else:
        user_answer = open_response(question)

    # Check if the answer is correct
    if any(x.upper() == user_answer for x in question["answer"]):
        print("CORRECT!")
    else:
        print(f"WRONG! Clearly the correct answer was {question['answer'][0]}.")

# Goodbye message
print("Thanks for playing our Pub Quiz!")
