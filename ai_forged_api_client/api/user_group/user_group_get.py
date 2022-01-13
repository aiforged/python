from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_user_group_view_model import AIForgedViewModelsUserGroupViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/UserGroup/Get".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "id": id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsUserGroupViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsUserGroupViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsUserGroupViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsUserGroupViewModel]:
    """Get by id

    Args:
        id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserGroupViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
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
    id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsUserGroupViewModel]:
    """Get by id

    Args:
        id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserGroupViewModel]
    """

    return sync_detailed(
        client=client,
        id=id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsUserGroupViewModel]:
    """Get by id

    Args:
        id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserGroupViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsUserGroupViewModel]:
    """Get by id

    Args:
        id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsUserGroupViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            x_api_version=x_api_version,
        )
    ).parsed