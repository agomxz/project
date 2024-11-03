from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self):
        return self.SessionLocal()

    def insert_objects(self, objects):
        session = self.get_session()
        try:
            session.add_all(objects)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting objects: {e}")
        finally:
            session.close()

    def alter_sequence(self, name_seq, num):
        session = self.get_session()
        try:
            session.execute(text(f"ALTER SEQUENCE {name_seq} RESTART WITH {num+1};"))
            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error sequence: {e}")
        finally:
            session.close()

        return None

    def execute_query(self, query_function):
        session = self.get_session()
        try:
            result = query_function(session)
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            session.close()
