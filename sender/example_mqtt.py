import sys
import logging
import time
from hub.hub import QcloudHub

provider = QcloudHub(device_file="./device_info.json", tls=True)
qcloud = provider.hub
logger = qcloud.logInit(qcloud.LoggerLevel.DEBUG, "logs/log", 1024*1024*10, 5, enable=True)

def on_connect(flags, rc, userdata):
    logger.debug("%s:flags:%d,rc:%d,userdata:%s" % (sys._getframe().f_code.co_name, flags, rc, userdata))
    pass


def on_disconnect(rc, userdata):
    logger.debug("%s:rc:%d,userdata:%s" % (sys._getframe().f_code.co_name, rc, userdata))
    pass


def on_message(topic, payload, qos, userdata):
    logger.debug("%s:topic:%s,payload:%s,qos:%s,userdata:%s" % (sys._getframe().f_code.co_name, topic, payload, qos, userdata))
    pass


def on_publish(mid, userdata):
    logger.debug("%s:mid:%d,userdata:%s" % (sys._getframe().f_code.co_name, mid, userdata))
    pass


def on_subscribe(mid, granted_qos, userdata):
    logger.debug("%s:mid:%d,granted_qos:%s,userdata:%s" % (sys._getframe().f_code.co_name, mid, granted_qos, userdata))
    pass


def on_unsubscribe(mid, userdata):
    logger.debug("%s:mid:%d,userdata:%s" % (sys._getframe().f_code.co_name, mid, userdata))
    pass


def publish_msg(topic, qos, message, device):
    context = '{"action": "%s", "targetDevice": "%s"}' % (message, device)
    logger.debug("publish %s" % context)
    qcloud.publish(topic, context, qos)
    pass


def topic_name(topic):
    product_id = qcloud.getProductID()
    device_name = qcloud.getDeviceName()
    topic_format = "%s/%s/%s"
    return topic_format % (product_id, device_name, topic)

def wait_for_connected():
    count = 0
    while True:
        if qcloud.isMqttConnected():
            break
        else:
            if count >= 3:
                # logger.error("\033[1;31m mqtt test fail...\033[0m")
                print("\033[1;31m mqtt test fail...\033[0m")
                # return False
                # 区分单元测试和sample
                return True
            time.sleep(1)
            count += 1


def example_mqtt():
    logger.debug("\033[1;36m mqtt test start...\033[0m")

    qcloud.registerMqttCallback(on_connect, on_disconnect,
                            on_message, on_publish,
                            on_subscribe, on_unsubscribe)
    qcloud.connect()
    wait_for_connected()

    count = 0
    number_of_msg = int(sys.argv[1])

    while True:
        if count >= number_of_msg:
            logger.info("finish running")
            break
        else:
            topic = topic_name('data')
            device_name = qcloud.getDeviceName()
            publish_msg(topic,1, sys.argv[2], device_name)
            count += 1

    qcloud.disconnect()

example_mqtt()