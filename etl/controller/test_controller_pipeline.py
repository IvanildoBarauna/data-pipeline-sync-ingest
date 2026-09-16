import pytest
from unittest.mock import patch

from etl.controller.pipeline import PipelineExecutor


@patch("etl.controller.pipeline.DatasetSerializer.serialize")
@patch("etl.controller.pipeline.ResponseTransformation")
@patch("etl.controller.pipeline.APIExtraction.run")
def test_pipelines_params_with_two_param(
    mock_extraction, _mock_transformer, _mock_serializer
):
    expected_result = ["USD-BRL", "USD-BRLT"]
    mock_extraction.return_value = ({}, expected_result)
    new_executor = PipelineExecutor("USD-BRL", "USD-BRLT")
    result = new_executor.pipeline_run()
    assert result == expected_result


@patch("etl.controller.pipeline.DatasetSerializer.serialize")
@patch("etl.controller.pipeline.ResponseTransformation")
@patch("etl.controller.pipeline.APIExtraction.run")
def test_pipelines_params_with_two_param_and_one_invalid(
    mock_extraction, _mock_transformer, _mock_serializer
):
    expected_result = ["USD-BRL", "USD-BRLT"]
    mock_extraction.return_value = ({}, expected_result)
    new_executor = PipelineExecutor("USD-BRL", "USD-BRLT", "invalid_param")
    result = new_executor.pipeline_run()
    assert result == expected_result


def test_pipelines_params_with_all_invalid_params():
    with pytest.raises(TypeError):
        new_executor = PipelineExecutor(1, 1, 1)
        new_executor.pipeline_run()


@patch("etl.controller.pipeline.APIExtraction.run")
def test_pipelines_params_with_all_invalid_keys_params(mock_extraction):
    mock_extraction.side_effect = KeyError("Invalid parameters")
    with pytest.raises(KeyError):
        validator = PipelineExecutor("INVALID-QUOTE", "INVALID-QUOTE2")
        validator.pipeline_run()
