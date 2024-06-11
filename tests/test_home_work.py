import pytest
from src.masks import masking_cards, check_mask
from src.processing import filter_by_state, sort_by_date


# тесты для маски номера карты
def test_mask_card(num_mask):
    assert masking_cards("7000792289606361") == num_mask

    with pytest.raises(TypeError):
        masking_cards()

    with pytest.raises(AttributeError):
        masking_cards(1234564789567465)


@pytest.mark.parametrize('value, expected', [
    ("123456478956746", "Не верно введен номер карты"),
    ("123456dsdf674653", "Не верно введен номер карты"),
])
def test_other(value, expected):
    assert masking_cards(value) == expected


# тесты для маски счета
def test_check_mask(tst_check_mask):
    assert check_mask("73654108430135874305") == tst_check_mask

    with pytest.raises(TypeError):
        check_mask()

    with pytest.raises(AttributeError):
        check_mask(1234564789567465)


@pytest.mark.parametrize('value, expected', [
    ("1234231534264576489", "Не верно введен номер счета"),
    ("12342315fgdh45764892", "Не верно введен номер счета"),
])
def test_check_mask_other(value, expected):
    assert check_mask(value) == expected


def test_filter(proces_test):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                           ) == proces_test


def test_filter():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                           "sdfxz") == "Введите корректный 2 аргумент"


def test_sort_date(sort_date):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == sort_date


