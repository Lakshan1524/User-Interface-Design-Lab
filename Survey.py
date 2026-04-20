def survey():
    print("\nUser Interface Satisfaction Survey")
    print("---------------------------------")
    print("Please rate each interface from 1 (Very Bad) to 5 (Excellent)\n")

    try:
        cli = int(input("Command Line Interface (CLI): "))
        gui = int(input("Graphical User Interface (GUI): "))
        vui = int(input("Voice User Interface (VUI): "))

        if not (1 <= cli <= 5 and 1 <= gui <= 5 and 1 <= vui <= 5):
            print("\nError: Ratings must be between 1 and 5 only.")
            return

        print("\nYour Ratings")
        print("------------")
        print(f"CLI : {cli}")
        print(f"GUI : {gui}")
        print(f"VUI : {vui}")

        average = (cli + gui + vui) / 3
        print(f"\nOverall Satisfaction Score: {average:.2f}")

    except ValueError:
        print("\nInvalid input! Please enter numeric values only.")

if __name__ == "__main__":
    survey()
