import logging  # 引入logging模块
import os.path
import time


class LogSave:
    def log_info(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 将logger添加到handler里面
        logger.addHandler(fh)
        logger.info(' --------------------------- info log ---------------------------')



    def log_debug(self, content):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Log等级总开关
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 将logger添加到handler里面
        logger.addHandler(fh)
        logger.debug(content)

if __name__ == '__main__':
    log_save = LogSave().log_info()

    logger = logging.getLogger()
    logger.info('2222222222222222222222222222222')
    logger.info('1111111111')

