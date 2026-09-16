from unittest.mock import patch

from etl.models.extract.api_data_extractor import APIExtraction


@patch("etl.models.extract.api_data_extractor.ClientBuilder")
@patch("etl.models.extract.api_data_extractor.ParamsValidator.valid_params_for_call")
def test_extraction_constructor(mock_valid_params, mock_client_builder):
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    expected_response = {"USDBRL": {"bid": "5.0"}}
    mock_valid_params.return_value = params
    mock_client_builder.return_value.get_api_data.return_value = expected_response

    extractor = APIExtraction.run(params)

    assert extractor[1] == params
    assert extractor[0] == expected_response
