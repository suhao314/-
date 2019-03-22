# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:21:41 2019

@author: suhao314
"""
#该程序将expData中出现的cid进行查询，将坐标，电荷，原子序数插入compoundCoordinates
#当查不到3D的坐标信息时查2D的坐标
import pymysql
import pubchempy as pcp
import time

db = pymysql.connect("","","","" )
cursor = db.cursor()
cursor.execute("select distinct cid from expData")
results = cursor.fetchall()
for row in results:
    print("-----------------------------------------")
    print(row[0])
    try:
        c = pcp.Compound.from_cid(row[0], record_type = '3d')
    except:
        print("3D======NotFound!======")
        c = pcp.Compound.from_cid(row[0])
        for j in c.atoms:
            sql_string = "insert into compoundCoordinates_TEST (aid, cidType, cid, atomicNumber, charge,x,y,z)\
                        values(%d, 1, %d, %d, %d, %f, %f, 0);"\
                        %(j.aid, row[0], j.number, j.charge, j.x, j.y)
            #print(sql_string)
            cursor.execute(sql_string)
        db.commit()
        print("++++++++++but succeed in 2D query!++++++++++")
        time.sleep(1)
        continue
    else:
        for j in c.atoms:
            sql_string = "insert into compoundCoordinates_TEST (aid, cidType, cid, atomicNumber, charge,x,y,z)\
                        values(%d, 1, %d, %d, %d, %f, %f, %f);"\
                        %(j.aid, row[0], j.number, j.charge, j.x, j.y, j.z)
            #print(sql_string)
            cursor.execute(sql_string)
        db.commit()
        print("Query Sucess!")
