from .container import SrvContainer, RepoContainer

if __name__ == '__main__':
    container = SrvContainer()
    container.init_resources()

    user_repo = container.repo.user()
    user_repo.do_something()

    container.shutdown_resources()

    # container = RepoContainer()
    # container.init_resources()

    # user_repo = container.user()
    # user_repo.do_something()

    # container.shutdown_resources()
