import threading
import time


class MyThread(threading.Thread):
    exitFlag = 0
    running = 0

    # 重写父类init方法（构造函数）
    def __init__(self,threadId,name):
        super(MyThread,self).__init__()
        self.threadId = threadId
        self.name = name
        self.flag = threading.Event()  # 用于暂停线程的标识
        self.flag.set()  # 设置为True
        self.running = threading.Event()  # 用于退出线程的标识
        self.running.set()  # 设置为True

    # 线程创建后直接运行run函数
    def run(self):
        print("starting:"+self.name)
        while self.running.isSet():
            self.flag.wait()
            print(self.name+": "+str(time.time()))
            time.sleep(1)
        print("ending:"+self.name)

    def pause(self):
        print("pause")
        self.flag.clear()  # 设置为False，让线程阻塞

    def resume(self):
        print("resume")
        self.flag.set()  # 设置为True，让线程停止阻塞

    def stop(self):
        print("stop")
        self.flag.set()  # 让线程从暂停恢复，如果已经暂停的话
        self.running.clear()  # 设置为False,用于线程的关闭


mThread = MyThread(1,"thread-1")
mThread.start()
time.sleep(3)
mThread.pause()
time.sleep(3)
mThread.resume()
time.sleep(3)
mThread.pause()
time.sleep(3)
mThread.stop()