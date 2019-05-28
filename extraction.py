from models import Base
from models import Address, Status, CenterStatus, CurrentStatus, EstateStatus, FlatType, House, HouseStateStatus, \
    IntervalStatus, DocType, NormativeDocument, OperStat, Room, RoomType, AddressObjectType, Stead, StructureStatus
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///mybase.db")
db_session = scoped_session(sessionmaker(bind = engine))
Base.query = db_session.query_property()


case = Address.query.filter(Address.livestatus == 1).first()

print(case.offname, case.postalcode, case.shortname)