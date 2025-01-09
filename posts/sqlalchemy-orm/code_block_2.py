from sqlalchemy import create_engine

engine = create_engine('sqlite:///./mydatabase.db') # Connects to an SQLite database
Base.metadata.create_all(engine)