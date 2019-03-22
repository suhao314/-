# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:42:08 2019

@author: suhao314
"""

#generate from db to gjf
#根据expData表中的cid在compoundCoordinates_TEST中查询并生成gaussian输入文件
#gaussian文件：<电荷， 自旋多重度>

import pymysql
db = pymysql.connect("","","","" )
cursor = db.cursor()
cursor.execute("select distinct cid from expData where cid = 144;")
results = cursor.fetchall()
gjf = "%nprocshared=4\n%mem=2GB\n# opt m062x/3-21g\n\nTitle Card Required\n\n "

#哈希表,下标从0开始
atomHashList = \
(' ','H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',\
 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',\
 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Te', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', \
 'Te','I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', \
 'Tm','Yb','Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',\
 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm','Md', 'No', 'Lr',\
 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Uue')

for row in results:
    print("--------------------------------------------------")
    print(row[0])
    sql_string1 = "select atomicNumber, x, y, z from compoundCoordinates_TEST where cid = %d;"%(row[0])
    cursor.execute(sql_string1)
    cresult1 = cursor.fetchall()
    sql_string2 = "select sum(charge) from compoundCoordinates_TEST where cid = %d;"%(row[0])
    cursor.execute(sql_string2)
    cresult2 = cursor.fetchall()
    print(str(cresult2[0][0]))
    gjf = gjf + str(int(cresult2[0][0])).strip(' ') + ' 1\n'
    for j in cresult1:
        gjf = gjf + atomHashList[j[0]] +'                 ' + str(j[1]) + '    ' + str(j[2]) + '    ' + str(j[3]) + '\n'
    print(gjf)
