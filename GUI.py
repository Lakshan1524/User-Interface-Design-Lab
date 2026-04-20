import tkinter as tk
import os
import webbrowser

def open_app():
    app = entry.get().lower().strip()

    if app == "calculator":
        os.system("calc")
        status.set("Calculator opened")

    elif app == "notepad":
        os.system("notepad")
        status.set("Notepad opened")

    elif app == "youtube":
        webbrowser.open("https://www.youtube.com")
        status.set("YouTube opened")

    elif app == "gmail":
        webbrowser.open("https://mail.google.com")
        status.set("Gmail opened")

    elif app == "whatsapp":
        os.system("start whatsapp:")
        status.set("WhatsApp opened")

    elif app == "telegram":
        os.system("start telegram:")
        status.set("Telegram opened")

    elif app == "copilot":
        webbrowser.open("https://copilot.microsoft.com")
        status.set("Copilot opened")

    else:
        status.set("Invalid app name")

root = tk.Tk()
root.title("App Launcher")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="App Launcher", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter app name:", font=("Arial", 11)).pack()

entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

tk.Button(root, text="Open App", font=("Arial", 11), width=15, command=open_app).pack(pady=10)

status = tk.StringVar()
tk.Label(root, textvariable=status, font=("Arial", 10), fg="blue").pack(pady=5)

tk.Label(root, text="Examples: calculator, whatsapp, youtube", font=("Arial", 9), fg="gray").pack()

root.mainloop()
