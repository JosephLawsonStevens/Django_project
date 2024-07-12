import pytest

from djangoproj.models import Student


@pytest.mark.django_db
def test_get_students():
    assert Student.objects.count() == 3

