# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/5/8 15:59'
import  MySQLdb,uuid
from scrapy.utils.project import get_project_settings #导入setting文件
import  xlrd,xlwt,logging
from datetime import date,datetime
from bjjs.db.dbhelper import DBHelper

def read_excel():
    workbook = xlrd.open_workbook("Z:\\Users\\wumingxing\\Desktop\\20190507_1.xlsx")
    for i in range(len(workbook.sheets())):
        sheet = workbook.sheet_by_index(i)
        trs_code = sheet.row_values(0)[1]
        trs_name = sheet.row_values(1)[1]
        fuc_desc = sheet.row_values(2)[1]
        input_start_index = ''
        input_end_index = ''
        # 第一次循环定位输入、输出的index
        for row  in range(sheet.nrows)[6:]:
            sheet_row_values = sheet.row_values(row)
            if (sheet_row_values[0]=='输入'):
                input_start_index=row
            if (sheet_row_values[0]=='输出'):
                input_end_index = row
        # 第二次循环，确认每条记录是输入项还是输出项
        #temp结果集中已经过滤掉输入、输出
        for row in range(sheet.nrows)[6:]:
            sheet_row_values = sheet.row_values(row)
            if (sheet_row_values[0] != '输入' and sheet_row_values[0] != '输出' and row > int(input_start_index) and row < int(input_end_index)):
                sheet_row_values.append('in')
                sheet_row_values.insert(0,fuc_desc)
                sheet_row_values.insert(0, trs_name)
                sheet_row_values.insert(0, trs_code)
            if (sheet_row_values[0] != '输入' and sheet_row_values[0] != '输出'  and row > int(input_end_index)):
                sheet_row_values.append('out')
                sheet_row_values.insert(0, fuc_desc)
                sheet_row_values.insert(0, trs_name)
                sheet_row_values.insert(0, trs_code)
            if (sheet_row_values[0] != '输入' and sheet_row_values[0] != '输出'):
                insert_db(sheet_row_values)

def insert_db(values):
    print (values)
    line=[]
    trs_code =values[0]
    trs_name = values[1]
    fuc_desc = values[2]
    eng_name = values[3]
    chinese_name = values[4]
    data_type = values[5]
    required = values[7]
    remark = values[-3]
    flag = values[-1]
    settings = get_project_settings()
    host = settings['MYSQL_HOST']
    db = settings['MYSQL_DBNAME']
    user = settings['MYSQL_USER']
    passwd = settings['MYSQL_PASSWD']
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=3306,charset="utf8")
    cur = db.cursor()
    insert_sql = """
    insert into api_api(id,trs_code,trs_name,fuc_desc,eng_name,chinese_name,data_type,required,remark,flag)
      values (%s,%s, %s, %s,%s,%s,%s, %s,%s,%s)
        """
    cur.execute(insert_sql,
                (str(uuid.uuid1()),trs_code, trs_name,fuc_desc,eng_name,chinese_name,data_type, required,remark,flag)
                )
    db.commit();
    # line=[trs_code,trs_name,func_des,eng_name,chinese_name,data_type,required,remark,flag]
    # print (line)
    # db.insert_api(line)


if __name__ == '__main__':
    read_excel()