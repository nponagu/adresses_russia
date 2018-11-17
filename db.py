import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey #этот тип нужен для создания внешнего ID зависимостей many to many

engine = create_engine("sqlite:///mybase.db")
#hop2

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property() 

# association_table = Table('association', Base.metadata,
#     Column('room_id', Integer, ForeignKey('room.id')),
#     Column('user_id', Integer, ForeignKey('user.id'))
# )

class Address(Base):
    """Таблица – ADDROBJ (Object) содержит коды, наименования и типы адресообразующих элементов (регионы; округа; 
    районы (улусы, кужууны); города, внутригородские районы,  поселки городского типа, сельские населенные пункты; 
    улицы, дополнительные адресные элементы, элементы улично-дорожной сети, планировочной структуры дополнительного 
    адресного элемента)."""
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    actstatus = Column(Integer)
    aoguid = Column(String(36))
    aoid = Column(String(36))
    aolevel = Column(Integer)
    areacode = Column(String(3))
    autocode = Column(String(1))
    centstatus = Column(Integer)
    citycode = Column(String(3))
    code = Column(String(17))
    currstatus = Column(Integer)
    enddate = Column(Date)
    formalname = Column(String(120))
    ifnsfl = Column(String(4))
    ifnsul = Column(String(4))
    nextid = Column(String(36))
    offname = Column(String(120))
    okato = Column(String(11))
    oktmo = Column(String(11))
    operstatus = Column(Integer)
    parentguid = Column(String(36))
    placecode = Column(String(3))
    plaincode = Column(String(15))
    postalcode = Column(String(6))
    previd = Column(String(36))
    regioncode = Column(String(2))
    shortname = Column(String(10))
    startdate = Column(Date)
    streetcode = Column(String(4))
    terrifnsfl = Column(String(4))
    terrifnsul = Column(String(4))
    updatedate = Column(Date)
    ctarcode = Column(String(3))
    extrcode = Column(String(4))
    sextcode = Column(String(3))
    livestatus = Column(Integer)
    normdoc = Column(String(36))
    plancode = Column(Integer)
    cadnum = Column(Integer)
    divtype = Column(Integer)


    def __init__(
        self, actstatus = None,    aoguid = None,  aoid = None,    aolevel = None,     areacode = None,    autocode = None,    
        centstatus = None,  citycode = None,    code = None,    currstatus = None,  enddate = None,     formalname = None,  
        ifnsfl = None,  ifnsul = None,  nextid = None,  offname = None,     okato = None,   oktmo = None,   operstatus = None,  
        parentguid = None,  placecode = None,   plaincode = None,   postalcode = None,  previd = None,  regioncode = None,  
        shortname = None,   startdate = None,   streetcode = None,  terrifnsfl = None,  terrifnsul = None,  updatedate = None,  
        ctarcode = None,    extrcode = None,    sextcode = None,    livestatus = None,  normdoc = None,     plancode = None,    
        cadnum = None,  divtype = None
        ):
        self.actstatus = actstatus
        self.aoguid = aoguid
        self.aoid = aoid
        self.aolevel = aolevel
        self.areacode = areacode
        self.autocode = autocode
        self.centstatus = centstatus
        self.citycode = citycode
        self.code = code
        self.currstatus = currstatus
        self.enddate = enddate
        self.formalname = formalname
        self.ifnsfl = ifnsfl
        self.ifnsul = ifnsul
        self.nextid = nextid
        self.offname = offname
        self.okato = okato
        self.oktmo = oktmo
        self.operstatus = operstatus
        self.parentguid = parentguid
        self.placecode = placecode
        self.plaincode = plaincode
        self.postalcode = postalcode
        self.previd = previd
        self.regioncode = regioncode
        self.shortname = shortname
        self.startdate = startdate
        self.streetcode = streetcode
        self.terrifnsfl = terrifnsfl
        self.terrifnsul = terrifnsul
        self.updatedate = updatedate
        self.ctarcode = ctarcode
        self.extrcode = extrcode
        self.sextcode = sextcode
        self.livestatus = livestatus
        self.normdoc = normdoc
        self.plancode = plancode
        self.cadnum = cadnum
        self.divtype = divtype

    def __repr__(self):
        return '<Address {} {} {}>'.format(self.aoguid, self.formalname, self.regioncode)

