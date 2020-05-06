import xlwt

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