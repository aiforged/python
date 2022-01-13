from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_value_type import AIForgedDALValueType
from ...models.ai_forged_view_models_data_type_view_model import AIForgedViewModelsDataTypeViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, AIForgedDALValueType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/System/DeleteDataType".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_id: Union[Unset, None, int] = UNSET
    if not isinstance(id, Unset):
        json_id = id.value if id else None

    params: Dict[str, Any] = {
        "id": json_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsDataTypeViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsDataTypeViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsDataTypeViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, AIForgedDALValueType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsDataTypeViewModel]:
    """Delete a datatype

    Args:
        id (Union[Unset, None, AIForgedDALValueType]): The type of values used for rules and
            settings
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsDataTypeViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
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
    id: Union[Unset, None, AIForgedDALValueType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsDataTypeViewModel]:
    """Delete a datatype

    Args:
        id (Union[Unset, None, AIForgedDALValueType]): The type of values used for rules and
            settings
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsDataTypeViewModel]
    """

    return sync_detailed(
        client=client,
        id=id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, AIForgedDALValueType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsDataTypeViewModel]:
    """Delete a datatype

    Args:
        id (Union[Unset, None, AIForgedDALValueType]): The type of values used for rules and
            settings
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsDataTypeViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, AIForgedDALValueType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsDataTypeViewModel]:
    """Delete a datatype

    Args:
        id (Union[Unset, None, AIForgedDALValueType]): The type of values used for rules and
            settings
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsDataTypeViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            x_api_version=x_api_version,
        )
    ).parsed
