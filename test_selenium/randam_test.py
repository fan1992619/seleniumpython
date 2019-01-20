import random
#使用随机函数生成随机数
def randam_str(str,num):
    res=''.join(random.sample(str,num))+"@163.com"
    # res = random.sample(str, num)不使用join转化生成的是一个list
    return res
resp=randam_str("1234567890andbg",6)
print(resp)