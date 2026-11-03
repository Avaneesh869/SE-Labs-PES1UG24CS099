
import pytest
from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


# extra_distance_fare() tests

def test_unknown_cab_type():
    with pytest.raises(ValueError, match="unknown cab type"):
        extra_distance_fare("bike", 10, "city", False)


def test_negative_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        extra_distance_fare("mini", -1, "city", False)


def test_subscriber_non_suv():
    assert extra_distance_fare("mini", 10, "city", True) == 24


def test_non_subscriber():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_subscriber_suv_excluded_from_extra_km():
    assert extra_distance_fare("suv", 15, "city", True) == 36


def test_distance_at_included_limit():
    assert extra_distance_fare("mini", 5, "city", False) == 0


def test_distance_below_included_limit():
    assert extra_distance_fare("sedan", 7, "city", False) == 0


def test_city_rate():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_non_city_rate():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_extra_distance_exactly_twenty():
    assert extra_distance_fare("mini", 25, "city", False) == 240


def test_extra_distance_above_twenty_city():
    assert extra_distance_fare("mini", 26, "city", False) == 420


def test_extra_distance_above_twenty_outstation():
    assert extra_distance_fare("mini", 26, "outstation", False) == 630


# seats_and_bags_ok() tests

def test_wheelchair_true_within_limit():
    assert seats_and_bags_ok(2, 5, True) is True


def test_wheelchair_true_over_limit():
    assert seats_and_bags_ok(3, 1, True) is False


def test_wheelchair_false_passenger_limit_exceeded():
    assert seats_and_bags_ok(5, 1, False) is False


def test_wheelchair_false_passenger_limit_not_exceeded():
    assert seats_and_bags_ok(4, 2, False) is True


def test_wheelchair_false_bags_exceeded():
    assert seats_and_bags_ok(3, 3, False) is False


# pickup_status() tests

def test_scheduled_on_time():
    assert pickup_status(10, True, False) == "on_time"


def test_unscheduled_on_time():
    assert pickup_status(5, False, False) == "on_time"


def test_airport_cutoff_on_time():
    assert pickup_status(15, False, True) == "on_time"


def test_delayed_pickup():
    assert pickup_status(0, False, False) == "delayed"


def test_missed_pickup():
    assert pickup_status(-11, False, False) == "missed"
