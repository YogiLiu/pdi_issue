from dependency_injector.wiring import Provide


class UserRepo:
    engine = Provide['engine']

    def do_something(self):
        print(self.engine)
