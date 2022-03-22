from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



question_bank = []
for questions in question_data :
    question = Question(questions["text"], questions["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was : {quiz.score}/{quiz.question_number}")
