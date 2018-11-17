import dbf #working with dbf format
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import db_session, Address, Status, CenterStatus, CurrentStatus, EstateStatus, FlatType, House, HouseStateStatus
from db import IntervalStatus, DocType, NormativeDocument, OperStat, Room, RoomType, AddressObjectType, Stead, StructureStatus
import os #library for working with folders

direction = 'W:/2018/Адреса/ФИАС/! archives/fias_delta_dbf'

#add dbf to ADDROBJ
def add_addres(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(
            row["actstatus"], row["aoguid"], row["aoid"], row["aolevel"], row["areacode"], row["autocode"],    
            row["centstatus"], row["citycode"], row["code"], row["currstatus"], row["enddate"],
            row["formalname"], row["ifnsfl"], row["ifnsul"], row["nextid"], row["offname"], row["okato"],   
            row["oktmo"], row["operstatus"], row["parentguid"], row["placecode"], row["plaincode"],   
            row["postalcode"], row["previd"], row["regioncode"], row["shortname"], row["startdate"],   
            row["streetcode"], row["terrifnsfl"], row["terrifnsul"], row["updatedate"], row["ctarcode"],    
            row["extrcode"], row["sextcode"], row["livestatus"], row["normdoc"], row["plancode"],    
            row["cadnum"], row["divtype"]
            )
        db_session.add(value)

def add_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["actstatid"], row["name"])
        db_session.add(value)

def add_center_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["centerstid"], row["name"])
        db_session.add(value)

def add_current_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["curentstid"], row["name"])
        db_session.add(value)

def add_estate_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["eststatid"], row["name"], row["shortname"])
        db_session.add(value)

def add_flat_type(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["fltypeid"], row["name"], row["shortname"])
        db_session.add(value)

def add_house(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(
            row["aoguid"], row["buildnum"], row["enddate"], row["eststatus"], row["houseguid"], row["houseid"],
            row["housenum"], row["statstatus"], row["ifnsfl"], row["ifnsul"], row["okato"], row["oktmo"], 
            row["postalcode"], row["startdate"], row["strucnum"], row["strstatus"], row["terrifnsfl"], row["terrifnsul"],
            row["updatedate"], row["normdoc"], row["counter"], row["cadnum"], row["divtype"]
            )
        db_session.add(value)

def add_house_state_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["housestid"], row["name"])
        db_session.add(value)

def add_interval_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["intvstatid"], row["name"])
        db_session.add(value)

def add_doc_type(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["ndtypeid"], row["name"])
        db_session.add(value)

def add_normative_document(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(
            row["normdocid"], row["docname"], row["docdate"], row["docnum"], row["doctype"], row["docimgid"]
            )
        db_session.add(value)

def add_oper_stat(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["operstatid"], row["name"])
        db_session.add(value)

def add_room(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(
            row["roomid"], row["roomguid"], row["houseguid"], row["regioncode"], row["flatnumber"],
            row["flattype"], row["roomnumber"], row["roomtype"], row["cadnum"], row["roomcadnum"], row["postalcode"],
            row["updatedate"], row["previd"], row["nextid"], row["operstatus"], row["startdate"], row["enddate"], 
            row["livestatus"], row["normdoc"]
            )
        db_session.add(value)

def add_room_type(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["rmtypeid"], row["name"], row["shortname"])
        db_session.add(value)

def add_address_object_type(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["level"], row["socrname"], row["scname"], row["kod_t_st"])
        db_session.add(value)

def add_stead(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(
            row["steadguid"], row["number"], row["regioncode"], row["postalcode"], row["ifnsfl"], row["terrifnsfl"], 
            row["ifnsul"], row["terrifnsul"], row["okato"], row["updatedate"], row["parentguid"], row["steadid"], 
            row["previd"], row["operstatus"], row["startdate"], row["enddate"], row["nextid"], row["oktmo"],
            row["livestatus"], row["cadnum"], row["divtype"], row["counter"], row["normdoc"]
            )
        db_session.add(value)

def add_structure_status(db=None, db_session=None, class_table=None):
    for row in db:
        value = class_table(row["strstatid"], row["name"], row["shortname"])
        db_session.add(value)

#convert dbfs to sqlite
addres_list = os.listdir(direction)
for file in addres_list:
    if len(file) > 6 and file[0:6] == 'ADDROB':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_addres(db=db, db_session=db_session, class_table=Address)
        db.close()
        db_session.commit()
    elif len(file) > 6 and file[0:6] == 'ACTSTA':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_status(db=db, db_session=db_session, class_table=Status)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'CENTERST':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_center_status(db=db, db_session=db_session, class_table=CenterStatus)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'CURENTST':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_current_status(db=db, db_session=db_session, class_table=CurrentStatus)
        db.close()
        db_session.commit()
    elif len(file) > 7 and file[0:7] == 'ESTSTAT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_estate_status(db=db, db_session=db_session, class_table=EstateStatus)
        db.close()
        db_session.commit()
    elif len(file) > 7 and file[0:8] == 'FLATTYPE':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_flat_type(db=db, db_session=db_session, class_table=FlatType)
        db.close()
        db_session.commit()
    elif len(file) > 4 and file[0:5] == 'HOUSE':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_house(db=db, db_session=db_session, class_table=House)
        db.close()
        db_session.commit()
    elif len(file) > 7 and file[0:7] == 'HSTSTAT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_house_state_status(db=db, db_session=db_session, class_table=HouseStateStatus)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'INTVSTAT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_interval_status(db=db, db_session=db_session, class_table=IntervalStatus)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'NDOCTYPE':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_doc_type(db=db, db_session=db_session, class_table=DocType)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:6] == 'NORDOC':
        db_name = direction + "/" + file
        try:
            db = dbf.Table(db_name, codepage='cp866', default_data_types='enhanced')
            db.open()
            add_normative_document(db=db, db_session=db_session, class_table=NormativeDocument)
            db.close()
            db_session.commit()
        except KeyError:
            print("KeyError" + db_name)
    elif len(file) > 8 and file[0:8] == 'OPERSTAT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_oper_stat(db=db, db_session=db_session, class_table=OperStat)
        db.close()
        db_session.commit()
    elif len(file) > 4 and file[0:4] == 'ROOM' and file[0:5] != 'ROOMT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_room(db=db, db_session=db_session, class_table=Room)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'ROOMTYPE':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_room_type(db=db, db_session=db_session, class_table=RoomType)
        db.close()
        db_session.commit()
    elif len(file) > 8 and file[0:8] == 'SOCRBASE':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_address_object_type(db=db, db_session=db_session, class_table=AddressObjectType)
        db.close()
        db_session.commit()
    elif len(file) > 5 and file[0:5] == 'STEAD':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_stead(db=db, db_session=db_session, class_table=Stead)
        db.close()
        db_session.commit()
    elif len(file) > 7 and file[0:7] == 'STRSTAT':
        db_name = direction + "/" + file
        db = dbf.Table(db_name, codepage='cp866')
        db.open()
        add_structure_status(db=db, db_session=db_session, class_table=StructureStatus)
        db.close()
        db_session.commit()