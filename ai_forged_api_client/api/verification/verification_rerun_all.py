from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    restart: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Verification/RerunAll".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "docId": doc_id,
        "restart": restart,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[bool]:
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
    restart: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Rerun verification on a document

     This will also run custom code

    Args:
        doc_id (Union[Unset, None, int]):
        restart (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        restart=restart,
        x_api_version=x_api_version,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    restart: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Rerun verification on a document

     This will also run custom code

    Args:
        doc_id (Union[Unset, None, int]):
        restart (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return sync_detailed(
        client=client,
        doc_id=doc_id,
        restart=restart,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    restart: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Rerun verification on a document

     This will also run custom code

    Args:
        doc_id (Union[Unset, None, int]):
        restart (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        restart=restart,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    restart: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Rerun verification on a document

     This will also run custom code

    Args:
        doc_id (Union[Unset, None, int]):
        restart (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return (
        await asyncio_detailed(
            client=client,
            doc_id=doc_id,
            restart=restart,
            x_api_version=x_api_version,
        )
    ).parsed
