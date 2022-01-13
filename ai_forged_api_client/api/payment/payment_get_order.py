from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: str,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Payment/GetOrder".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_json_body = json_body

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: str,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """Get info on an order

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (str):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: str,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """Get info on an order

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (str):

    Returns:
        Response[File]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: str,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """Get info on an order

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (str):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: str,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """Get info on an order

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (str):

    Returns:
        Response[File]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_api_version=x_api_version,
        )
    ).parsed