class Status(Base):
    """Статус актуальности ФИАС"""
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    actstatid = Column(Integer)
    name = Column(String(100))

    def __init__(
        self, actstatid=None, name=None
        ):
        self.actstatid = actstatid
        self.name = name

    def __repr__(self):
        return '<Status {} {}>'.format(self.actstatid, self.name)

class CenterStatus(Base):
    """Статус центра"""
    __tablename__ = 'centerstatus'
    id = Column(Integer, primary_key=True)
    centerstid = Column(Integer)
    name = Column(String(100))

    def __init__(
        self, centerstid=None, name=None
        ):
        self.centerstid = centerstid
        self.name = name

    def __repr__(self):
        return '<Status {} {}>'.format(self.centerstid, self.name)

class CurrentStatus(Base):
    """Таблица CURENTST (CurrentStatus) – содержит перечень статусов актуальности записи  адресного элемента по 
    классификатору КЛАДР4.0."""
    __tablename__ = 'currentstatus'
    id = Column(Integer, primary_key=True)
    curentstid = Column(Integer)
    name = Column(String(100))

    def __init__(
        self, curentstid=None, name=None
        ):
        self.curentstid = curentstid
        self.name = name

    def __repr__(self):
        return '<CurrentStatus {} {}>'.format(self.curentstid, self.name)

class EstateStatus(Base):
    """Таблица ESTSTAT (EstateStatus) – содержит перечень возможных видов владений."""
    __tablename__ = 'estatestatus'
    id = Column(Integer, primary_key=True)
    eststatid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

    def __init__(
        self, eststatid=None, name=None, shortname=None
        ):
        self.eststatid = eststatid
        self.name = name
        self.shortname = shortname

    def __repr__(self):
        return '<EstateStatus {} {}>'.format(self.eststatid, self.name)

class FlatType(Base):
    """Таблица FLATTYPE (FlatType) – НЕТ В ДОКУМЕНТЕ. ВАЖНО: ОПРЕДЕЛЯЕТ ТИП ПОМЕЩЕНИЯ (КВАРТИРА, ОФИС, СКЛАД И Т.Д.)"""
    __tablename__ = 'flattype'
    id = Column(Integer, primary_key=True)
    fltypeid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

    def __init__(
        self, fltypeid=None, name=None, shortname=None
        ):
        self.fltypeid = fltypeid
        self.name = name
        self.shortname = shortname

    def __repr__(self):
        return '<FlatType {} {}>'.format(self.fltypeid, self.name)

class House(Base):
    """Таблица HOUSE (House) содержат информацию о номерах отдельных домов, владений, домовладений, корпусов, 
    строений и земельных участках"""
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    aoguid = Column(String(36))
    buildnum = Column(String(10))
    enddate = Column(Date)
    eststatus = Column(Integer)
    houseguid = Column(String(36))
    houseid = Column(String(36))
    housenum = Column(String(20))
    statstatus = Column(Integer)
    ifnsfl = Column(String(4))
    ifnsul = Column(String(4))
    okato = Column(String(11))
    oktmo = Column(String(11))
    postalcode = Column(String(6))
    startdate = Column(Date)
    strucnum = Column(String(10))
    strstatus = Column(Integer)
    terrifnsfl = Column(String(4))
    terrifnsul = Column(String(4))
    updatedate = Column(Date)
    normdoc = Column(String(36))
    counter = Column(Integer)
    cadnum = Column(String(100))
    divtype = Column(Integer)

    def __init__(
        self, aoguid=None, buildnum=None, enddate=None, eststatus=None, houseguid=None, houseid=None, housenum=None, 
        statstatus=None, ifnsfl=None, ifnsul=None, okato=None, oktmo=None, postalcode=None, startdate=None, 
        strucnum=None, strstatus=None, terrifnsfl=None, terrifnsul=None, updatedate=None, normdoc=None, counter=None,
        cadnum=None, divtype=None
        ):
        self.aoguid = aoguid
        self.buildnum = buildnum
        self.enddate = enddate
        self.eststatus = eststatus
        self.houseguid = houseguid
        self.houseid = houseid
        self.housenum = housenum
        self.statstatus = statstatus
        self.ifnsfl = ifnsfl
        self.ifnsul = ifnsul
        self.okato = okato
        self.oktmo = oktmo
        self.postalcode = postalcode
        self.startdate = startdate
        self.strucnum = strucnum
        self.strstatus = strstatus
        self.terrifnsfl = terrifnsfl
        self.terrifnsul = terrifnsul
        self.updatedate = updatedate
        self.normdoc = normdoc
        self.counter = counter
        self.cadnum = cadnum
        self.divtype = divtype

    def __repr__(self):
        return '<House {} {} {}>'.format(self.aoguid, self.eststatus, self.housenum)

