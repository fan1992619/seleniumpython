import configparser
class ReadIni():
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name="D:\PycharmProjects\Web-selenium\config\LocalElement.ini"
        if node == None:
            self.node="RegisterElement"
        else:
            self.node=node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    #获取值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data
if __name__ == '__main__':
    run_test = ReadIni()
    print(run_test.get_value('user_name'))