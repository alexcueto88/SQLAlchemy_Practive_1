from models import User,Comment
from main import session


# session = Session(bind=engine)

user1 = User(
    username = 'jona',
    email_address = "jona@email.com",
    comments = [
        Comment(text="Hello World"),
        Comment(text="This is text comment.")
    ]
)

paul = User(
    username = 'Paul',
    email_address = "paul@email.com",
    comments = [
        Comment(text="Hello World"),
        Comment(text="This is text comment.")
    ]
)

cathy = User(
    username = 'Cathy',
    email_address = "cathy@email.com",
)

session.add_all([user1,paul,cathy])

session.commit()
