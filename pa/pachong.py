# -*- coding: utf-8 -*-
# url：https://movie.douban.com/top250
import importlib
import random
import sys
import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By

# 反爬虫设置--伪造IP和请求
ip = ['111.155.116.210', '115.223.217.216', '121.232.146.39', '221.229.18.230', '115.223.220.59', '115.223.244.146',
      '180.118.135.26', '121.232.199.197', '121.232.145.101', '121.31.139.221', '115.223.224.114']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest',
    'X-Forwarded-For': ip[random.randint(0, 10)],
    'Host': ip[random.randint(0, 10)]
}

importlib.reload(sys)

try:
    conn = pymssql.connect(host="172.20.8.110", port="31002", user="root", password="Wa@123456", database="fedx", charset="utf8")
except pymssql.OperationalError as msg:
    print("error: Could not Connection SQL Server!please check your dblink configure!")
    sys.exit()
else:
    cur = conn.cursor()


def main():
    for n in range(0, 10):
        count = n * 25
        url = 'https://movie.douban.com/top250?start=' + str(count)
        j = 1
        # if(n == 7):
        #     j = 5
        for i in range(j, 26):
            driver = webdriver.PhantomJS(desired_capabilities=headers)  # 封装浏览器信息
            driver.set_page_load_timeout(15)
            driver.get(url)  # 加载网页
            # data = driver.page_source  # 获取网页文本
            # driver.save_screenshot('1.png')  # 截图保存

            name = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/a/span")[0].text.replace('\'',
                                                                                                                '')
            ename = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/a/span")[1].text.replace("/",
                                                                                                                 "").replace(
                " ", "").replace('\'', '')
            try:
                otherName = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/a/span")[2].text.lstrip(
                    ' / ').replace("/", "|").replace(" ", "").replace('\'', '')
            except:
                otherName = ''
            info = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/p")[0].text.replace("/",
                                                                                                           "|").replace(
                " ", "").replace('\'', '')
            score = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/div/span[2]")[0].text.replace(
                '\'', '')
            number = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/div/span[4]")[0].text.replace(
                "人评价", "").replace('\'', '')
            remark = driver.find_elements(By.XPATH, "//ol/li[" + str(i) + "]/div/div/div/p/span")[0].text.replace('\'',
                                                                                                                  '')

            sql = "insert into Movies(Name,EName,OtherName,Info,Score,Number,Remark) values('" + name + \
                  "','" + ename + "','" + otherName + "','" + info + \
                  "','" + score + "','" + number + "','" + remark + "') "
            try:
                cur.execute(sql)
                conn.commit()
                print("第" + str(n) + "页，第" + str(i) + "条电影信息新增成功")
                time.sleep(30)
            except:
                conn.rollback()
                print("新增失败：" + sql)
            driver.quit()


if __name__ == '__main__':
    main()