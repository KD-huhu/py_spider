import xlwt
import xlrd
from xlutils.copy import copy


class ExcelUtils(object):
    # 工具类的方法：不适用外部变量
    # 静态方法：直接可以用类名.方法名来调用
    # @staticmethod
    # 类变量：
    # 实例变量
    @staticmethod
    def write_to_excel(filename,sheetname,word_list):
        '''
        将传入的word_list写入excel文件中
        :param filename:文件名
        :param sheetname:表单名
        :param word_list:写入内容,word_list是列表，列表内容是字典
        :return:
        '''
        try:
            # 创建workbook
            workbook = xlwt.Workbook(encoding='utf-8')
            # 给工作表添加sheet表单
            sheet = workbook.add_sheet(sheetname)
            # 获得表头
            head = []
            for i in word_list[0].keys():
                head.append(i)
            # 将表头写入excel
            for i in range(len(head)):
                sheet.write(0,i,head[i])
            # 将内容写入表格中
            i = 1
            for item in word_list:
                for j in range(len(head)):
                    # print(item[head[j]])
                    sheet.write(i,j,item[head[j]])
                i += 1
            # 保存文件
            workbook.save(filename)
            print('写入excel成功！')
        except Exception as e:
            print(e)
            print('写入excel失败！')


    @staticmethod
    def write_to_excel_append(filename,sheetname,infor):
        '''
        在已有excel中追加内容的方法
        :param filename: excel文件名
        :param sheetname: 工作表名
        :param infor: 追加内容
        :return:
        '''
        # 打开excel文件
        work_book = xlrd.open_workbook(filename)
        # 获取表单名
        sheets = work_book.sheet_names()
        # 寻找对应的表单
        for i in range(len(sheets)):
            if sheetname == sheets[i]:
                # work_sheet = sheets[i]
                break
        # 找到表单就直接追加
        if i < len(sheets):
            work_sheet = work_book.sheet_by_name(sheets[i])
        # 找不到就创建一个表单
        else:
            work_sheet = work_book.add_sheet(sheetname)
        # 获取已经写入的行数
        old_rows = work_sheet.nrows
        # 获取表头的所有字段
        keys = work_sheet.row_values(0)
        # 将xlrd对象转化成xlwt，为了写入
        new_work_book = copy(work_book)

        # 获取表单来添加数据
        new_sheet = new_work_book.get_sheet(i)
        i = old_rows
        for item in infor:
            for j in range(len(keys)):
                new_sheet.write(i,j,item[keys[j]])
            i += 1

        new_work_book.save(filename)
        print('追加excel成功！')