import random
def magic_8_ball(name, question):
    answers = {
        1: "Yes - definitely",
        2: "It is decidedly so",
        3: "Without a doubt",
        4:"Reply hazy, try again",
        5: "Ask again later",
        6: "Better not tell you now",
        7: "My sources say no",
        8: "Outlook not so good",
        9: "Very doubtful",
        10: "Oracles are telling me right now",
        11: "Magic 8 Ball is under technical maintenance, try again later",
    }

    random_number = random.randint(1, len(answers))
    answer = answers.get(random_number, "Error")

    if name.strip() == "":
        return f"Question: {question}\nMagic 8-Ball's answer: {answer}"
    else:
        return f"{name} asks: {question}\nMagic 8-Ball's answer: {answer}"


if __name__ == "__main__":
    name = input("Enter your name: ")
    question = input("Ask a question: ")
    print(magic_8_ball(name, question))