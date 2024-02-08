from Tests import  test_first, test_second, test_third
from seleniumClass import SeleniumInterface
import pytest

@pytest.fixture(scope="session")
def browser():
    connect = SeleniumInterface()
    driver = connect.CreateConnection() 
    yield driver
    connect.CloseConnection(driver)
    
