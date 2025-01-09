user = session.query(User).filter_by(name='Alice').first()
print(f"Found user: {user.name}")

users_with_nickname = session.query(User).filter(User.nickname.like('%smith%')).all()
for user in users_with_nickname:
    print(f"User with 'smith' in nickname: {user.name}")
