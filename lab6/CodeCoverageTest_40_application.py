
from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


# Tests for extra_distance_fare()

def test_unknown_cab_type():
    try:
        extra_distance_fare("bike", 10, "city", False)
        assert False
    except ValueError:
        assert True


def test_negative_distance():
    try:
        extra_distance_fare("mini", -1, "city", False)
        assert False
    except ValueError:
        assert True


def test_within_included_distance():
    assert extra_distance_fare("sedan", 5, "city", False) == 0


def test_subscriber_included_distance():
    assert extra_distance_fare("mini", 7, "city", True) == 0


def test_suv_subscriber():
    assert extra_distance_fare("suv", 13, "city", True) == 12


def test_city_fare():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_non_city_fare():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_long_distance_city():
    assert extra_distance_fare("mini", 30, "city", False) == 500


def test_long_distance_outstation():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750


# Tests for seats_and_bags_ok()

def test_wheelchair_allowed():
    assert seats_and_bags_ok(2, 3, True) is True


def test_wheelchair_exceeds_limit():
    assert seats_and_bags_ok(3, 1, True) is False


def test_passengers_exceed_limit():
    assert seats_and_bags_ok(5, 1, False) is False


def test_bags_exceed_limit():
    assert seats_and_bags_ok(3, 3, False) is False


def test_valid_seats_and_bags():
    assert seats_and_bags_ok(4, 2, False) is True


# Tests for pickup_status()

def test_scheduled_on_time():
    assert pickup_status(10, True, False) == "on_time"


def test_unscheduled_on_time():
    assert pickup_status(5, False, False) == "on_time"


def test_airport_on_time():
    assert pickup_status(15, False, True) == "on_time"


def test_delayed_pickup():
    assert pickup_status(0, False, False) == "delayed"


def test_missed_pickup():
    assert pickup_status(-11, False, False) == "missed"
