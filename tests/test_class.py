def test_transfer_data(test_class):
    assert test_class.moneys == "31957.58"
    assert test_class.currency == "руб."
    assert test_class.date == "2019-08-26T10:50:58.294041"
    assert test_class.description == "Перевод организации"
    assert test_class.to_whom == "Счет 64686473678894779589"


def test_data_date_and_description(test_class):
    assert test_class.data_date_and_description() == "26-08-2019 Перевод организации"


def test_data_from_whom(test_class):
    assert test_class.data_from_whom("Maestro 1596837868705199") == "Maestro 1596 37** **** 5199"
    assert test_class.data_from_whom("Maestro 15961213854993921675") == "Maestro 1596 21** **** **** 1675"


def test_data_to_whom(test_class):
    assert test_class.data_to_whom() == "Счет **9589"


def test_data_moneys(test_class):
    assert test_class.data_moneys() == "31957.58 руб."
