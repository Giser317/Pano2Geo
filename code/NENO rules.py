import csv
import xlrd
import math


def duquExcel(path):
    excel = xlrd.open_workbook(path)
    excel.sheet_names()  
    sheet = excel.sheet_by_index(0)  
    rows=[]
    for i in range(1, sheet.nrows):
        row_list = sheet.row_values(i)
        rows.append(row_list)
    return rows


def chaifenByPoints(rows,streetViewPoints):
    streetViewPoints=[]
    for i in range(1,streetViewPoints):
        result=[]
        for row in rows:   
            if int(row[1])==i:
                result.append(row)
        AngleDic,lenDic,resultDic=crearDic(result)
        pointNumber=len(result)
        buildingNumber=len(AngleDic)
        triangleType=solvTriangle(resultDic)
        angle_sum=angleSum(AngleDic)
        item=[i,buildingNumber,pointNumber,angle_sum,triangleType]
        streetViewPoints.append(item)
    return streetViewPoints


def crearDic(rows):
    AngleDic={}
    lenDic={}
    resultDic={}
    for row in rows:
        if int(row[6]) not in AngleDic.keys():
            AngleDic[int(row[6])]=[float(row[3])]
        else:
            AngleDic[int(row[6])].append(float(row[3]))
        if int(row[6]) not in lenDic.keys():
            lenDic[int(row[6])]=[float(row[4])]
        else:
            lenDic[int(row[6])].append(float(row[4]))
        if int(row[6]) not in resultDic.keys():
            resultDic[int(row[6])]={float(row[3]):float(row[4])}
        else:
            dic={float(row[3]):float(row[4])}
            resultDic[int(row[6])].update(dic)
    return AngleDic,lenDic,resultDic


def angleSum(dic):
    sum=0
    for key in dic.keys():
        sum=(max(dic[key])-min(dic[key]))+sum
        if sum>=180:
            term=sorted(dic[key])
            try:
                sum=(360-max(dic[key]))+term[-2]
            except:
                sum = (360 - max(dic[key])) + min(dic[key])

    return sum

def solvTriangle(dic):
    triangleType=0
    for key in dic.keys():
        print(str(key)+'`````````'+str(dic[key]))
        if len(dic[key])==2:
            building=dic[key]
            bian=list(building.values())
            jiajiao=max(list(building.keys()))-min(list(building.keys()))
            if jiajiao>=90:
                triangleType=triangleType+1
            else:
                c = math.sqrt(bian[0]** 2 + bian[1]** 2 - 2 * bian[0] * bian[1] * math.cos(jiajiao * math.pi / 180))
                cosa=(bian[1]**2+c**2-bian[0]** 2)/(2*bian[1]*c)
                jiaoa=math.acos(cosa)
                a=jiaoa*180/math.pi
                cosb = (bian[0] ** 2 + c ** 2 - bian[1] ** 2) / (2 * bian[0] * c)
                jiaob=math.acos(cosb)
                b=jiaob*180/math.pi
                if a>90 or b >90:
                    triangleType=triangleType+0
                else:
                    triangleType=triangleType+1
        else:
            continue
    return triangleType


def xieruCSV(rows,path):
    f=open(path,'a',newline='')
    for i in rows:
        csv_write=csv.writer(f)
        try:
            csv_write.writerow(i)
        except:
            continue
    f.close()



streetViewPoints=0
excelPath=r"constructSightLines.xls"
rows=duquExcel(excelPath)
points=chaifenByPoints(rows,streetViewPoints)
outputPath=r''
xieruCSV(points,outputPath)