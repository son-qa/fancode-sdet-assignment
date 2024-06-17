import pytest
from configurations.test_configs import test_configuration
from modules.users import Users


@pytest.fixture(scope='session')
def instatiate_users():
    env = test_configuration['env']
    users = Users(env=env)
    yield users
    del users
