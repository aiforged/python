from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_project_user_status import AIForgedDALProjectUserStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    req_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALProjectUserStatus] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/MarketPlace/ApproveRequest".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_status: Union[Unset, None, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params: Dict[str, Any] = {
        "reqId": req_id,
        "status": json_status,
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
    req_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALProjectUserStatus] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Approve a user request

    Args:
        req_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALProjectUserStatus]): Status for project user link
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        req_id=req_id,
        status=status,
        x_api_version=x_api_version,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    req_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALProjectUserStatus] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Approve a user request

    Args:
        req_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALProjectUserStatus]): Status for project user link
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        req_id=req_id,
        status=status,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)
