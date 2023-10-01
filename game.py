import random


class Game:
    questions_main = {
        "Язык программирования (русским алфавитом)": "фортран",
        "Устройство вывода информации": "принтер",
        "Электронная схема, управляющая внешним устройством": "контроллер",
        "Разъемы подключения внешних устройств": "интерфейс"
    }
    questions_final = {
        "Тип пометки, используемый для быстрого нахождения пользователей и фотографии": "хэштег",
        " Процесс разметки компьютерного диска — разбиения его на логические части сектора, дорожки и их пометка": "форматирование",
        "дин из простейших логических элементов, который преобразует значение в другое ему противоположное": "инвертор",
        "Наука об общих свойствах процессов управления в живых и неживых системах": "кибернетика"
    }

    scores = [100, 200, 300, 400, 500, 0, "next", "Б"]

    score1 = 0
    score2 = 0
    gameOver = False
    player = 0
    break_main = False

    answer = ""
    star_answer = []
    question = ""

    def get_question(self):
        choice = random.choice(list(self.questions_main.items()))
        self.question = choice[0]
        self.answer = choice[1]

        self.star_answer = []
        for i in range(len(self.answer)):
            self.star_answer.append("*")

    def greetings(self):
        print("Вопрос:", self.question)
        print(*self.star_answer)

    def run(self):
        question = self.get_question()
        star_answer = []
        for i in range(len(answer)):
            star_answer.append("*")

        greetings(question, star_answer)