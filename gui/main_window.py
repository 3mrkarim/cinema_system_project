import tkinter as tk
from gui.admin_page import AdminPage

## Creating the main window
class MainWindow:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("CineBook")
    self.root.geometry("1200x800")

    self.admin_page = AdminPage(self.root)
    self.admin_page.pack(fill="both", expand=True)

  def run(self):
    self.root.mainloop()