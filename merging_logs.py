log1 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
    {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
]

log2 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
    {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
]


def merge_logs(log1: list, log2: list) -> list:
    """
    Function to merge logs (received from two lists), deletes duplicates (compared by id's of records) and sort result (by datetime timestamp).

    :param log1: first list of records
    :param log2: second list of records

    :return: list of merged records
    """
    for record1 in log1:
        for record2 in log2:
            if record2['id'] == record1['id']:
                log2.remove(record2)
    return sorted(log1 + log2, key=lambda d: d['datetime'])


print(merge_logs(log1, log2))