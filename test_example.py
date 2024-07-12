# test_example.py

import pytest
import tempfile
import os


# Определение фикстуры
@pytest.fixture
def temp_file():
    # Создание временного файла
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(b'Test data')
    temp.close()

    # Возврат имени временного файла
    yield temp.name

    # Удаление временного файла после завершения теста
    try:
        os.remove(temp.name)
    except OSError:
        pass


# Использование фикстуры в тесте
def test_temp_file_content(temp_file):
    with open(temp_file, 'r') as file:
        data = file.read()
    assert data == 'Test data'
