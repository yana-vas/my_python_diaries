from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(AbstractWorker):
    def work(self):
        print("I'm a robot. I'm working....")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of category {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "`worker` must be of category {}".format(Eatable)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


manager = Manager()
break_manager = BreakManager()

worker = Worker()
manager.set_worker(worker)
break_manager.set_worker(worker)
manager.manage()
break_manager.lunch_break()

super_worker = SuperWorker()
manager.set_worker(super_worker)
break_manager.set_worker(super_worker)
manager.manage()
break_manager.lunch_break()

robot = Robot()
manager.set_worker(Robot())
manager.manage()

break_manager.set_worker(robot)
