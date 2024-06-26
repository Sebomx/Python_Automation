# Фикстуры можно хранить в данном конфиге
# Примеры

import pytest

@pytest.fixture
def input_value():
    input = 39
    return input





'''
#from sqlalchemy import create_engine, ForeignKey


#Пример фикстуры для http клиента к приложению
@pytest.fixture(scope="function")
def client():
    return TestClient(app=app)


#Пример фикстуры для создания временной БД на базе SQLAlchemy
@pytest.fixture(scope="function")
def tmp_database() -> Generator:
    try:
        create_database(settings.POSTGRES_URL_SYNC_CLIENT)
        yield settings.POSTGRES_URL_SYNC_CLIENT
    finally:
        drop_database(settings.POSTGRES_URL_SYNC_CLIENT)
'''
