import requests

# https://opentdb.com
question_data = []
def new_game():
    api = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean", verify=False)
    data = api.json()

    for i in range(10):
        question = data['results'][i]
        question_data.append(question)
    return question_data


question_data = new_game()
