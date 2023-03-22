import pytest
from utils.transfer_data import TransferData


@pytest.fixture
def test_class():
    transfer_data = TransferData("2019-08-26T10:50:58.294041", "Перевод организации", "Счет 64686473678894779589",
                                 "31957.58", "руб.")
    return transfer_data
