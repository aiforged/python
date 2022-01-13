from typing import Any, Dict, List, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/DeleteMulti".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(ids, Unset):
        if ids is None:
            json_ids = None
        else:
            json_ids = ids

    params: Dict[str, Any] = {
        "Ids": json_ids,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Delete multiple documents

    Args:
        ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        ids=ids,
        x_api_version=x_api_version,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Delete multiple documents

    Args:
        ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        ids=ids,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
