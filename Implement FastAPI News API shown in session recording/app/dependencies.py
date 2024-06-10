from .database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    else:
        pass
    finally:
        if db is not None:
            db.close()
