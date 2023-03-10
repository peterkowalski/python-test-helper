"""Dummy docstring."""
import curses
import random


def picking_random_elements(elements: list, list_amount: int):
    """Picks random values from list without repetitions
    Args:
    list: list of elements
    list_amount: amount of random picked elements
    """
    random_numbers = range(0, len(elements))
    random_elements = random.sample(random_numbers, list_amount)
    return random_elements


def checking_answers(answer: str, correct_answer: str):
    """Checks if given answer is correct with const (works for upper and lower
    letters)
        Args:
        answer: given answer
        correct_answer: correct uppercase answer
    """
    if answer.upper() == correct_answer:
        print("POPRAWNA ODPOWIEDŹ")
        return True
    else:
        print("NIEPOPRAWNA ODPOWIEDŹ")
        return False


def saving_into_file(questions: list, answers: list, correct_answers: list):
    """Save elements from 3 given lists into file with ';' suffix after values
    Args:
    questions: list of questions
    answers: list of answers
    correct_answers: list of correct answers associated with questions
    """
    with open("questions.txt", "w") as f:
        for i in range(len(questions)):
            f.write(
                "{};{};{}\n".format(
                    questions[i], ";".join(answers[i]), correct_answers[i]
                )
            )


def reading_from_file(questions: list, answers: list, correct_answers: list):
    """Reading elements from file 'questions.txt'

    Args:
        questions (list): questions list
        answers (list): answers list
        correct_answers (list): correct answers list
    """
    try:
        f = open("questions.txt", "r")

    except IOError:
        print(
            "Nie mozna otworzyć pliku, sprawdź czy znajduje się w odpowiedniej ściezce..."
        )
    line_container = []
    try:
        for line in f:
            line_container = line.split(";")
            questions.append(line_container[0])
            answers.append(line_container[1 : len(line_container) - 1])
            correct_answers.append(line_container[len(line_container) - 1].strip())
    except EOFError:
        print("Plik jest pusty, nie mozna odczytać pytań...")
    except IndexError:
        print("Plik z pytaniami zawiera dane w złym formacie...")
        print("Poprawny format:")
        print("[pytanie] ;[odp1] ;[odp2];[odp3] ;[odp-N] ;[poprawna odp]")


def adding_new_questions(questions: list, answers: list, correct_answers: list):
    """Function adding new questions from user while whole program is running

    Args:
        questions (list): list of questions
        answers (list): list of answers
        correct_answers (list): list of correct answers
    """
    while True:
        pick = str(input("Jezeli nie chcesz wprowadzać nowego pytania wpisz [N]: "))
        if pick == "N" or pick.upper() == "N":
            break
        else:
            question = str(input("Podaj pytanie jakie chcesz dodać: "))
        if question == "" or question.isnumeric() is True:
            print("Musisz podać pytanie...\n")
            continue
        else:
            break
    temp_answers = []
    itr = 1
    options = []
    while True:
        single_answer = str(
            input(
                "Podaj {} odpowiedź lub wpisz [N], aby zakończyć dodawanie: ".format(
                    itr
                )
            )
        )
        if single_answer == "":
            print("Musisz wymyślić jakąś odpowiedź...")
            continue
        elif single_answer.upper() == "N":
            break
        else:
            itr += 1
            temp_answers.append(single_answer)

    for i in range(len(temp_answers)):
        options.append(chr(65 + i))
    while True:
        print("Wskaz poprawną odpowiedź spośród - ", end="")
        for itr, i in enumerate(options):
            print("{}: {}|".format(i, temp_answers[itr]), end="")
        print(": ", end="")
        temp_correct_answer = str(input())
        if temp_correct_answer.upper() not in options:
            print("Musisz wskazać, którąś z podanych...")
            continue
        else:
            temp_correct_answer = temp_answers[
                options.index(temp_correct_answer.upper())
            ]
            break
    questions.append(question)
    answers.append(temp_answers)
    correct_answers.append(temp_correct_answer)


def saving_points_to_file(points: list, records_amount: int):
    with open("points.txt", "w") as f:
        for itr, i in enumerate(points):
            f.write(i + "\n")
            if itr > records_amount:
                break


def reading_points_from_file(points: list, records_amount: int):
    try:
        f = open("points.txt", "r")
    except IOError:
        print(
            "Nie mozna otworzyć pliku, sprawdź czy znajduje się w odpowiedniej ściezce..."
        )
    try:
        for line in f:
            points.append(line.strip())
    except EOFError:
        print("Plik jest pusty, nie mozna odczytać punktów...")
    except IndexError:
        print("Plik z pytaniami zawiera dane w złym formacie...")
        print("Poprawny format:")
        print("[punkty]/[ilość pytań]")


menu_options = ["Rozpocznij quiz", "Ostatnie wyniki", "Zamknij program"]


def main_menu(stdscr):
    attributes = {}
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes["normal"] = curses.color_pair(1)
    attributes["highlighted"] = curses.color_pair(2)
    c = 0
    option = 0
    while c != 10:
        stdscr.erase()
        stdscr.addstr("MENU GŁOWNE\n", curses.A_UNDERLINE)
        for i in range(len(menu_options)):
            if i == option:
                attr = attributes["highlighted"]
            else:
                attr = attributes["normal"]
            stdscr.addstr("{}".format(i + 1))
            stdscr.addstr(menu_options[i] + "\n", attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(menu_options) - 1:
            option += 1
    stdscr.addstr("Wybrałeś {}".format(menu_options[option]))
    stdscr.getch()
