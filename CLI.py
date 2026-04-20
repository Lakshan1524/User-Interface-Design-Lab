import os
import webbrowser

while True:
    command = input(">> ").lower()

    if command == "open youtube":
        webbrowser.open("https://www.youtube.com")

    elif command == "open gmail":
        webbrowser.open("https://mail.google.com")

    elif command == "open whatsapp":
        os.system("start whatsapp:")

    elif command == "open telegram":
        os.system("start telegram:")

    elif command == "open calculator":
        os.system("calc")

    elif command == "open notepad":
        os.system("notepad")

    elif command == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid command")