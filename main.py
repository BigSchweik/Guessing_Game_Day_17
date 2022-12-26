from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.ask_question()
    print(f"Your score is: {quiz.score}/{quiz.question_number}")
    print("\n")
score_percent = round((quiz.score/quiz.question_number) * 100, 2)
print("You've completed the quiz")

if score_percent > 90:
    print("You're a fucking Genius")
print(f"Your final score is {score_percent}%")