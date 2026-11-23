from database.database_manager import DatabaseManager

class AdminService:

  def __init__(self):
      self.db = DatabaseManager()

  def add_movie(self, title):

      if not title.strip():
          return False

      return self.db.add_movie(title)