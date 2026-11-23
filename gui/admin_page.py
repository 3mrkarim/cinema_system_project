import tkinter as tk
from tkinter import ttk
from services.admin_service import AdminService


class AdminPage(tk.Frame):

  def __init__(self, parent):
    super().__init__(parent)
    self.admin_service = AdminService()
    self.create_layout()

  def create_layout(self):
    field_width = 24

    self.title_label = tk.Label(self, text="Admin Dashboard", font=("Arial", 20, "bold"))
    self.title_label.pack(pady=(15, 10))

    # --- Add A New Movie Section ---
    self.entry_label = tk.Label(self, text="Add A New Movie", font=("Arial", 15))
    self.entry_label.pack(pady=(10, 5))

    self.input_frame = tk.Frame(self)
    self.input_frame.pack(pady=5)
    self.input_frame.columnconfigure(0, minsize=130)
    self.input_frame.columnconfigure(1, minsize=180)

    # Movie Title Entry
    self.movie_entry_label = tk.Label(self.input_frame, text="Movie Title:")
    self.movie_entry_label.grid(row=0, column=0, sticky="e", padx=(0, 8), pady=5)

    self.movie_entry = tk.Entry(self.input_frame, width=field_width)
    self.movie_entry.grid(row=0, column=1, sticky="w", padx=(8, 0), pady=5)

    # Movie Time Entry
    self.movie_time_entry_label = tk.Label(self.input_frame, text="Movie Time:")
    self.movie_time_entry_label.grid(row=1, column=0, sticky="e", padx=(0, 8), pady=5)

    self.movie_time_entry = tk.Entry(self.input_frame, width=field_width)
    self.movie_time_entry.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=5)

    # Movie Genre Entry
    self.movie_genre_entry_label = tk.Label(self.input_frame, text="Movie Genre:")
    self.movie_genre_entry_label.grid(row=2, column=0, sticky="e", padx=(0, 8), pady=5)

    self.movie_genre_entry = tk.Entry(self.input_frame, width=field_width)
    self.movie_genre_entry.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=5)

    # Button to submit the movie
    self.add_button = tk.Button(
        self,
        text="Add Movie",
        width=16,
        command=self.add_movie,
    )
    self.add_button.pack(pady=(8, 15))

    # --- Add A New Showtime Section ---
    self.showtime_section_label = tk.Label(
        self, text="Add A New Showtime", font=("Arial", 15)
    )
    self.showtime_section_label.pack(pady=(10, 5))

    self.showtime_input_frame = tk.Frame(self)
    self.showtime_input_frame.pack(pady=5)
    self.showtime_input_frame.columnconfigure(0, minsize=130)
    self.showtime_input_frame.columnconfigure(1, minsize=180)

    # Showtime Movie Selection Input
    self.showtime_movie_label = tk.Label(
        self.showtime_input_frame, text="Select Movie:"
    )
    self.showtime_movie_label.grid(row=0, column=0, sticky="e", padx=(0, 8), pady=5)

    self.showtime_movie_entry = ttk.Combobox(
        self.showtime_input_frame, width=field_width - 3
    )
    self.showtime_movie_entry.grid(row=0, column=1, sticky="w", padx=(8, 0), pady=5)

    # Time Row for showtime input
    self.showtime_time_label = tk.Label(
        self.showtime_input_frame, text="Showtime Time:"
    )
    self.showtime_time_label.grid(row=1, column=0, sticky="e", padx=(0, 8), pady=5)

    self.showtime_time_entry = tk.Entry(self.showtime_input_frame, width=field_width)
    self.showtime_time_entry.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=5)

    # Date Row for showtime input
    self.showtime_date_label = tk.Label(
        self.showtime_input_frame, text="Showtime Date:"
    )
    self.showtime_date_label.grid(row=2, column=0, sticky="e", padx=(0, 8), pady=5)

    self.showtime_date_entry = ttk.Combobox(
        self.showtime_input_frame, width=field_width - 3
    )
    self.showtime_date_entry.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=5)

    # Price Row for showtime input
    self.showtime_price_label = tk.Label(
        self.showtime_input_frame, text="Showtime Price:"
    )
    self.showtime_price_label.grid(row=3, column=0, sticky="e", padx=(0, 8), pady=5)

    self.showtime_price_entry = tk.Entry(self.showtime_input_frame, width=field_width)
    self.showtime_price_entry.grid(row=3, column=1, sticky="w", padx=(8, 0), pady=5)

    # Button to submit the showtime
    self.add_showtime_button = tk.Button(
        self,
        text="Add Showtime",
        width=16,
        # command=self.add_showtime
    )
    self.add_showtime_button.pack(pady=(8, 15))

  def add_movie(self):
    title = self.movie_entry.get()
    time = self.movie_time_entry.get()
    genre = self.movie_genre_entry.get()

    result = self.admin_service.add_movie(title, time, genre)

    if result:
      print("Movie added successfully!")
    else:
      print("Failed to add movie.")