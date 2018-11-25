import os
from dbfread import DBF
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base
from models import Address, Status, CenterStatus, CurrentStatus, EstateStatus, FlatType, House, HouseStateStatus, \
    IntervalStatus, DocType, NormativeDocument, OperStat, Room, RoomType, AddressObjectType, Stead, StructureStatus

DIRECTION = 'C:/projects/Adresses/adresses_russia/fias_delta_dbf'
MODEL_NAME = {
    'ADDROB': Address,
    'ACTSTAT': Status,
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
    'ROOM': Room,
    'ROOMTYPE': RoomType,
    'SOCRBASE': AddressObjectType,
    'STEAD': Stead,
    'STRSTAT': StructureStatus
}

engine = create_engine("sqlite:///mybase.db")

Base.metadata.create_all(engine)

def get_table_name(file_name):
    '''get a name of dbf file without numbers
    Input:
    :file_name: - a name of dbf file
    Output:
    :type_: - a clear name of dbf file to send it to a dictionary
    '''
    type_ = ''.join([i for i in os.path.splitext(file_name)[0] if not i.isnumeric()])
    return type_

for file in os.listdir(DIRECTION):
    print(
        'Работаем с файлом "{}"'.format(file)
    )
    session = Session(bind=engine)
    dp_path = r'{}/{}'.format(DIRECTION, file)
    dbf_db = DBF(dp_path, 'cp866')
    type_ = get_table_name(file)
    for row in dbf_db:
        current_model = MODEL_NAME[type_]
        session.add(current_model(**dict((k.lower(), v) for k, v in row.items())))  #в функцию
    session.commit()

session.close()
