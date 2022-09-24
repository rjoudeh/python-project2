from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://yynfpfcmzaurur:86559a5c68397a1e1c13caa3da96a0176517227e2673043e0e13c8ec04775a05@ec2-3-219-19-205.compute-1.amazonaws.com:5432/da104r99sjglr0',
    echo=True)
Session = sessionmaker(bind=engine)


def get_db_session():
    return Session()
