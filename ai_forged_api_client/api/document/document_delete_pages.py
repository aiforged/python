from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_operation_option import AIForgedDALOperationOption
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...models.ai_forged_view_models_document_data_view_model import AIForgedViewModelsDocumentDataViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: List[int],
    id: Union[Unset, None, int] = UNSET,
    child_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    child_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    child_delete_options: Union[Unset, None, AIForgedDALOperationOption] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/DeletePages".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_child_usage: Union[Unset, None, int] = UNSET
    if not isinstance(child_usage, Unset):
        json_child_usage = child_usage.value if child_usage else None

    json_child_status: Union[Unset, None, int] = UNSET
    if not isinstance(child_status, Unset):
        json_child_status = child_status.value if child_status else None

    json_child_delete_options: Union[Unset, None, int] = UNSET
    if not isinstance(child_delete_options, Unset):
        json_child_delete_options = child_delete_options.value if child_delete_options else None

    params: Dict[str, Any] = {
        "id": id,
        "childUsage": json_child_usage,
        "childStatus": json_child_status,
        "childDeleteOptions": json_child_delete_options,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsDocumentDataViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsDocumentDataViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsDocumentDataViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[int],
    id: Union[Unset, None, int] = UNSET,
    child_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    child_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    child_delete_options: Union[Unset, None, AIForgedDALOperationOption] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsDocumentDataViewModel]:
    """Delete pages from a document

    Args:
        id (Union[Unset, None, int]):
        child_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        child_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        child_delete_options (Union[Unset, None, AIForgedDALOperationOption]): API operation
            option
        x_api_version (Union[Unset, None, str]):
        json_body (List[int]):

    Returns:
        Response[AIForgedViewModelsDocumentDataViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        id=id,
        child_usage=child_usage,
        child_status=child_status,
        child_delete_options=child_delete_options,
        x_api_version=x_api_version,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: List[int],
    id: Union[Unset, None, int] = UNSET,
    child_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    child_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    child_delete_options: Union[Unset, None, AIForgedDALOperationOption] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsDocumentDataViewModel]:
    """Delete pages from a document

    Args:
        id (Union[Unset, None, int]):
        child_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        child_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        child_delete_options (Union[Unset, None, AIForgedDALOperationOption]): API operation
            option
        x_api_version (Union[Unset, None, str]):
        json_body (List[int]):

    Returns:
        Response[AIForgedViewModelsDocumentDataViewModel]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        id=id,
        child_usage=child_usage,
        child_status=child_status,
        child_delete_options=child_delete_options,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[int],
    id: Union[Unset, None, int] = UNSET,
    child_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    child_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    child_delete_options: Union[Unset, None, AIForgedDALOperationOption] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsDocumentDataViewModel]:
    """Delete pages from a document

    Args:
        id (Union[Unset, None, int]):
        child_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        child_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        child_delete_options (Union[Unset, None, AIForgedDALOperationOption]): API operation
            option
        x_api_version (Union[Unset, None, str]):
        json_body (List[int]):

    Returns:
        Response[AIForgedViewModelsDocumentDataViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        id=id,
        child_usage=child_usage,
        child_status=child_status,
        child_delete_options=child_delete_options,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: List[int],
    id: Union[Unset, None, int] = UNSET,
    child_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    child_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    child_delete_options: Union[Unset, None, AIForgedDALOperationOption] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsDocumentDataViewModel]:
    """Delete pages from a document

    Args:
        id (Union[Unset, None, int]):
        child_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        child_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        child_delete_options (Union[Unset, None, AIForgedDALOperationOption]): API operation
            option
        x_api_version (Union[Unset, None, str]):
        json_body (List[int]):

    Returns:
        Response[AIForgedViewModelsDocumentDataViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            id=id,
            child_usage=child_usage,
            child_status=child_status,
            child_delete_options=child_delete_options,
            x_api_version=x_api_version,
        )
    ).parsed
