import pytest
from dnareport.core.allele import Allele
from dnareport.core.errors import AlleleDataTypeError


def test_allele_from_string():
    allele = Allele('18')
    assert allele.value == '18'


def test_allele_from_int():
    with pytest.raises(AlleleDataTypeError):
        Allele(18)
