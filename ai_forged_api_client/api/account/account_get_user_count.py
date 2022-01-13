from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Account/GetUserCount".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "filter": filter_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[int]:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[int]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Get count of users

    Args:
        filter_ (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
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
    filter_: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Get count of users

    Args:
        filter_ (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Get count of users

    Args:
        filter_ (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Get count of users

    Args:
        filter_ (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            x_api_version=x_api_version,
        )
    ).parsed
