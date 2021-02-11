"""Tests for overall app"""


def test_db(db):
    assert db.session.scalar("SELECT 1")
