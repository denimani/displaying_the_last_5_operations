from utils.sort_operations import last_five_operations


def test_last_five_operations():
    assert len(last_five_operations()) == 5
