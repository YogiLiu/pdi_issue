from .container import SrvContainer

if __name__ == '__main__':
    container = SrvContainer()
    container.init_resources()

    user_repo = container.repo.user()
    user_repo.do_something()

    container.shutdown_resources()
