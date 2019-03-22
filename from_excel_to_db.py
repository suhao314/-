# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:47:25 2019

@author: suhao314
"""
#从下列文件中读取信息，并将其插入至数据库的表中
#本质上将excel变成数据库的一个关系模式的实例
#目的数据库关系模式：expData
import pymysql

db = pymysql.connect("","","","" )
cursor = db.cursor()
                     
                     
fileobj_temp = open("C:/Users//Documents/bishe/temp.txt", "rt")
fileobj_solvent = open("C:/Users//Documents/bishe/solvent.txt", "rt")
fileobj_primkey = open("C:/Users//Documents/bishe/primary key.txt", "rt")
fileobj_ffname = open("C:/Users//Documents/bishe/ffname.txt", "rt")
fileobj_exeV = open("C:/Users//Documents/bishe/exeV.txt", "rt")
fileobj_emeV = open("C:/Users//Documents/bishe/emeV.txt", "rt")
fileobj_em = open("C:/Users//Documents/bishe/em.txt", "rt")
fileobj_CIDType = open("C:/Users//Documents/bishe/CIDType.txt", "rt")
fileobj_cid = open("C:/Users//Documents/bishe/cid.txt", "rt")
fileobj_abex = open("C:/Users//Documents/bishe/abex.txt", "rt")
fileobj_ab = open("C:/Users//Documents/bishe/ab.txt", "rt")

count = 0

while True:
    sql_string = "insert into expData (pk, ffname, cidType, cid, solvent, ab, temp, ael, eml, aeeV, emeV) values("
    
    field_1 = fileobj_primkey.readline()
    field_1 = field_1.strip('\n')
    
    field_2 = fileobj_ffname.readline()
    field_2 = field_2.strip('\n')
    field_2 = ',"' + field_2 + '",'
    
    field_3 = fileobj_CIDType.readline()
    field_3 = field_3.strip('\n')
    field_3 += ','
    
    field_4 = fileobj_cid.readline()
    field_4 = field_4.strip('\n')
    field_4 += ','
    
    field_5 = fileobj_solvent.readline()
    field_5 = field_5.strip('\n')
    field_5 = '"' + field_5 + '",'
    
    field_6 = fileobj_ab.readline()
    field_6 = field_6.strip('\n')
    field_6 = '"' + field_6 + '",'
    
    field_7 = fileobj_temp.readline()
    field_7 = field_7.strip('\n')
    field_7 += ','
    
    field_8 = fileobj_abex.readline()
    field_8 = field_8.strip('\n')
    field_8 += ','
    
    field_9 = fileobj_em.readline()
    field_9 = field_9.strip('\n')
    field_9 += ','
    
    field10 = fileobj_exeV.readline()
    field10 = field10.strip('\n')
    field10 += ','
    
    field11 = fileobj_emeV.readline()
    field11 = field11.strip('\n')
    field11 += ');'
    
    if not field_1:
        break
    
    count += 1
    
    sql_string = sql_string + field_1 + field_2 + field_3 + field_4 + field_5 \
    + field_6 + field_7 + field_8 + field_9 + field10 + field11
    
    print("-----------------------------")
    print(count)
    print(sql_string)
    
    try:
        cursor.execute(sql_string)
        db.commit()
    except:
        db.rollback()
        
db.close()
    
    