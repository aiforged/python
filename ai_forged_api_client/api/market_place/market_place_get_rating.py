from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/MarketPlace/GetRating".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "stpdId": stpd_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Optional[float]]:
    if response.status_code == 200:
        response_200 = cast(Optional[float], response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Optional[float]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Optional[float]]:
    """Get service rating

    Args:
        stpd_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Optional[float]]
    """

    kwargs = _get_kwargs(
        client=client,
        stpd_id=stpd_id,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[Optional[float]]:
    """Get service rating

    Args:
        stpd_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Optional[float]]
    """

    return sync_detailed(
        client=client,
        stpd_id=stpd_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Optional[float]]:
    """Get service rating

    Args:
        stpd_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Optional[float]]
    """

    kwargs = _get_kwargs(
        client=client,
        stpd_id=stpd_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[Optional[float]]:
    """Get service rating

    Args:
        stpd_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Optional[float]]
    """

    return (
        await asyncio_detailed(
            client=client,
            stpd_id=stpd_id,
            x_api_version=x_api_version,
        )
    ).parsed
