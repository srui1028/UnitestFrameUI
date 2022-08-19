'''
    这个文件用来读取yaml数据
'''
import yaml


# 读取yaml方法
def loadyaml(filename):
    files = open(filename, 'r', encoding='utf-8')
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

# 打印读取结果
# a =loadyaml('../data/user.yaml')
# print(a)
