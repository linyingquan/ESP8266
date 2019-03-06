'''
这是一个部署mqtt的，代码示例
会将dht22温湿度传感器的数据上传到mqtt服务器上
'''
import dht
import machine
import time
from ubinascii import hexlify
from umqtt.simple import MQTTClient

# 定义引脚
DHT = dht.DHT22(machine.Pin(4))

# CLIENT_ID: 每个 mqtt 客户端有自己独立的 client_id 标识
# 无所谓是什么，但不同客户端不能相同。此处我们使用 8266 的 unique_id
client_id = hexlify(machine.unique_id()).decode()

# 定义mqtt服务器ip地址，用户名和密码
mqtt_broker = "192.168.43.3"
mqtt_user = 'pi'
mqtt_passwd = '123456'

# 定义主题订阅位置
TEM_TOPIC = "my/test/dht/temperature"
HUM_TOPIC = "my/test/dht/humidity"

# 等待 15 秒，wifi 自动连接上再运行
time.sleep(15)

# 将数据上传到mqtt服务器
mqtt = MQTTClient( client_id, mqtt_broker, 1883, mqtt_user, mqtt_passwd)
# 连接mqtt服务器
mqtt.connect()
print("连接到服务器：{s}".format(s=mqtt_broker))

# 不断循环，每 10 秒测量一次温度和湿度，发布到 mqtt 服务器上
while True:

    try:
        DHT.measure()
    except:
        print("NO dht Pin(%d)"%(PIN_NO))
        break
    print("测量到的温度： %d ; 湿度： %d"%(DHT.temperature(), DHT.humidity()))

    mqtt.publish(TEM_TOPIC, str(DHT.temperature()).encode(), retain=True)
    mqtt.publish(HUM_TOPIC, str(DHT.humidity()).encode(), retain=True)
    time.sleep(10)
