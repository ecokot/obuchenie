from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///db.sqlite3', echo=True)

with engine.connect() as conn:
    result = conn.execute(text('SELECT 1 + 1'))
    print(result.scalar())