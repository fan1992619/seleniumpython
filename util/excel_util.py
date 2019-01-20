#如何按照数据驱动格式获取excel的内容
#新建excel的时候一定要注意设置单元格的格式，这样输入进去的数字才能以文本的形式进行处理
#有时候输入11111，拿出来说是11111.0，只需要在excel设置为文本格式后，双击该数字单元格，然后左上角
#有格实心的小三角就可以了
import sys
sys.path.append('D:\PycharmProjects\Web-selenium')
import xlrd
from xlutils.copy import copy
class ExcelUtil():
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path='D:\PycharmProjects\Web-selenium\config\keyword.xls'
        else:
            self.excel_path=excel_path
        if index==None:
            self.index=0
        self.data=xlrd.open_workbook(self.excel_path)
        #获取excel哪一个表
        self.table=self.data.sheets()[self.index]
    # 获取每一行的所有数据，然后添加到一个list里面
    def get_data(self):
        res=[]
        rows=self.get_line()
        if rows != None:
            for i in range(rows):
                col=self.table.row_values(i)
                res.append(col)
            return res
        return None
    #获取excel的行数
    def get_line(self):
        #获取行数
        rows=self.table.nrows
        if rows >=1:
            return rows
        return None
    #获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_line()>= row:
            data=self.table.cell(row,col).value
            return data
        return None
    #写入数据
    def write_data(self,row,col,value):
        read_data=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_data)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save('D:\PycharmProjects\Web-selenium\config\keyword.xls')
if __name__ == '__main__':
    ex=ExcelUtil()
    print(ex.get_col_value(3,4))
