#text attribute
#answer attribute
from data import question_data
import random


class Question:
    def __init__(self, text, answer):
        """pulls the text and answer key values from the dictionary and assigns that values to the attribute"""
        self.text = text
        self.answer = answer


dict_list_select = random.randint(0,11)
new_q = Question(question_data[dict_list_select]['text'],question_data[dict_list_select]['answer'])


# print(new_q.text)
# print(new_q.answer)
