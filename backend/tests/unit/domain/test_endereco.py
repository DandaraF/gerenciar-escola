from unittest import TestCase

from tests.unit.domain.util import general_roundtrip
from tests.unit.mocks import endereco_mock


class TestEndereco(TestCase):
    def test_endereco_roundtrip(self):
        mock_endereco = endereco_mock()

        self.assertEqual(mock_endereco, general_roundtrip(mock_endereco))
