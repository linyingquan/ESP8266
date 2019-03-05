# ESP8266  Python使用方法
## MicroPython简介

- 官网介绍（http://www.micropython.org/）

        MicroPython是Python 3编程语言的精简高效实现 ，包括Python标准库的一小部分，并且经过优化，可在微控制器和受限环境中运行。

        MicroPython pyboard是一个紧凑的电子电路板，在裸机上运行MicroPython，为您提供一个低级Python操作系统，可用于控制各种电子项目。

        MicroPython包含许多高级功能，如交互式提示，任意精度整数，闭包，列表理解，生成器，异常处理等。然而它非常紧凑，可以在256k的代码空间和16k的RAM内运行。

        MicroPython旨在尽可能与普通Python兼容，以便您轻松地将代码从桌面传输到微控制器或嵌入式系统。
        
    
- 在ESP8266上运行MicroPython
    -  开发环境
        - ESP NodeMCU
        - Windows10 64位
    - 安装esptool
    
            # 需要安装python环境
            pip install esptool

    - 安装MicroPython固件
        - 在官网上下载最新固件（http://micropython.org/download#esp8266）
        - 将NodeMCU用数据线与电脑链接，并在cmd命令窗口使用mode查看com口
        - 使用命令写入固件
        
                # 清空原有固件，如果报错没有该命令则需要使用esptool.py ...
                esptool --port COMx erase_flash
                
                # 写入固件
                esptool --port COMx --baud 115200 write_flash 0 esp8266-20180511-v1.9.4.bin
                （部分型号的 NodeMCU，需增加命令参数 -fm dio）
                
    - 使用putty链接开发板
        - 使用串口连接 COMx
        - 速率设置为 115200
        - 将 Serial /FLow control 设置为None
        - 输入回车键即会显示输入提示符
        
## Micro Python 常用库

- machine 库

        import machine
        # 设置 p2 为 gpio 2号口，并设置为输出
        p2 = machine.Pin(2,machine.Pin.OUT)
        # 熄灭
        p2.value(1)
        #点亮
        p2.value(0)
     
- os 库
    - 对文件系统进行操作
    - 常用文件系统操作命令
    
            os.statvfs('/')     # 查看文件系统状态
            os.listdir()        # 列出当前目录下文件
            os.mkdir('xxxx')    # 创建目录
            os.rmdir('xxxx')    # 删除目录
            os.stat('test.py')  # 列出文件状态
            os.rename('test.py','test.py.bak')  # 修改文件名
            os.remove('test.py.bak')            # 删除文件
            
            # 打印文件内容
            f=open('boot.py','r')
            f.read()
            f.close()

- network 库
    - 对网卡进行操作
    - 常用命令
    
            sta_if = network.WLAN(network.STA_IF)   # 设置工作站网卡 sta_if
            sta_if.active(True)                     # 开启网卡
            sta_if.connect('xxx','yyy')             # 连接 wifi 网络，名称为 xxx，密码为 yyy
            sta_if.active()                         # 查询网卡是否激活
            sta_if.isconnected()                    # 查询网络是否连接
            sta_if.ifconfig()                       # 查询网络连接信息
            sta_if.active(False)                    # 关闭网卡
            
            # 设置热点，热点名为Micropython... , 密码为：micropythoN
            ap_if = network.WLAN(network.AP_IF)             # 设置热点网卡 ap_if
            ap_if.config(essid="abc", password="12345678")  # 设置热点与密码
            ap_if.config("essid")                           # 查看设置的热点
            sta_if.active(False)                            # 关闭热点
            
                
- webrepl_setup 库
    - 操作web界面
    - 输入 e 
    - 输入 密码
    - 输入 y
    - 浏览器访问 webrepl 网页（http://micropython.org/webrepl/）
    - 修改 IP 地址
    
- time 库
    - 操作时间的函数
    - 常用命令
    
            time.sleep(1)  # 延时1秒
            
            
- dht 库
    - dht 操作温湿度传感器
            
            import dht
            import machine
            # 将4号引脚设置为dht11传感器
            d1 = dht.DHT11(machine.Pin(4))
            # 测量一次
            d1.measure()
            # 返回测量的温湿度
            d1.temperature()
            d1.humidity()
            
- MQTTClient 库
    - 
    
            
- 基本使用方法
    - 编译环境会自动出现缩进，连续按4次回车，即开始运行程序，CTRL + C 终止程序
    - 按 Ctrl + e 进入粘贴模式，CTRL + D 退出即可
    - 也可以保存为.py文件，使用 webrepl 上传文件，import 文件名 即可运行该程序
    - 每次esp8266上电后会自动运行 main.py 函数

