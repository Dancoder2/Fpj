#Author: Dan Olufemi
#Date written:07/11/2025
#Assignment: Project
#Short Desc: This program chooses randomly from different ganes and display it.
import tkinter as tk
from tkinter import messagebox
import random
import json
from PIL import Image, ImageTk

def load_unlock_data():
    try:
        with open("unlocks.json", "r") as f:
            return json.load(f)
    except Exception:
        return {"points": 0, "unlocked_games": ["Fast Typing", "Math Quiz", "Guess the Word", "Click Counter"]}

def save_unlock_data(data):
    with open("unlocks.json", "w") as f:
        json.dump(data, f)

unlock_data = load_unlock_data()

root = tk.Tk()
root.title("Wheel of Fun")
root.geometry("600x500")

display_result = tk.StringVar()
bg_label = None

try:
    bg = Image.open("background.jpg").resize((600, 500))
    bg = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg
except Exception:
    root.configure(bg="white")

if bg_label:
    bg_label.lower()

wheel_frame = tk.Frame(root, width=300, height=300)
wheel_frame.place(relx=0.5, rely=0.3, anchor="center")


def load_game_bg(win, image_path="background.jpg"):
    try:
        bg_img = Image.open(image_path).resize((600, 500))
        bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(win, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        win.bg_color = None
        bg_label.lower()
    except Exception:
        win.configure(bg="lightgray")
        win.bg_color = "lightgray"

def award_points(amount):
    unlock_data["points"] += amount
    save_unlock_data(unlock_data)
    points_label.config(text=f"Points: {unlock_data['points']}")
    messagebox.showinfo("Points", f"You earned {amount} points!")

def is_unlocked(name):
    return name in unlock_data["unlocked_games"]

game_emojis = {
    "Fast Typing": "⌨️",
    "Math Quiz": "➕",
    "Guess the Word": "❓",
    "Click Counter": "🖱️",
    "True or False": "✔️❌",
    "Quick Tap": "⚡",
    "Maze": "🌀",
    "Color Click": "🎨",
    "Number Guess": "🔢",
    "Simon Says": "🔴🟢🔵🟡",
    "Word Scramble": "🔤"
}

def fast_typing_game(on_win=None):
    win = tk.Toplevel()
    win.title("Fast Typing")
    load_game_bg(win)
    phrase = "Type this phrase quickly"
    answered = [False]

    def check():
        if answered[0]:
            return
        answered[0] = True
        if entry.get().strip().lower() == phrase.lower():
            result.config(text="Correct!")
            if on_win:
                on_win(5)
        else:
            result.config(text="Wrong")
        win.after(1500, win.destroy)

    bgc = getattr(win, "background", "white")
    tk.Label(win, text=phrase, bg=bgc).pack(pady=10)
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Submit", command=check).pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def math_quiz_game(on_win=None):
    win = tk.Toplevel()
    win.title("Math Quiz")
    load_game_bg(win)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*", "/"])
    if op == "/":
        a *= b
    expr = f"{a} {op} {b}"
    ans = round(eval(expr), 2)
    answered = [False]
    def check():
        if answered[0]:
            return
        answered[0] = True
        try:
            val = float(entry.get())
            if abs(val - ans) < 0.01:
                result.config(text="Correct")
                if on_win:
                    on_win(5)
            else:
                result.config(text="Wrong")
        except:
            result.config(text="Invalid input")
        win.after(1500, win.destroy)
    bgc = getattr(win, "background", "white")
    tk.Label(win, text=f"What is {expr}?", bg=bgc).pack(pady=5)
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Submit", command=check).pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def guess_the_word_game(on_win=None):
    win = tk.Toplevel()
    win.title("Guess the Word")
    load_game_bg(win)
    words = ["apple", "banana", "cherry"]
    answer = random.choice(words)
    scrambled = "".join(random.sample(answer, len(answer)))
    answered = [False]
    def check():
        if answered[0]:
            return
        answered[0] = True
        if entry.get().strip().lower() == answer:
            result.config(text="Correct!")
            if on_win:
                on_win(5)
        else:
            result.config(text=f"Wrong! Answer was {answer}")
        win.after(2000, win.destroy)
    bgc = getattr(win, "background", "white")
    tk.Label(win, text=f"Unscramble this word: {scrambled}", bg=bgc).pack(pady=10)
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Submit", command=check).pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def click_counter_game(on_win=None):
    win = tk.Toplevel()
    win.title("Click Counter")
    load_game_bg(win)
    clicks = [0]
    time_left = [10]
    answered = [False]
    def click():
        if answered[0]:
            return
        clicks[0] += 1
        label.config(text=f"Clicks: {clicks[0]}")
    def countdown():
        if time_left[0] <= 0:
            answered[0] = True
            if on_win:
                on_win(clicks[0])
            win.destroy()
            return
        time_left[0] -= 1
        timer_label.config(text=f"Time left: {time_left[0]}s")
        win.after(1000, countdown)
    bgc = getattr(win, "background", "white")
    label = tk.Label(win, text="Clicks: 0", font=("Arial", 16), bg=bgc)
    label.pack(pady=10)
    btn = tk.Button(win, text="Click me!", font=("Arial", 14), command=click)
    btn.pack(pady=10)
    timer_label = tk.Label(win, text="Time left: 10s", font=("Arial", 14), bg=bgc)
    timer_label.pack()
    countdown()
    win.focus_set()
    win.grab_set()

def true_false_game(on_win=None):
    win = tk.Toplevel()
    win.title("True or False")
    load_game_bg(win)
    question = "Python is a programming language."
    correct_answer = True
    answered = [False]
    bgc = getattr(win, "background", "white")
    tk.Label(win, text=question, bg=bgc).pack(pady=5)
    def answer(val):
        if answered[0]:
            return
        answered[0] = True
        if val == correct_answer:
            result.config(text="Correct!")
            if on_win:
                on_win(5)
        else:
            result.config(text="Wrong")
        true_btn.config(state="disabled")
        false_btn.config(state="disabled")
        win.after(1500, win.destroy)
    true_btn = tk.Button(win, text="True", command=lambda: answer(True))
    true_btn.pack()
    false_btn = tk.Button(win, text="False", command=lambda: answer(False))
    false_btn.pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def quick_tap_game(on_win=None):
    win = tk.Toplevel()
    win.title("Quick Tap")
    load_game_bg(win)
    clicks = [0]
    answered = [False]
    def tap():
        if answered[0]:
            return
        clicks[0] += 1
        label.config(text=f"Taps: {clicks[0]}")
        if clicks[0] >= 20:
            answered[0] = True
            if on_win:
                on_win(10)
            win.after(1000, win.destroy)
    bgc = getattr(win, "background", "white")
    label = tk.Label(win, text="Taps: 0", font=("Arial", 16), bg=bgc)
    label.pack(pady=10)
    btn = tk.Button(win, text="Tap me!", font=("Arial", 14), command=tap)
    btn.pack(pady=10)
    win.focus_set()
    win.grab_set()

def maze_game(on_win=None):
    win = tk.Toplevel()
    win.title("Maze")
    load_game_bg(win)
    label = tk.Label(win, text="Maze game coming soon!", font=("Arial", 18))
    label.pack(pady=100)
    def close():
        if on_win:
            on_win(10)
        win.destroy()
    tk.Button(win, text="Finish Maze", command=close).pack()
    win.focus_set()
    win.grab_set()

def color_click_game(on_win=None):
    win = tk.Toplevel()
    win.title("Color Click")
    load_game_bg(win)
    colors = ["red", "green", "blue", "yellow"]
    current_color = [random.choice(colors)]
    clicks = [0]
    answered = [False]
    def next_color():
        current_color[0] = random.choice(colors)
        btn.config(bg=current_color[0])
    def click():
        if answered[0]:
            return
        clicks[0] += 1
        if clicks[0] >= 10:
            answered[0] = True
            if on_win:
                on_win(10)
            win.after(1000, win.destroy)
            return
        next_color()
    bgc = getattr(win, "background", "white")
    btn = tk.Button(win, text="Click me", bg=current_color[0], font=("Arial", 14), command=click)
    btn.pack(pady=100)
    win.focus_set()
    win.grab_set()

def number_guess_game(on_win=None):
    win = tk.Toplevel()
    win.title("Number Guess")
    load_game_bg(win)
    number = random.randint(1, 20)
    attempts = [0]
    answered = [False]
    bgc = getattr(win, "background", "white")
    def check():
        if answered[0]:
            return
        try:
            guess = int(entry.get())
        except:
            result.config(text="Enter a valid number")
            return
        attempts[0] += 1
        if guess == number:
            answered[0] = True
            result.config(text=f"Correct! Attempts: {attempts[0]}")
            if on_win:
                on_win(10)
            win.after(1500, win.destroy)
        elif guess < number:
            result.config(text="Too low!")
        else:
            result.config(text="Too high!")
    tk.Label(win, text="Guess a number between 1 and 20", bg=bgc).pack(pady=10)
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Guess", command=check).pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def simon_says_game(on_win=None):
    win = tk.Toplevel()
    win.title("Simon Says")
    load_game_bg(win)
    colors = ["red", "green", "blue", "yellow"]
    pattern = []
    user_pattern = []
    answered = [False]
    bgc = getattr(win, "background", "white")

    def next_round():
        pattern.append(random.choice(colors))
        label.config(text="Watch the pattern")
        btn_frame.after(1000, show_pattern, 0)

    def show_pattern(i):
        if i < len(pattern):
            color = pattern[i]
            btns[color].config(relief="sunken")
            btn_frame.after(500, lambda: btns[color].config(relief="raised"))
            btn_frame.after(600, show_pattern, i + 1)
        else:
            label.config(text="Repeat the pattern")
            user_pattern.clear()

    def button_click(color):
        if answered[0]:
            return
        user_pattern.append(color)
        idx = len(user_pattern) - 1
        if user_pattern[idx] != pattern[idx]:
            answered[0] = True
            label.config(text="Wrong! Game over")
            win.after(1500, win.destroy)
            return
        if len(user_pattern) == len(pattern):
            if len(pattern) == 5:
                answered[0] = True
                label.config(text="You won!")
                if on_win:
                    on_win(15)
                win.after(1500, win.destroy)
            else:
                label.config(text="Good! Next round")
                btn_frame.after(1000, next_round)

    label = tk.Label(win, text="Simon Says", font=("Arial", 16), bg=bgc)
    label.pack(pady=10)
    btn_frame = tk.Frame(win)
    btn_frame.pack()
    btns = {}
    for color in colors:
        b = tk.Button(btn_frame, bg=color, width=6, height=3,
                      command=lambda c=color: button_click(c))
        b.pack(side="left", padx=5, pady=5)
        btns[color] = b
    win.after(1000, next_round)
    win.focus_set()
    win.grab_set()

def word_scramble_game(on_win=None):
    win = tk.Toplevel()
    win.title("Word Scramble")
    load_game_bg(win)
    words = ["python", "banana", "computer", "elephant", "flower"]
    answer = random.choice(words)
    scrambled = "".join(random.sample(answer, len(answer)))
    answered = [False]

    def check():
        if answered[0]:
            return
        answered[0] = True
        if entry.get().strip().lower() == answer:
            result.config(text="Correct!")
            if on_win:
                on_win(10)
        else:
            result.config(text=f"Wrong! Answer was {answer}")
        win.after(2000, win.destroy)

    bgc = getattr(win, "background", "white")
    tk.Label(win, text=f"Unscramble this word: {scrambled}", bg=bgc).pack(pady=10)
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Submit", command=check).pack()
    result = tk.Label(win, text="", bg=bgc)
    result.pack()
    win.focus_set()
    win.grab_set()

def show_lock_popup(name, cost, function):
    win = tk.Toplevel()
    win.title(f"{name} Locked")
    tk.Label(win, text=f"{game_emojis.get(name, '')} {name} is locked").pack(pady=5)
    tk.Label(win, text=f"Unlock for {cost} points?").pack(pady=5)
    tk.Label(win, text="🔒", font=("Arial", 50)).pack(pady=10)
    def unlock():
        if unlock_data["points"] >= cost:
            unlock_data["points"] -= cost
            if name not in unlock_data["unlocked_games"]:
                unlock_data["unlocked_games"].append(name)
            save_unlock_data(unlock_data)
            points_label.config(text=f"Points: {unlock_data['points']}")
            win.destroy()
            messagebox.showinfo("Unlocked", f"{name} unlocked!")
            if function:
                function(on_win=award_points)
        else:
            messagebox.showwarning("Not enough points", "You need more points")
    tk.Button(win, text="Unlock", command=unlock).pack(pady=5)
    tk.Button(win, text="Cancel", command=win.destroy).pack()

def spin_wheel():
    result = random.choice(games_list)
    name = result["name"]
    display_result.set(f"Landed on: {game_emojis.get(name, '')} {name}")
    if is_unlocked(name):
        if result["function"]:
            result["function"](on_win=award_points)
        else:
            messagebox.showinfo("Info", f"{name} is ready but not yet implemented.")
    else:
        show_lock_popup(name, result["cost"], result["function"])

games_list = [
    {"name": "Fast Typing", "function": fast_typing_game, "cost": 0},
    {"name": "Math Quiz", "function": math_quiz_game, "cost": 0},
    {"name": "Guess the Word", "function": guess_the_word_game, "cost": 0},
    {"name": "Click Counter", "function": click_counter_game, "cost": 200},
    {"name": "True or False", "function": true_false_game, "cost": 0},
    {"name": "Quick Tap", "function": quick_tap_game, "cost": 15},
    {"name": "Maze", "function": maze_game, "cost": 100},
    {"name": "Color Click", "function": color_click_game, "cost": 100},
    {"name": "Number Guess", "function": number_guess_game, "cost": 0},
    {"name": "Simon Says", "function": simon_says_game, "cost": 100},
    {"name": "Word Scramble", "function": word_scramble_game, "cost": 100}
]

tk.Label(root, text="Wheel of Fun", font=("Arial", 18), bg="white").pack(pady=10)
tk.Button(root, text="Spin", font=("Arial", 14), command=spin_wheel).pack(pady=20)
tk.Label(root, textvariable=display_result, font=("Arial", 14), bg="white").pack(pady=10)
points_label = tk.Label(root, text=f"Points: {unlock_data['points']}", font=("Arial", 12), bg="white")
points_label.pack()

root.mainloop()
