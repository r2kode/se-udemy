from math import sqrt


class ModulesDemo():

    def builtin_modules(self, param):
        return sqrt(param)


modules = ModulesDemo()
print(modules.builtin_modules(4))