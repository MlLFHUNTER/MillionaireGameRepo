import random
import pygame
import time

pygame.mixer.init()
correct_sound = pygame.mixer.Sound("khsm_q6-correct.mp3")
wrong_sound = pygame.mixer.Sound("khsm_q6-wrong.mp3")
fifty_sound = pygame.mixer.Sound("khsm_50-50.mp3")
total_win_sound = pygame.mixer.Sound("khsm_q10-correct.mp3")


class Game:
    def __init__(self):
        self.questions = [
            {
                "question": "Яка столиця Франції?",
                "options": ["А) Лондон", "Б) Рим", "В) Париж", "Г) Берлін"],
                "correct_answer": "В"
            },
            {
                "question": "Скільки планет у Сонячній системі?",
                "options": ["А) 8", "Б) 9", "В) 10", "Г) 7"],
                "correct_answer": "А"
            },
            {
                "question": "Що з цих тварин літає?",
                "options": ["А) Слон", "Б) Кіт", "В) Птах", "Г) Змія"],
                "correct_answer": "В"
            },
            {
                "question": "Яка ріка є найдовшою у світі?",
                "options": ["А) Амазонка", "Б) Ніл", "В) Янцзи", "Г) Міссісіпі"],
                "correct_answer": "А"
            },
            {
                "question": "Яка столиця України?",
                "options": ["А) Київ", "Б) Львів", "В) Харків", "Г) Одеса"],
                "correct_answer": "А"
            },
            {
                "question": "Який хімічний елемент позначається символом 'O'?",
                "options": ["А) Кисень", "Б) Вуглець", "В) Гелій", "Г) Азот"],
                "correct_answer": "А"
            },
            {
                "question": "Яка планета Сонячної системи має найбільшу кількість супутників?",
                "options": ["А) Земля", "Б) Юпітер", "В) Сатурн", "Г) Марс"],
                "correct_answer": "Б"
            },
            {
                "question": "Як називається найбільша пустеля на Землі?",
                "options": ["А) Сахара", "Б) Атакама", "В) Гобі", "Г) Аравійська пустеля"],
                "correct_answer": "А"
            },
            {
                "question": "Хто написав трагедію 'Ромео і Джульєтта'?",
                "options": ["А) Вільям Шекспір", "Б) Микола Гоголь", "В) Марк Твен", "Г) Федір Достоєвський"],
                "correct_answer": "А"
            },
            {
                "question": "Скільки континентів на планеті Земля?",
                "options": ["А) 5", "Б) 6", "В) 7", "Г) 8"],
                "correct_answer": "В"
            },
            {
                "question": "Який найбільший океан на Землі?",
                "options": ["А) Атлантичний океан", "Б) Тихий океан", "В) Індійський океан",
                            "Г) Північний Льодовитий океан"],
                "correct_answer": "Б"
            },
            {
                "question": "Хто зображений на найпоширенішій купюрі Української гривні?",
                "options": ["А) Богдан Хмельницький", "Б) Тарас Шевченко", "В) Іван Франко", "Г) Володимир Великий"],
                "correct_answer": "Б"
            },
            {
                "question": "Що означає абревіатура 'DNA'?",
                "options": ["А) Діоксид азоту", "Б) Дезоксирибонуклеїнова кислота", "В) Дика наука автоматизації", "Г) "
                            "Дискретна"
                            "навігаційна апаратура"],
                "correct_answer": "Б"
            },
            {
                "question": "Яка найбільша гора на Землі?",
                "options": ["А) Еверест", "Б) Кіліманджаро", "В) Аконкагуа", "Г) Маккінлі"],
                "correct_answer": "А"
            },
        ]
        self.now_hint = ""
        self.list_with_prizes = [1000, 5000, 10000, 20000, 50000, 100000, 300000, 500000, 1000000]
        self.hints = [
            "50/50 (залишиться тільки два варіанти відповідей)",
            "зателефонувати другу (ви можете зателефонувати другу та попросити допомоги)",
            "Підказка залу (глядачі дадуть свою відповідь)",
        ]
        self.used_hints = []
        self.correct_answers = 0
        self.current_prize = 0
        self.current_question = None

    # This function get random question from a list
    def get_random_question(self):
        return random.choice(self.questions)

    # This function show the random question from past function
    @staticmethod
    def show_question(questions):
        print(questions["question"])
        time.sleep(1)
        for option in questions["options"]:
            print(option)
            time.sleep(1)

    # func for getting hint
    def get_hint(self):
        hint = random.choice(self.hints)
        self.hints.remove(hint)
        self.used_hints.append(hint)
        if hint:
            if hint == "50/50 (залишиться тільки два варіанти відповідей)":
                self.now_hint = "50/50"

            if hint == "зателефонувати другу (ви можете зателефонувати другу та попросити допомоги)":
                self.now_hint = "дзвінок"

            if hint == "Підказка залу (глядачі дадуть свою відповідь)":
                self.now_hint = "допомога залу"
            return hint

        else:
            return "На жаль, більше підказок немає."

    # 50/50 hint
    def fifty(self, question):
        if self.used_hints != 3:
            options = self.current_question["options"]
            correct_answer = self.current_question["correct_answer"]
            i = 0
            while len(options) != 2:
                if options[i][0] == correct_answer:
                    i += 1
                    continue
                else:
                    options.pop(i)
                i += 1
            return {
                "question": self.current_question["question"],
                "options": options,
            }
        else:
            return "У вас більше немає підказок"

    def call_friend(self):
        if self.used_hints != 3:
            correct_answer = self.current_question["correct_answer"]
            wrong_answers = []
            if random.randint(0, 10) > 5:
                time.sleep(1)
                return f"Я вважаю що правильна відповідь: {correct_answer}"
            else:
                for i in self.current_question["options"]:
                    if i == correct_answer:
                        continue
                    else:
                        wrong_answers.append(i)
                        return f"Я вважаю що правильна відповідь: {random.choice(wrong_answers)}"
        else:
            return "У вас більшe немає підказок"

    @staticmethod
    def help_of_audience(self, question):
        cur_quest = self.current_question
        all_votes = 100
        cor_votes = random.randint(40, 70)
        wrg_votes = all_votes - cor_votes
        wrg1 = random.randint(0, wrg_votes)
        wrg2 = random.randint(0, wrg_votes - wrg1)
        wrg3 = random.randint(0, wrg_votes - (wrg2 + wrg1))
        lst_with_vot = [cor_votes, wrg1, wrg2, wrg3]
        random.shuffle(lst_with_vot)
        for i, option in enumerate(cur_quest["options"]):
            print(f'{option}: {lst_with_vot[i]}%')

    def validating(self, user_answer):
        correct_answer = self.current_question["correct_answer"]
        if user_answer.upper() == correct_answer:
            self.correct_answers += 1
            self.current_prize = self.list_with_prizes[self.correct_answers - 1]
            return True
        else:

            return False

    def play(self):
        print("Вітаємо у грі 'Хто хоче стати мільйонером?'")
        print("Ви отримаєте суму грошей за кожну правильну відповідь.")
        print("Якщо ви відповісте неправильно, гра закінчиться, і ви заберете останню суму грошей.")
        print("Під час гри ви зможете скористатись підказками.")
        print("Починаємо!")
        print(8 * "*", "Перше питання", 8 * "*")
        time.sleep(1.5)

        while self.current_prize != self.list_with_prizes[-1]:
            self.current_question = self.get_random_question()
            self.show_question(self.current_question)
            self.questions.remove(self.current_question)

            while 1:
                print("Введіть 'підказка' для використвння випадкової підказки")
                user_answer = input("Оберіть відповідь(Введіть букву): ")

                if user_answer == "підказка":
                    if self.hints:
                        print(self.get_hint())
                        fifty_sound.play()
                    else:
                        print("Більше підказок немає")

                elif self.validating(user_answer):
                    print(f"Вітаємо! Ви відповіли правильно і виграли {self.current_prize} грн.")
                    print(f"Загальний виграш становить: {self.current_prize} грн.")
                    correct_sound.play()
                    break
                else:
                    print("Вибачте, відповідь неправильна. Гра закінчена.")
                    print(f"Ваш виграш становить: {self.current_prize} грн.")
                    time.sleep(2)
                    wrong_sound.play()
                    return

                if self.now_hint == "50/50":
                    self.now_hint = ""
                    print(self.fifty(self.current_question))
                elif self.now_hint == "дзвінок":
                    self.now_hint = ""
                    print(self.call_friend())
                elif self.now_hint == "допомога залу":
                    self.now_hint = ""
                    self.help_of_audience(self, self.current_question)

            time.sleep(2)
            print(8 * "*", "Наступне питання", 8 * "*")

        print("Вітаємо! Ви відповіли правильно на всі питання!")
        print(f"Ваш загальний виграш становить: {sum(self.list_with_prizes)} грн.")
        print("Дякуємо за гру!")
        total_win_sound.play()


while True:
    game1 = Game()
    game1.play()
