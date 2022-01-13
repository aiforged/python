from io import BytesIO
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_data_type import AIForgedDALDocumentDataType
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/GetBlob".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_types: Union[Unset, None, List[Optional[int]]] = UNSET
    if not isinstance(types, Unset):
        if types is None:
            json_types = None
        else:
            json_types = []
            for types_item_data in types:
                types_item = types_item_data.value if types_item_data else None

                json_types.append(types_item)

    params: Dict[str, Any] = {
        "userId": user_id,
        "Id": id,
        "types": json_types,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        user_id (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        id=id,
        types=types,
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
    user_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        user_id (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        id=id,
        types=types,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        user_id (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        id=id,
        types=types,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        user_id (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            id=id,
            types=types,
            x_api_version=x_api_version,
        )
    ).parsed
