from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.microsoft_asp_net_core_identity_user_login_info import MicrosoftAspNetCoreIdentityUserLoginInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: MicrosoftAspNetCoreIdentityUserLoginInfo,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Account/DeleteUserLoginProvider".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "userId": user_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    if response.status_code == 200:
        response_200 = MicrosoftAspNetCoreIdentityUserLoginInfo.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: MicrosoftAspNetCoreIdentityUserLoginInfo,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    """Get list of current user login providers

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (MicrosoftAspNetCoreIdentityUserLoginInfo):

    Returns:
        Response[MicrosoftAspNetCoreIdentityUserLoginInfo]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: MicrosoftAspNetCoreIdentityUserLoginInfo,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    """Get list of current user login providers

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (MicrosoftAspNetCoreIdentityUserLoginInfo):

    Returns:
        Response[MicrosoftAspNetCoreIdentityUserLoginInfo]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: MicrosoftAspNetCoreIdentityUserLoginInfo,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    """Get list of current user login providers

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (MicrosoftAspNetCoreIdentityUserLoginInfo):

    Returns:
        Response[MicrosoftAspNetCoreIdentityUserLoginInfo]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: MicrosoftAspNetCoreIdentityUserLoginInfo,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[MicrosoftAspNetCoreIdentityUserLoginInfo]:
    """Get list of current user login providers

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (MicrosoftAspNetCoreIdentityUserLoginInfo):

    Returns:
        Response[MicrosoftAspNetCoreIdentityUserLoginInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
