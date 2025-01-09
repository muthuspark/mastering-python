new_user = User(name='Alice', fullname='Alice Smith', nickname='alicesmith')
session.add(new_user)
session.commit()

all_users = session.query(User).all()
for user in all_users:
    print(f"Name: {user.name}, Full Name: {user.fullname}, Nickname: {user.nickname}")