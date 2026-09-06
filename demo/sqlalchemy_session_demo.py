from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///demo.db', echo=False)

with Session(engine) as session:
    result = session.execute(text('select 1'))
    print(result.scalar())