class HouseStateStatus(Base):
    """Таблица HSTSTAT (HouseStateStatus) – содержит перечень возможных состояний объектов недвижимости"""
    __tablename__ = 'housestatestatus'
    id = Column(Integer, primary_key=True)
    housestid = Column(Integer)
    name = Column(String(60))

    def __init__(
        self, housestid=None, name=None
        ):
        self.housestid = housestid
        self.name = name

    def __repr__(self):
        return '<HouseStateStatus {} {}>'.format(self.housestid, self.name)

class IntervalStatus(Base):
    """Таблица INTVSTAT (IntervalStatus) – содержит перечень возможных значений интервалов домов 
    (обычный, четный, нечетный)"""
    __tablename__ = 'intervalstatus'
    id = Column(Integer, primary_key=True)
    intvstatid = Column(Integer)
    name = Column(String(100))

    def __init__(self, intvstatid=None, name=None):
        self.intvstatid = intvstatid
        self.name = name

    def __repr__(self):
        return '<IntervalStatus {} {}>'.format(self.intvstatid, self.name)

class DocType(Base):
    """DOCTYPE – Тип документа"""
    __tablename__ = 'doctype'
    id = Column(Integer, primary_key=True)
    ndtypeid = Column(Integer)
    name = Column(String(100))

    def __init__(self, ndtypeid=None, name=None):
        self.ndtypeid = ndtypeid
        self.name = name

    def __repr__(self):
        return '<DocType {} {}>'.format(self.ndtypeid, self.name)

class NormativeDocument(Base):
    """Таблица  NORDOC (NormativeDocument) - сведения по нормативному документу, являющемуся основанием 
    присвоения адресному элементу наименования"""
    __tablename__ = 'normative_document'
    id = Column(Integer, primary_key=True)
    normdocid = Column(String(36))
    docname = Column(String(100))
    docdate = Column(String(100))
    docnum = Column(String(20))
    doctype = Column(Integer)
    docimgid = Column(Integer)

    def __init__(self, normdocid=None, docname=None, docdate=None, docnum=None, doctype=None, docimgid=None):
        self.normdocid = normdocid
        self.docname = docname
        self.docdate = docdate
        self.docnum = docnum
        self.doctype = doctype
        self.docimgid = docimgid

    def __repr__(self):
        return '<NormativeDocument {} {}>'.format(self.normdocid, self.docname)

class OperStat(Base):
    """Таблица  OPERSTAT (OperationStatus) – содержит перечень кодов операций над адресными объектами"""
    __tablename__ = 'oper_stat'
    id = Column(Integer, primary_key=True)
    operstatid = Column(Integer)
    name = Column(String(100))

    def __init__(self, operstatid=None, name=None):
        self.operstatid = operstatid
        self.name = name

    def __repr__(self):
        return '<OperStat {} {}>'.format(self.operstatid, self.name)

class Room(Base):
    """Таблица ROOM (Room) содержит записи с номерами помещений, квартир, офисов, комнат, 
    а также их кадастровые номера"""
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    roomid = Column(String(36))
    roomguid = Column(String(36))
    houseguid = Column(String(36))
    regioncode = Column(String(2))
    flatnumber = Column(String(50))
    flattype = Column(Integer)
    roomnumber = Column(String(50))
    roomtype = Column(Integer)
    cadnum = Column(String(100))
    roomcadnum = Column(String(100))
    postalcode = Column(String(6))
    updatedate = Column(Date)
    previd = Column(String(36))
    nextid = Column(String(36))
    operstatus = Column(Integer)
    startdate = Column(Date)
    enddate = Column(Date)
    livestatus = Column(Integer)
    normdoc = Column(String(36))

    def __init__(self, roomid=None, roomguid=None, houseguid=None, regioncode=None, flatnumber=None, flattype=None, 
        roomnumber=None, roomtype=None, cadnum=None, roomcadnum=None, postalcode=None, updatedate=None, previd=None, 
        nextid=None, operstatus=None, startdate=None, enddate=None, livestatus=None, normdoc=None):
        self.roomid = roomid
        self.roomguid = roomguid
        self.houseguid = houseguid
        self.regioncode = regioncode
        self.flatnumber = flatnumber
        self.flattype = flattype
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.cadnum = cadnum
        self.roomcadnum = roomcadnum
        self.postalcode = postalcode
        self.updatedate = updatedate
        self.previd = previd
        self.nextid = nextid
        self.operstatus = operstatus
        self.startdate = startdate
        self.enddate = enddate
        self.livestatus = livestatus
        self.normdoc = normdoc

    def __repr__(self):
        return '<Room {} {}>'.format(self.roomid, self.flatnumber, self.roomnumber)

