from src.entity.champion import Champion


def check_champion_vars(expected: Champion, actual: Champion) -> list:
    """
    compare and check different fields
    :param expected: want to compare champion
    :param actual: want to compare champion
    :return: Two dimensional list. Those format is [[fieldname, expected value, actual value], ...]
     e.g. [[attack_damage, 2, 3], [armor, 30, 40]]
    """
    expected_fields = vars(expected)
    actual_fields = vars(actual)
    return [[key, expected_fields[key], actual_fields[key]] for (key, value) in expected_fields.items() \
            if vars(expected)[key] != actual_fields[key]]


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Champion) and isinstance(right, Champion) \
     and op == '==':
        assert_message = [str(x) for x in check_champion_vars(left, right)]
        assert_message.insert(0, 'comparing Champion instance [fieldname, expected, actual]')
        return assert_message
