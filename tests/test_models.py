import pytest
from core.models import Cases


@pytest.mark.django_db
def test_cases():
    Cases.objects.create(confirmed=500, recovered=200, country='Nigeria')
    assert Cases.objects.count() == 1