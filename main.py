import tkinter as tk
import random
import time


class TypingSpeedTest:
    def __init__(self, window):
        self.master = window
        self.master.title("Typing Speed Test")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful programming language.",
            "Coding is fun and challenging.",
            "Practice makes perfect."
        ]

        self.current_sentence = random.choice(self.sentences)

        self.label_sentence = tk.Label(window, text=self.current_sentence, font=("Helvetica", 14))
        self.label_sentence.pack(pady=10)

        self.entry = tk.Entry(window, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.start_time = None
        self.timer_label = tk.Label(window, text="Time: 0.0 seconds", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.start_button = tk.Button(window, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

    def start_typing_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.current_sentence)

        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.master.bind("<Return>", self.check_typing_speed)
        self.update_timer()

    def check_typing_speed(self, event):
        if self.start_time:
            end_time = time.time()
            elapsed_time = round(end_time - self.start_time, 2)

            user_input = self.entry.get()
            if user_input == self.current_sentence:
                wpm = self.calculate_wpm(elapsed_time)
                result_text = f"Typing speed: {wpm} WPM"
            else:
                result_text = "Incorrect! Try again."

            self.timer_label.config(text=f"Time: {elapsed_time} seconds | {result_text}")
            self.start_time = None
            self.master.unbind("<Return>")

    def update_timer(self):
        if self.start_time:
            elapsed_time = round(time.time() - self.start_time, 2)
            self.timer_label.config(text=f"Time: {elapsed_time} seconds")
            self.master.after(100, self.update_timer)

    def calculate_wpm(self, elapsed_time):
        words_per_minute = (len(self.current_sentence.split()) / elapsed_time) * 60
        return round(words_per_minute)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
