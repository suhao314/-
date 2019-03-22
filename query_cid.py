# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:21:41 2019

@author: suhao314
"""
#该程序将expData中出现的cid进行查询，将坐标，电荷，原子序数插入compoundCoordinates
import pymysql
import pubchempy as pcp

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
        print("======NotFound!======")
        continue
    else:
        for j in c.atoms:
            sql_string = "insert into compoundCoordinates (aid, cidType, cid, atomicNumber, charge,x,y,z)\
                        values(%d, 1, %d, %d, %d, %f, %f, %f);"\
                        %(j.aid, row[0], j.number, j.charge, j.x, j.y, j.z)
            #print(sql_string)
            cursor.execute(sql_string)
        db.commit()
        print("Query Sucess!")
