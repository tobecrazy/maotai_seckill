# -*- coding: UTF-8 -*-
import sys
import time
from jd_spider_requests import JdSeckill

if __name__ == '__main__':
    usages = """                                                                                                                                                                                          
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
 3.查看当前时间
"""
    print(usages)
    jd_seckill = JdSeckill()
    choice_function = input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    elif choice_function == '3':
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        sys.exit(1)
    else:
        print('没有此功能')
        sys.exit(1)
