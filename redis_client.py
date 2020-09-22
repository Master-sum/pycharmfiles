"""
作者   ：bjx
创建时间   ：2020/9/12  6:15 下午 
文件名称   ：redis_client.PY
开发工具   ：PyCharm
"""
import redis
import threading

#创建锁
locks = threading.local()
locks.redis = {}
#提醒返回值
def key_for(user_id):
    return "{}".format(user_id)
#定义一个私有方法
def _unlock(client,key):
    client.deleta(key)#释放锁
#创建锁
def _lock(client,key):
    return bool(client.set(key,True,nx=True,ex=5))#创建锁的参数
#定义一个方法使用
def lock(client,user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] += 1
        return True
    ok = _lock(client,key)
    if not ok:
        return False
    locks.redis[key] += 1
    return True

def unlock(client,user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1
        if locks.redis[key] <= 0:
            del locks.redis[key]
        return True

    return False
client = redis.StrictRedis()
print("lock",lock(client,"ccc"))