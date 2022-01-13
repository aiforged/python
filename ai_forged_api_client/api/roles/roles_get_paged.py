from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_role_view_model import AIForgedViewModelsRoleViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = -1,
    page_size: Union[Unset, None, int] = -1,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Roles/GetPaged".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "page": page,
        "pageSize": page_size,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsRoleViewModel]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsRoleViewModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsRoleViewModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = -1,
    page_size: Union[Unset, None, int] = -1,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsRoleViewModel]]:
    """Get roles by pages

    Args:
        page (Union[Unset, None, int]):  Default: -1.
        page_size (Union[Unset, None, int]):  Default: -1.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsRoleViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
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
    page: Union[Unset, None, int] = -1,
    page_size: Union[Unset, None, int] = -1,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsRoleViewModel]]:
    """Get roles by pages

    Args:
        page (Union[Unset, None, int]):  Default: -1.
        page_size (Union[Unset, None, int]):  Default: -1.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsRoleViewModel]]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = -1,
    page_size: Union[Unset, None, int] = -1,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsRoleViewModel]]:
    """Get roles by pages

    Args:
        page (Union[Unset, None, int]):  Default: -1.
        page_size (Union[Unset, None, int]):  Default: -1.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsRoleViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = -1,
    page_size: Union[Unset, None, int] = -1,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsRoleViewModel]]:
    """Get roles by pages

    Args:
        page (Union[Unset, None, int]):  Default: -1.
        page_size (Union[Unset, None, int]):  Default: -1.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsRoleViewModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            x_api_version=x_api_version,
        )
    ).parsed
