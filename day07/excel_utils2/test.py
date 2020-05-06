import xlwt
import xlrd
from xlutils.copy import copy
class ExcelUtils(object):
    #工具类的方法：不适用外部变量
    #静态方法：直接可以用类名.方法名来调用
    # @staticmethod
    #类变量：
    #实例变量

    #类方法
    @staticmethod
    def write_to_excel(filename,sheetname,word_list):
        '''
        写入excel
        :param filename: 文件名
        :param sheetname: 表单名
        :param word_list: [item,item,{}]
        :return:
        '''
        try:
            # 创建workbook
            workbook = xlwt.Workbook(encoding='utf-8')
            # 给工作表添加sheet表单
            sheet = workbook.add_sheet(sheetname)
            # 设置表头
            head = []
            for i in word_list[0].keys():
                head.append(i)
            # print(head)
            # 将表头写入excel
            for i in range(len(head)):
                sheet.write(0, i, head[i])
            # 写内容
            i = 1
            for item in word_list:
                for j in range(len(head)):
                    sheet.write(i, j, item[head[j]])
                i += 1
            # 保存
            workbook.save(filename)
            print('写入excle成功！')
        except Exception as e:
            print(e)
            print('写入失败！')
    @staticmethod
    def write_to_excel_append(filename,infos):
        '''
        追加excel的方法
        :param filename: 文件名
        :param infos: 【item，item】
        :return:
        '''
        #打开excle文件
        work_book = xlrd.open_workbook(filename)
        #获取工作表中的所有sheet表单名称
        sheets = work_book.sheet_names()
        #获取第一个表单
        work_sheet = work_book.sheet_by_name(sheets[0])
        #获取已经写入的行数
        old_rows = work_sheet.nrows
        #old_rows = work_sheet.nrows
        #获取表头的所有字段
        keys = work_sheet.row_values(0)
        # print('===================',keys)
        #将xlrd对象转化成xlwt，为了写入
        new_work_book = copy(work_book)

        #获取表单来添加数据
        new_sheet = new_work_book.get_sheet(0)
        i = old_rows
        for item in infos:
            for j in range(len(keys)):
                new_sheet.write(i, j, item[keys[j]])
            i += 1

        new_work_book.save(filename)
        print('追加成功！')