class RoomType(Base):
    """Таблица  ROOMTYPE (RoomType) – Тип комнаты"""
    __tablename__ = 'room_type'
    id = Column(Integer, primary_key=True)
    rmtypeid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

    def __init__(self, rmtypeid=None, name=None, shortname=None):
        self.rmtypeid = rmtypeid
        self.name = name
        self.shortname = shortname

    def __repr__(self):
        return '<RoomType {} {}>'.format(self.rmtypeid, self.name)

class AddressObjectType(Base):
    """Таблица  SOCRBASE (AddressObjectType) – содержит перечень полных, сокращённых наименований типов адресных 
    элементов и уровней их классификации"""
    __tablename__ = 'address_object_type'
    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    socrname = Column(String(50))
    scname = Column(String(10))
    kod_t_st = Column(String(4))

    def __init__(self, level=None, socrname=None, scname=None, kod_t_st=None):
        self.level = level
        self.socrname = socrname
        self.scname = scname
        self.kod_t_st = kod_t_st

    def __repr__(self):
        return '<AddressObjectType {} {}>'.format(self.kod_t_st, self.socrname)

class Stead(Base):
    """Таблица STEAD (Stead) содержит коды, кадастровые номера земельных участков"""
    __tablename__ = 'stead'
    id = Column(Integer, primary_key=True)
    steadguid = Column(String(36))
    number = Column(String(250))
    regioncode = Column(String(2))
    postalcode = Column(String(6))
    ifnsfl = Column(String(4))
    terrifnsfl = Column(String(4))
    ifnsul = Column(String(4))
    terrifnsul = Column(String(4))
    okato = Column(String(11))
    updatedate = Column(Date)
    parentguid = Column(String(36))
    steadid = Column(String(36))
    previd = Column(String(36))
    operstatus = Column(Integer)
    startdate = Column(Date)
    enddate = Column(Date)
    nextid = Column(String(36))
    oktmo = Column(String(11))
    livestatus = Column(Integer)
    cadnum = Column(String(100))
    divtype = Column(Integer)
    counter = Column(Integer)
    normdoc = Column(String(36))

    def __init__(
        self, steadguid=None, number=None, regioncode=None, postalcode=None, ifnsfl=None, terrifnsfl=None,
        ifnsul=None, terrifnsul=None, okato=None, updatedate=None, parentguid=None, steadid=None, previd=None,
        operstatus=None, startdate=None, enddate=None, nextid=None, oktmo=None, livestatus=None, cadnum=None, 
        divtype=None, counter=None, normdoc=None
        ):
        self.steadguid = steadguid
        self.number = number
        self.regioncode = regioncode
        self.postalcode = postalcode
        self.ifnsfl = ifnsfl
        self.terrifnsfl = terrifnsfl
        self.ifnsul = ifnsul
        self.terrifnsul = terrifnsul
        self.okato = okato
        self.updatedate = updatedate
        self.parentguid = parentguid
        self.steadid = steadid
        self.previd = previd
        self.operstatus = operstatus
        self.startdate = startdate
        self.enddate = enddate
        self.nextid = nextid
        self.oktmo = oktmo
        self.livestatus = livestatus
        self.cadnum = cadnum
        self.divtype = divtype
        self.counter = counter
        self.normdoc = normdoc

    def __repr__(self):
        return '<Stead {} {}>'.format(self.steadguid, self.number)

class StructureStatus(Base):
    """Таблица STRSTAT (StructureStatus) – содержит перечень видов строений"""
    __tablename__ = 'structure_status'
    id = Column(Integer, primary_key=True)
    strstatid = Column(Integer)
    name = Column(String(20))
    shortname = Column(String(20))

    def __init__(self, strstatid=None, name=None, shortname=None):
        self.strstatid = strstatid
        self.name = name
        self.shortname = shortname

    def __repr__(self):
        return '<StructureStatus {} {}>'.format(self.strstatid, self.name)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)