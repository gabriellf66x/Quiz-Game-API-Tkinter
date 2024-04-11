from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    var_text = key['text']
    var_answer = key['answer']
    data_imported = Question(var_text, var_answer)
    # Question class objects are all being imported into question_bank, therefore calling a single object allows us
    # to use .text
    question_bank.append(data_imported)

brain = QuizBrain(question_bank)
brain.next_question()
brain.still_has_questions()













