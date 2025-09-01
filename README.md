# fwerkor/nju-qiangke
南京大学校内选课辅助程序

## 免责声明
本项目的目的是帮助学习HTTP通信用法。

如果用于抢课，产生的一切后果由使用者本人承担！

请勿提高发包频率！建议发包延时不低于60秒，以免过度影响手动选课的同学的体验，破坏选课公平性。

发包延时低于0.5秒时，将有极大概率影响学校服务器运行，可能收获处分！

严禁滥用！！！

本项目开发者不对将该程序应用于抢课所造成的后果负责！！！

## 使用方法

### 配置环境

本项目使用基于Python3环境搭建，用到requests等扩展，详见`requirements.txt`。

```shell
pip3 install -r requirements.txt
```

项目运行时需要连接xk.nju.edu.cn，仅当设备连接至校园网或使用学校VPN时可用！

### 运行

```shell
python3 main.py
```

### 参数获取

#### studentCode
即学号

#### token、cookie、addParam值
最简单的获取方法：使用电脑浏览器打开选课界面，按F12打开开发者工具，点击“网络”（“Network”）,发起一次选课尝试（失败的），然后找到其中的Post请求。

## 友情链接
[南京大学选课平台](https://xk.nju.edu.cn)
