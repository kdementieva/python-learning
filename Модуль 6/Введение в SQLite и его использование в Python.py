import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute(
  """
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER DEFAULT NULL
  );
  """
)

def add_data(title, author, year=None):
  cursor.execute(
    """
    INSERT INTO books(title, author, year)
    VALUES(?, ?, ?);
    """,
    (title, author, year)
  )
  conn.commit()

def get_data():
  data = cursor.execute(
    """
    SELECT *
    FROM books;
    """
   ).fetchall()
  return(data)

def update_data(id, title, author, year):
  cursor.execute(
    """
    UPDATE books
    SET title = (?), author = (?), year = (?)
    WHERE id == (?);
    """,
    (title, author, year, id)
  )
  conn.commit()

def delete_data(id):
  cursor.execute(
    """
    DELETE FROM books
    WHERE id = (?);
    """,
    (id,)
  )
  conn.commit()


add_data("1984", "George Orwell", 1949)
add_data("Brave New World", "Aldous Huxley")

print('Данные в базе: \n')
print(get_data())

update_data(1, "Nineteen Eighty-Four", "George Orwell", 1949)
print('После обновления: \n')
print(get_data())

delete_data(1)
print('После удаления: \n')
print(get_data())
conn.close()