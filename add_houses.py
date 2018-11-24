import os
from dbfread import DBF
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base
from models import Address, Status, CenterStatus, CurrentStatus, EstateStatus, FlatType, House, HouseStateStatus, \
    IntervalStatus, DocType, NormativeDocument, OperStat, Room, RoomType, AddressObjectType, Stead

DIRECTION = '/fias_delta_dbf'
MODEL_NAME = {
    'ADDROB': Address,
    'ACTSTAT': Status,
    # 'ACTSTA': Status,
    'CENTERST': CenterStatus,
    'CURENTST': CurrentStatus,
    'ESTSTAT': EstateStatus,
    'FLATTYPE': FlatType,
    'HOUSE': House,
    'HSTSTAT': HouseStateStatus,
    'INTVSTAT': IntervalStatus,
    'NDOCTYPE': DocType,
    'NORDOC': NormativeDocument,
    'OPERSTAT': OperStat,
    'ROOMTYPE': Room,
    'SOCRBASE': RoomType,
    'STEAD': AddressObjectType,
    'STRSTAT': Stead
}

engine = create_engine("sqlite:///mybase.db")

Base.metadata.create_all(engine)

for file in os.listdir(DIRECTION):
    print(
        'Работаем с файлом "{}"'.format(file)
    )
    session = Session(bind=engine)
    dp_path = r'{}/{}'.format(DIRECTION, file)
    dbf_db = DBF(dp_path, 'cp866')
    for row in dbf_db:
        type_ = ''.join([i for i in os.path.splitext(file)[0] if not i.isnumeric()]) #в функцию
        current_model = MODEL_NAME[type_]
        session.add(current_model(**dict((k.lower(), v) for k, v in row.items())))  #в функцию
    session.commit()

session.close()
