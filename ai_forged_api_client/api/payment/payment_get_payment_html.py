from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    u_id: Union[Unset, None, str] = UNSET,
    p_id: Union[Unset, None, int] = UNSET,
    b_id: Union[Unset, None, int] = UNSET,
    intent: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Payment/GetPaymentHtml".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "uId": u_id,
        "pId": p_id,
        "bId": b_id,
        "intent": intent,
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
    u_id: Union[Unset, None, str] = UNSET,
    p_id: Union[Unset, None, int] = UNSET,
    b_id: Union[Unset, None, int] = UNSET,
    intent: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """Get paymetnhtml for credit card processing

    Args:
        u_id (Union[Unset, None, str]):
        p_id (Union[Unset, None, int]):
        b_id (Union[Unset, None, int]):
        intent (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        u_id=u_id,
        p_id=p_id,
        b_id=b_id,
        intent=intent,
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
    u_id: Union[Unset, None, str] = UNSET,
    p_id: Union[Unset, None, int] = UNSET,
    b_id: Union[Unset, None, int] = UNSET,
    intent: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """Get paymetnhtml for credit card processing

    Args:
        u_id (Union[Unset, None, str]):
        p_id (Union[Unset, None, int]):
        b_id (Union[Unset, None, int]):
        intent (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    return sync_detailed(
        client=client,
        u_id=u_id,
        p_id=p_id,
        b_id=b_id,
        intent=intent,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    u_id: Union[Unset, None, str] = UNSET,
    p_id: Union[Unset, None, int] = UNSET,
    b_id: Union[Unset, None, int] = UNSET,
    intent: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """Get paymetnhtml for credit card processing

    Args:
        u_id (Union[Unset, None, str]):
        p_id (Union[Unset, None, int]):
        b_id (Union[Unset, None, int]):
        intent (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        client=client,
        u_id=u_id,
        p_id=p_id,
        b_id=b_id,
        intent=intent,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    u_id: Union[Unset, None, str] = UNSET,
    p_id: Union[Unset, None, int] = UNSET,
    b_id: Union[Unset, None, int] = UNSET,
    intent: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """Get paymetnhtml for credit card processing

    Args:
        u_id (Union[Unset, None, str]):
        p_id (Union[Unset, None, int]):
        b_id (Union[Unset, None, int]):
        intent (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[File]
    """

    return (
        await asyncio_detailed(
            client=client,
            u_id=u_id,
            p_id=p_id,
            b_id=b_id,
            intent=intent,
            x_api_version=x_api_version,
        )
    ).parsed
