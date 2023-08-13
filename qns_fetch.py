import requests

class QnsFetch:
    def __init__(self):
        self.max = 20
        res = requests.get(f"https://opentdb.com/api.php?amount={self.max}&category=18&difficulty=easy&type=multiple")
        self.data = res.json()
        self.index = 0
        
    def get_qns(self):
        currentData = self.data['results'][self.index]
        self.index += 1

        return [currentData["question"], currentData["correct_answer"]]