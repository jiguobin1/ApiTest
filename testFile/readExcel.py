# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 21:58 
# @Author : Ji
# @File : getpathInfo.py
import os
from testFile import getpathInfo# 自己定义的内部类，该类返回项目的绝对路径
# 调用读Excel的第三方库xlrd
import xlrd

path = getpathInfo.get_Path()


class readExcel():
    def __init__(self):
        pass

    #读取excel
    def get_excel_value(self,sheet,row,file_name=None):
        '''
        :param file_name:打开excel
        :param sheet: 获取页数
        :param row:
        '''
        if file_name == None:
            #默认地址
            file_name = 'D:\\liantuo\\ApiTest\\testFile\\case\\userCase.xls'
            # print(file_name)
        else:
            self.file_name=file_name
        book = xlrd.open_workbook(file_name) #打开一个excel
        sheet = book.sheet_by_name(sheet)
        data=sheet.row_values(row)
        return data
    def get_excel_info(self,sheet,row,file_name=None):
        data=(dict(zip(readExcel().get_excel_value(sheet,0),readExcel().get_excel_value(sheet,row-1))))
        data.pop('shuoming')
        return data


if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    # r=readExcel().get_excel_value('login',0)
    # print(r)
    print(readExcel().get_excel_info('login',2))
