import tkinter as tk
from tkinter import ttk
from services.admin_service import AdminService
from tkinter import messagebox

BG = "#17090d"
FIELD = "#4a2a33"
GOLD = "#d9a441"
GOLD_HOVER = "#ecbf63"
CREAM = "#f3e7d3"


FONT_TITLE = ("Arial", 30, "bold")
FONT_SECTION = ("Arial", 15, "bold")
FONT_LABEL = ("Arial", 16)
FONT_INPUT = ("Arial", 13)
FONT_BUTTON = ("Arial", 11, "bold")


class AdminPage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG)
        self.admin_service = AdminService()
        self.create_layout()

    def create_layout(self):
        field_width = 24

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TCombobox",
            fieldbackground=FIELD,
            background=GOLD,
            foreground=CREAM,
            arrowcolor=BG,
            bordercolor=FIELD,
            lightcolor=FIELD,
            darkcolor=FIELD,
            padding=3,
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", FIELD)],
            foreground=[("readonly", CREAM)],
            background=[("active", GOLD_HOVER)],
        )
        style.map("TCombobox", bordercolor=[("focus", GOLD)])
        self.option_add("*TCombobox*Listbox.background", FIELD)
        self.option_add("*TCombobox*Listbox.foreground", CREAM)
        self.option_add("*TCombobox*Listbox.selectBackground", GOLD)
        self.option_add("*TCombobox*Listbox.selectForeground", BG)
        self.option_add("*TCombobox*Listbox.font", FONT_INPUT)

        self.title_label = tk.Label(
            self, text="Admin Dashboard", font=FONT_TITLE, bg=BG, fg=GOLD
        )
        self.title_label.pack(pady=(15, 10))

        # --- Add A New Movie Section ---
        self.entry_label = tk.Label(
            self, text="Add A New Movie", font=FONT_SECTION, bg=BG, fg=CREAM
        )
        self.entry_label.pack(pady=(10, 5))

        self.input_frame = tk.Frame(self, bg=BG)
        self.input_frame.pack(pady=5)
        self.input_frame.columnconfigure(0, minsize=130)
        self.input_frame.columnconfigure(1, minsize=180)

        # Movie Title Entry
        self.movie_entry_label = tk.Label(
            self.input_frame, text="Movie Title:", font=FONT_LABEL, bg=BG, fg=CREAM
        )
        self.movie_entry_label.grid(
            row=0, column=0, sticky="e", padx=(0, 8), pady=5)

        self.movie_entry = tk.Entry(
            self.input_frame, width=field_width, font=FONT_INPUT,
            bg=FIELD, fg=CREAM, insertbackground=GOLD, relief="flat"
        )
        self.movie_entry.grid(row=0, column=1, sticky="w", padx=(8, 0), pady=5)

        # Movie Time Entry
        self.movie_time_entry_label = tk.Label(
            self.input_frame, text="Movie Time:", font=FONT_LABEL, bg=BG, fg=CREAM
        )
        self.movie_time_entry_label.grid(
            row=1, column=0, sticky="e", padx=(0, 8), pady=5)

        self.movie_time_entry = tk.Entry(
            self.input_frame, width=field_width, font=FONT_INPUT,
            bg=FIELD, fg=CREAM, insertbackground=GOLD, relief="flat"
        )
        self.movie_time_entry.grid(
            row=1, column=1, sticky="w", padx=(8, 0), pady=5)

        # Movie Genre Entry
        self.movie_genre_entry_label = tk.Label(
            self.input_frame, text="Movie Genre:", font=FONT_LABEL, bg=BG, fg=CREAM
        )
        self.movie_genre_entry_label.grid(
            row=2, column=0, sticky="e", padx=(0, 8), pady=5)

        self.movie_genre_entry = tk.Entry(
            self.input_frame, width=field_width, font=FONT_INPUT,
            bg=FIELD, fg=CREAM, insertbackground=GOLD, relief="flat"
        )
        self.movie_genre_entry.grid(
            row=2, column=1, sticky="w", padx=(8, 0), pady=5)

        # Button to submit the movie
        self.add_button = tk.Button(
            self,
            text="Add Movie",
            width=16,
            font=FONT_BUTTON,
            bg=GOLD,
            fg=BG,
            activebackground=GOLD_HOVER,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            command=self.add_movie,
        )
        self.add_button.pack(pady=(8, 15))

        # --- Add A New Showtime Section ---
        self.showtime_section_label = tk.Label(
            self, text="Add A New Showtime", font=FONT_SECTION, bg=BG, fg=CREAM
        )
        self.showtime_section_label.pack(pady=(10, 5))

        self.showtime_input_frame = tk.Frame(self, bg=BG)
        self.showtime_input_frame.pack(pady=5)
        self.showtime_input_frame.columnconfigure(0, minsize=130)
        self.showtime_input_frame.columnconfigure(1, minsize=180)

        # Showtime Movie Selection Input
        self.showtime_movie_label = tk.Label(
            self.showtime_input_frame, text="Select Movie:", font=FONT_LABEL,
            bg=BG, fg=CREAM
        )
        self.showtime_movie_label.grid(
            row=0, column=0, sticky="e", padx=(0, 8), pady=5)

        self.showtime_movie_entry = ttk.Combobox(
            self.showtime_input_frame, width=field_width - 3, font=FONT_INPUT
        )
        self.showtime_movie_entry.grid(
            row=0, column=1, sticky="w", padx=(8, 0), pady=5)

        # Time Row for showtime input
        self.showtime_time_label = tk.Label(
            self.showtime_input_frame, text="Showtime Time:", font=FONT_LABEL,
            bg=BG, fg=CREAM
        )
        self.showtime_time_label.grid(
            row=1, column=0, sticky="e", padx=(0, 8), pady=5)

        self.showtime_time_entry = tk.Entry(
            self.showtime_input_frame,
            width=field_width,
            font=FONT_INPUT,
            bg=FIELD,
            fg=CREAM,
            insertbackground=GOLD,
            relief="flat",
        )
        self.showtime_time_entry.grid(
            row=1, column=1, sticky="w", padx=(8, 0), pady=5)

        # Date Row for showtime input
        self.showtime_date_label = tk.Label(
            self.showtime_input_frame, text="Showtime Date:", font=FONT_LABEL,
            bg=BG, fg=CREAM
        )
        self.showtime_date_label.grid(
            row=2, column=0, sticky="e", padx=(0, 8), pady=5)

        self.showtime_date_entry = ttk.Combobox(
            self.showtime_input_frame, width=field_width - 3, font=FONT_INPUT
        )
        self.showtime_date_entry.grid(
            row=2, column=1, sticky="w", padx=(8, 0), pady=5)

        # Price Row for showtime input
        self.showtime_price_label = tk.Label(
            self.showtime_input_frame, text="Showtime Price:", font=FONT_LABEL,
            bg=BG, fg=CREAM
        )
        self.showtime_price_label.grid(
            row=3, column=0, sticky="e", padx=(0, 8), pady=5)

        self.showtime_price_entry = tk.Entry(
            self.showtime_input_frame,
            width=field_width,
            font=FONT_INPUT,
            bg=FIELD,
            fg=CREAM,
            insertbackground=GOLD,
            relief="flat",
        )
        self.showtime_price_entry.grid(
            row=3, column=1, sticky="w", padx=(8, 0), pady=5)

        # Button to submit the showtime
        self.add_showtime_button = tk.Button(
            self,
            text="Add Showtime",
            width=16,
            font=FONT_BUTTON,
            bg=GOLD,
            fg=BG,
            activebackground=GOLD_HOVER,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            # command=self.add_showtime
        )
        self.add_showtime_button.pack(pady=(8, 15))
        for btn in (self.add_button, self.add_showtime_button):
            btn.bind("<Enter>", lambda e: e.widget.config(bg=GOLD_HOVER))
            btn.bind("<Leave>", lambda e: e.widget.config(bg=GOLD))

    def add_movie(self):
        title = self.movie_entry.get()
        time = self.movie_time_entry.get()
        genre = self.movie_genre_entry.get()

        result = self.admin_service.add_movie(title, time, genre)

        if result:
            messagebox.showinfo("Success", "Movie added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add movie.")
