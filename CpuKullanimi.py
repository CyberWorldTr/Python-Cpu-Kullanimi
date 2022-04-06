# Python 100% Cpu Kullanımı Yapmak!! Kullanırken Dikkatli Olmakta Fayda Var :)
from threading import Thread


class Yukleme(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        for i in range(10000):
            msg = "%s Çalışıyor" % \
                self.name
            print(msg)

def create_threads():
    for i in range(1000):
        isim = "İs #%s" % (i + 1)
        islerim = Yukleme(isim)
        islerim.start()

if __name__ == "__main__":
    create_threads()