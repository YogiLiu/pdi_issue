from dependency_injector import containers, providers


def create_engine():
    yield 'database engine'


class RepoContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.repo'])

    engine = providers.Resource(create_engine)
    # engine = providers.Factory(lambda: 'database engine')

    user = providers.Singleton('.repo.UserRepo')


class SrvContainer(containers.DeclarativeContainer):
    repo = providers.Container(RepoContainer)
