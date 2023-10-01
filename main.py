# база вопросов в виде словарей
import random

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


def get_question():
    return random.choice(list(questions_main.items()))


def greetings(question, star_answer):
    print("Вопрос:", question)
    print(*star_answer)


def run_game(question, answer):
    star_answer = []
    for i in range(len(answer)):
        star_answer.append("*")

    greetings(question, star_answer)




if __name__ == '__main__':
    question = get_question()
    run_game(question[0], question[1])
