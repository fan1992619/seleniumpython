import logging
import os
import datetime
class UserLog:
    def __init__(self):
        #使用日志模块，是为了部署到服务器的时候，能看到日志来解决问题
        #设置成一个对象
        self.logger=logging.getLogger()
        #设置一个日志的等级
        self.logger.setLevel(logging.INFO)
        #还需设置一个流，以流的形式来输出。调用StreamHandler()方法就相当于创建了一个流。代表控制台输出日志
        # consle=logging.StreamHandler()
        #文件路径
        #os.path.abspath(__file__)当前文件路径，os.path.dirname(os.path.abspath(__file__))当前文件路径的上一路径
        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_dir=os.path.join(base_dir,"logs")
        log_file=datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name=log_dir+"/"+log_file
        # print(log_name)
        #日志输出到文件,必须加上'a',encoding='utf-8'，不然会报错
        self.file_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
        #添加日志格式
        formatter=logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
        #把文件设置成格式的形式
        self.file_handle.setFormatter(formatter)
        #添加一个流
        self.logger.addHandler(self.file_handle)
        self.logger.debug("test")
    def get_log(self):
        return self.logger
    def close_log(self):
        #关闭日志,为了性能，如果多性能没有要求可以不用关闭
        self.file_handle.close()
        #logger也需要关闭
        self.logger.removeHandler(self.file_handle)
if __name__ == '__main__':
    user=UserLog()
    user.get_log()