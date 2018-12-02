from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Status(Base):
    """Статус актуальности ФИАС"""
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    actstatid = Column(Integer)
    name = Column(String(100))
    adresses = relationship("Address", backref="status")

    def __repr__(self):
        return '<Status {} {}>'.format(self.actstatid, self.name)


class Address(Base):
    """Таблица – ADDROBJ (Object) содержит коды, наименования и типы адресообразующих элементов (регионы; округа;
    районы (улусы, кужууны); города, внутригородские районы,  поселки городского типа, сельские населенные пункты; 
    улицы, дополнительные адресные элементы, элементы улично-дорожной сети, планировочной структуры дополнительного 
    адресного элемента)."""
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    actstatus = Column(Integer, ForeignKey('status.id'))
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

    def __repr__(self):
        return '<Address {} {} {}>'.format(self.aoguid, self.formalname, self.regioncode)


class CenterStatus(Base):
    """Статус центра"""
    __tablename__ = 'centerstatus'
    id = Column(Integer, primary_key=True)
    centerstid = Column(Integer)
    name = Column(String(100))

    def __repr__(self):
        return '<Status {} {}>'.format(self.centerstid, self.name)


class CurrentStatus(Base):
    """Таблица CURENTST (CurrentStatus) – содержит перечень статусов актуальности записи  адресного элемента по 
    классификатору КЛАДР4.0."""
    __tablename__ = 'currentstatus'
    id = Column(Integer, primary_key=True)
    curentstid = Column(Integer)
    name = Column(String(100))

    def __repr__(self):
        return '<CurrentStatus {} {}>'.format(self.curentstid, self.name)


class EstateStatus(Base):
    """Таблица ESTSTAT (EstateStatus) – содержит перечень возможных видов владений."""
    __tablename__ = 'estatestatus'
    id = Column(Integer, primary_key=True)
    eststatid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

    def __repr__(self):
        return '<EstateStatus {} {}>'.format(self.eststatid, self.name)


class FlatType(Base):
    """Таблица FLATTYPE (FlatType) – НЕТ В ДОКУМЕНТЕ. ВАЖНО: ОПРЕДЕЛЯЕТ ТИП ПОМЕЩЕНИЯ (КВАРТИРА, ОФИС, СКЛАД И Т.Д.)"""
    __tablename__ = 'flattype'
    id = Column(Integer, primary_key=True)
    fltypeid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

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

    def __repr__(self):
        return '<House {} {} {}>'.format(self.aoguid, self.eststatus, self.housenum)


class HouseStateStatus(Base):
    """Таблица HSTSTAT (HouseStateStatus) – содержит перечень возможных состояний объектов недвижимости"""
    __tablename__ = 'housestatestatus'
    id = Column(Integer, primary_key=True)
    housestid = Column(Integer)
    name = Column(String(60))

    def __repr__(self):
        return '<HouseStateStatus {} {}>'.format(self.housestid, self.name)


class IntervalStatus(Base):
    """Таблица INTVSTAT (IntervalStatus) – содержит перечень возможных значений интервалов домов 
    (обычный, четный, нечетный)"""
    __tablename__ = 'intervalstatus'
    id = Column(Integer, primary_key=True)
    intvstatid = Column(Integer)
    name = Column(String(100))

    def __repr__(self):
        return '<IntervalStatus {} {}>'.format(self.intvstatid, self.name)


class DocType(Base):
    """DOCTYPE – Тип документа"""
    __tablename__ = 'doctype'
    id = Column(Integer, primary_key=True)
    ndtypeid = Column(Integer)
    name = Column(String(100))

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

    def __repr__(self):
        return '<NormativeDocument {} {}>'.format(self.normdocid, self.docname)


class OperStat(Base):
    """Таблица  OPERSTAT (OperationStatus) – содержит перечень кодов операций над адресными объектами"""
    __tablename__ = 'oper_stat'
    id = Column(Integer, primary_key=True)
    operstatid = Column(Integer)
    name = Column(String(100))

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

    def __repr__(self):
        return '<Room {} {}>'.format(self.roomid, self.flatnumber, self.roomnumber)


class RoomType(Base):
    """Таблица  ROOMTYPE (RoomType) – Тип комнаты"""
    __tablename__ = 'room_type'
    id = Column(Integer, primary_key=True)
    rmtypeid = Column(Integer)
    name = Column(String(100))
    shortname = Column(String(100))

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

    def __repr__(self):
        return '<Stead {} {}>'.format(self.steadguid, self.number)


class StructureStatus(Base):
    """Таблица STRSTAT (StructureStatus) – содержит перечень видов строений"""
    __tablename__ = 'structure_status'
    id = Column(Integer, primary_key=True)
    strstatid = Column(Integer)
    name = Column(String(20))
    shortname = Column(String(20))

    def __repr__(self):
        return '<StructureStatus {} {}>'.format(self.strstatid, self.name)