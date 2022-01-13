from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_data_type import AIForgedDALDocumentDataType
from ...models.ai_forged_view_models_document_data_view_model import AIForgedViewModelsDocumentDataViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    blobid: Union[Unset, None, int] = UNSET,
    pageindex: Union[Unset, None, int] = UNSET,
    images_count: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/GetData".format(client.base_url)

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
        "Id": id,
        "types": json_types,
        "contentType": content_type,
        "text": text,
        "blobid": blobid,
        "pageindex": pageindex,
        "imagesCount": images_count,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsDocumentDataViewModel]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsDocumentDataViewModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsDocumentDataViewModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    blobid: Union[Unset, None, int] = UNSET,
    pageindex: Union[Unset, None, int] = UNSET,
    images_count: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsDocumentDataViewModel]]:
    """Get document images

    Args:
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        content_type (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        blobid (Union[Unset, None, int]):
        pageindex (Union[Unset, None, int]):
        images_count (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentDataViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        types=types,
        content_type=content_type,
        text=text,
        blobid=blobid,
        pageindex=pageindex,
        images_count=images_count,
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
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    blobid: Union[Unset, None, int] = UNSET,
    pageindex: Union[Unset, None, int] = UNSET,
    images_count: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsDocumentDataViewModel]]:
    """Get document images

    Args:
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        content_type (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        blobid (Union[Unset, None, int]):
        pageindex (Union[Unset, None, int]):
        images_count (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentDataViewModel]]
    """

    return sync_detailed(
        client=client,
        id=id,
        types=types,
        content_type=content_type,
        text=text,
        blobid=blobid,
        pageindex=pageindex,
        images_count=images_count,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    blobid: Union[Unset, None, int] = UNSET,
    pageindex: Union[Unset, None, int] = UNSET,
    images_count: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsDocumentDataViewModel]]:
    """Get document images

    Args:
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        content_type (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        blobid (Union[Unset, None, int]):
        pageindex (Union[Unset, None, int]):
        images_count (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentDataViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        types=types,
        content_type=content_type,
        text=text,
        blobid=blobid,
        pageindex=pageindex,
        images_count=images_count,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    types: Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    blobid: Union[Unset, None, int] = UNSET,
    pageindex: Union[Unset, None, int] = UNSET,
    images_count: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsDocumentDataViewModel]]:
    """Get document images

    Args:
        id (Union[Unset, None, int]):
        types (Union[Unset, None, List[Optional[AIForgedDALDocumentDataType]]]):
        content_type (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        blobid (Union[Unset, None, int]):
        pageindex (Union[Unset, None, int]):
        images_count (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentDataViewModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            types=types,
            content_type=content_type,
            text=text,
            blobid=blobid,
            pageindex=pageindex,
            images_count=images_count,
            x_api_version=x_api_version,
        )
    ).parsed
