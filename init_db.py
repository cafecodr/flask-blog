import sqlite3

INSERT_STATEMENT = "INSERT INTO posts (title, content) VALUES (?, ?)"
TEST_POSTS = [
    {"title": "First Post", "content": "A short blog post to start the conversation."},
    {"title": "Second Post", "content": "A second blog post to keep the conversation going."},
]


def setup_db():
    """A simple function to set up the database and populate it with sample posts.

    Utilizes the `INSERT_STATEMENT` and `TEST_POSTS` constants.

    Run with `python init_db.py`
    """

    global INSERT_STATEMENT, TEST_POSTS

    conn = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    for post in TEST_POSTS:
        cur.execute(INSERT_STATEMENT, (post["title"], post["content"]))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    setup_db()
