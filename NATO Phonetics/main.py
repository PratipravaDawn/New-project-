import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]: row["code"] for (index, row) in file.iterrows()}


def nato():
    name = input("Enter the message: ").upper()
    name_list = [letters for letters in name if not letters == " "]

    try:
        code_list = [nato_dict[letters] for letters in name_list]
    except KeyError:
        print("Sorry, only letters please")
        nato()
    else:
        print(code_list)

nato()
