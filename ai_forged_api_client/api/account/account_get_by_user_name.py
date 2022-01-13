from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_user_view_model import AIForgedViewModelsUserViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_name: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Account/GetByUserName".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "userName": user_name,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsUserViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsUserViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsUserViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    user_name: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsUserViewModel]:
    """Get user info by username

    Args:
        user_name (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        user_name=user_name,
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
    user_name: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsUserViewModel]:
    """Get user info by username

    Args:
        user_name (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserViewModel]
    """

    return sync_detailed(
        client=client,
        user_name=user_name,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_name: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsUserViewModel]:
    """Get user info by username

    Args:
        user_name (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        user_name=user_name,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_name: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsUserViewModel]:
    """Get user info by username

    Args:
        user_name (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_name=user_name,
            x_api_version=x_api_version,
        )
    ).parsed
