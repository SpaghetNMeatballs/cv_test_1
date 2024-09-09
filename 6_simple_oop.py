from msuai import BaseClass


class ChildClass(BaseClass):
    def prime_check(self):
        for i in range(2, self.value - 1):
            if self.value % i == 0:
                self.is_prime = False
                return
        self.is_prime = True


a = ChildClass()
a.submit()
