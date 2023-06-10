import freezegun
import datetime

@freezegun.freeze_time('2024, 1, 1')
def test_something():
    asser datetime.now() == datetime.datetime(2024, 1, 1)

test_something()
