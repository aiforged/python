from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_custom_data_set_record import AIForgedViewModelsCustomDataSetRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    key_value: Union[Unset, None, str] = UNSET,
    include_verifications: Union[Unset, None, bool] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/DataSet/GetRecordByKeyValue".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "docId": doc_id,
        "defId": def_id,
        "keyValue": key_value,
        "includeVerifications": include_verifications,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsCustomDataSetRecord]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsCustomDataSetRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsCustomDataSetRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    key_value: Union[Unset, None, str] = UNSET,
    include_verifications: Union[Unset, None, bool] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsCustomDataSetRecord]:
    """Find a custom dataset by key

    Args:
        doc_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        key_value (Union[Unset, None, str]):
        include_verifications (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsCustomDataSetRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        def_id=def_id,
        key_value=key_value,
        include_verifications=include_verifications,
        x_api_version=x_api_version,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    key_value: Union[Unset, None, str] = UNSET,
    include_verifications: Union[Unset, None, bool] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsCustomDataSetRecord]:
    """Find a custom dataset by key

    Args:
        doc_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        key_value (Union[Unset, None, str]):
        include_verifications (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsCustomDataSetRecord]
    """

    return sync_detailed(
        client=client,
        doc_id=doc_id,
        def_id=def_id,
        key_value=key_value,
        include_verifications=include_verifications,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    key_value: Union[Unset, None, str] = UNSET,
    include_verifications: Union[Unset, None, bool] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsCustomDataSetRecord]:
    """Find a custom dataset by key

    Args:
        doc_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        key_value (Union[Unset, None, str]):
        include_verifications (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsCustomDataSetRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        def_id=def_id,
        key_value=key_value,
        include_verifications=include_verifications,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    key_value: Union[Unset, None, str] = UNSET,
    include_verifications: Union[Unset, None, bool] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsCustomDataSetRecord]:
    """Find a custom dataset by key

    Args:
        doc_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        key_value (Union[Unset, None, str]):
        include_verifications (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsCustomDataSetRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            doc_id=doc_id,
            def_id=def_id,
            key_value=key_value,
            include_verifications=include_verifications,
            x_api_version=x_api_version,
        )
    ).parsed
