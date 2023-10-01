import random


class PlayersIterator:
    def __init__(self, players):
        self.players = players
        self.current_player = -1
        self.players_status = [True] * players

    def __iter__(self):
        return self

    def check_game_over(self):
        return self.players_status.count(True) == 1

    def clear_player(self, player):
        self.players_status[player] = False

    def __next__(self):
        if self.check_game_over():
            raise StopIteration
        else:
            self.current_player = (self.current_player + 1) % self.players
            while not self.players_status[self.current_player]:
                self.current_player = (self.current_player + 1) % self.players
            return self.current_player


class Game:
    questions_main = {
        "Язык программирования (русским алфавитом)": "фортран",
        "Устройство вывода информации": "принтер",
        "Электронная схема, управляющая внешним устройством": "контроллер",
        "Разъемы подключения внешних устройств": "интерфейс"
    }

    wheel = [100, 200, 300, 400, 500, 0, "next", "Б"]

    n_players = 2
    scores = [0] * n_players
    break_main = None

    players_iterator = PlayersIterator(n_players)

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

    def run_game(self):

        for player in self.players_iterator:
            print(f'Играет Игрок-{player + 1}')
            print("Готовы ли вы назвать слово целиком? Введите 'да' или нажмите любую клавишу")
            if input().lower() == "да":
                if self.call_word(player):
                    self.break_main = player
                    break
            else:
                self.roll(player)

    def run(self):
        self.get_question()
        self.greetings()
        self.run_game()
