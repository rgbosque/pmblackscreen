# Company: Openmedia.io
# Date: 10/08/2022
# Developer: Rodel G. Bosque
# Version: Beta

import os
import csv


def continue_process():
    while True:
        selection = input("Continue? [Y/N]: ").upper()
        if selection == "Y":
            menu()
            break
        elif selection == "N":
            system_info()
            break
        else:
            print("Select on selection only!")


def find_keyword():
    os.system("cls")

    data_rec = []
    dict_rec = {}
    keyword = input("Keyword: ")

    # this is where the data will retrieve
    with open("data.csv",  newline='') as csvfile:
        reader = csv.reader(csvfile)

        for tools, data in reader:
            data_rec.append({"tools": tools, "data": data})

        for rec in data_rec:
            if rec['tools'].upper() == keyword.upper():
                print(f"Tools: {rec['tools']}")
                print(f"Info: {rec['data']}")
                print("========================")
                # break
    continue_process()


def add_keyword():
    os.system("cls")
    print("Please enter your details.")
    tools = input("Tools: ").upper()
    username = input("username: ")
    hint = input("hint: ")
    data_rec = []

    save_record = input("Save this [Y/N]? ").upper()
    if save_record == "Y":
        with open("data.csv", "a", newline='') as csvfile:
            fieldnames = ['tools', 'data']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'tools': tools, 'data': {'username': username, 'hint': hint}})
    elif save_record == "N":
        pass

    continue_process()


def system_info():
    os.system("cls")
    print("Thank you for using PM Blackscreen!")
    print("Version: Beta")
    print("Developer: Openmedia.io")
    print("Email: openmediaio@gmail.com")
    print("Copyright @ 2022 Openmedia.io")


def menu():
    while True:
        os.system("cls")
        print("========================")
        print("**** PM Blackscreen ****")
        print("========================")
        print("[F] - Find")
        print("[A] - Add Keyword")
        print("[Q] - Quit")
        print("========================")
        selection = input(">>> ").upper()

        if selection == "Q":
            os.system("cls")
            system_info()
            break
        elif selection == "F":
            find_keyword()
            break
        elif selection == "A":
            add_keyword()
            break


def main():
    menu()


if __name__ == "__main__":
    main()
