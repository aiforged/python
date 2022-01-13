from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.system_get_system_info_response_200 import SystemGetSystemInfoResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/System/GetSystemInfo".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SystemGetSystemInfoResponse200]:
    if response.status_code == 200:
        response_200 = SystemGetSystemInfoResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SystemGetSystemInfoResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[SystemGetSystemInfoResponse200]:
    """Get system and application information

    Args:
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[SystemGetSystemInfoResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
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
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[SystemGetSystemInfoResponse200]:
    """Get system and application information

    Args:
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[SystemGetSystemInfoResponse200]
    """

    return sync_detailed(
        client=client,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[SystemGetSystemInfoResponse200]:
    """Get system and application information

    Args:
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[SystemGetSystemInfoResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[SystemGetSystemInfoResponse200]:
    """Get system and application information

    Args:
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[SystemGetSystemInfoResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_api_version=x_api_version,
        )
    ).parsed
