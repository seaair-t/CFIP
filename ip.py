import requests
from bs4 import BeautifulSoup

# 目标网址
url = 'https://ipdb.030101.xyz/bestcf/'

# 发送HTTP请求获取网页内容
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找嵌套的CSV文件链接
script_tag = soup.find('script', string=lambda text: text and 'bestcf.csv' in text)
csv_url = 'https://ipdb.030101.xyz/api/bestcf.csv'

# 发送HTTP请求获取CSV文件内容
csv_response = requests.get(csv_url)
csv_response.raise_for_status()  # 检查请求是否成功

# 解析CSV文件内容并提取第一列数据，去掉第一行和最后一行
csv_content = csv_response.text
lines = csv_content.split("\n")
first_column_data = [line.split(",")[0] for line in lines[1:-1] if line.strip()]

# 将第一列数据保存到txt文件，每行后面加上'#优选IP'，指定编码为utf-8
with open('first_column_data.txt1', 'w', encoding='utf-8') as file:
    for item in first_column_data:
        file.write(f"{item} #HK\n")

print('第一列数据已保存到first_column_data.txt文件中')
