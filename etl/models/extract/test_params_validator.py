import pytest
from unittest.mock import patch
from etl.models.extract.params_validator import ParamsValidator


@pytest.fixture
def valid_params() -> list:
    return ["BRL-COP", "BRL-PEN"]


@pytest.fixture
def invalid_params() -> list:
    return ["param1", "param2"]


@pytest.fixture
def mixed_params():
    return ["BRL-COP", "BRL-PEN", "param1", "param2"]


@patch("etl.models.extract.params_validator.ClientBuilder")
def test_valid_params(mock_client_builder, valid_params):  # pylint: disable=redefined-outer-name
    mock_client_builder.return_value.get_api_data.return_value = valid_params
    valid = ParamsValidator.valid_params_for_call(valid_params)
    assert valid_params == valid


@patch("etl.models.extract.params_validator.ClientBuilder")
def test_invalid_params(mock_client_builder, invalid_params):  # pylint: disable=redefined-outer-name
    mock_client_builder.return_value.get_api_data.return_value = []
    with pytest.raises(KeyError):
        ParamsValidator.valid_params_for_call(invalid_params)


@patch("etl.models.extract.params_validator.ClientBuilder")
def test_mixed_params(
    mock_client_builder,
    mixed_params, valid_params
):  # pylint: disable=redefined-outer-name
    mock_client_builder.return_value.get_api_data.return_value = valid_params
    validated = ParamsValidator.valid_params_for_call(mixed_params)
    assert validated == valid_params
