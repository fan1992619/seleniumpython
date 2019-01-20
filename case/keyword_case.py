import sys
sys.path.append('D:\PycharmProjects\Web-selenium')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def __init__(self):
        self.hand_excel=ExcelUtil()
        self.action_method=ActionMethod()
    def run_main(self):
        case_line=self.hand_excel.get_line()
        if case_line :
            for i in range(1,case_line):
                # self.hand_excel.write_data(i,9,'test')
                # continue
                is_run=self.hand_excel.get_col_value(i,3)
                if is_run=='yes':
                    #执行方法
                    method=self.hand_excel.get_col_value(i, 4)
                    # print(method)
                    #输入的数据
                    send_value=self.hand_excel.get_col_value(i, 5)
                    # print(send_value)
                    #操作元素
                    hand_value=self.hand_excel.get_col_value(i, 6)
                    # print(hand_value)
                    #预期结果
                    except_result_method=self.hand_excel.get_col_value(i,7)
                    #实际结果
                    except_result=self.hand_excel.get_col_value(i,8)
                    self.run_menthod(method,send_value,hand_value)
                    if except_result!='':
                        result_value=self.get_except_result_value(except_result)
                        if result_value[0]=='text':
                            print('---->',except_result_method)
                            res=self.run_menthod(except_result_method)
                            print(res,"------------>title")
                            if result_value[1] in res:
                                self.hand_excel.write_data(i,9,'pass')
                            else:
                                self.hand_excel.write_data(i,9,'fail')
                        elif result_value[0]=='element':
                            print(except_result_method)
                            #如果获取的元素是element，那么执行run_mentod方法，result_value[1]参数是掉get_element使用
                            res=self.run_menthod(except_result_method,result_value[1])
                            print(res,"-------------->element")
                            if res:
                                self.hand_excel.write_data(i,9,'pass')
                            else:
                                self.hand_excel.write_data(i,9,'fail')
                        else:
                            print('没有else')
                    else:
                        print("没有预期结果")
    #拆分预期结果，以“=”拆分
    def get_except_result_value(self,data):
        result=data.split('=')
        return result
    def run_menthod(self,method,send_value='',hand_value=''):
        #使用反射的方法获取self,action_method的对象_
        #getattr（）返回回来的是一个对象的值
        #如果send_value有值，就传入“输入的数据”和“操作元素”
        #如果有send_value没有值，操作元素有值，那就传一个操作元素
        #如果都没有值，就不传
        method_value=getattr(self.action_method,method)
        if send_value =='' and hand_value=='':
            result=method_value()
        elif send_value != '' and hand_value=='':
            result=method_value(send_value)
        elif send_value=='' and hand_value != '':
            #send_value==None and hand_value != None:不能这么写，不然会报错，以为在
            #excel_util.get_col_value()里面有一个判断，排除为空的情况。所以只能写成 ''
            result=method_value(hand_value)
        else :
            result=method_value(send_value,hand_value)
        return result
if __name__ == '__main__':
    run=KeywordCase()
    run.run_main()