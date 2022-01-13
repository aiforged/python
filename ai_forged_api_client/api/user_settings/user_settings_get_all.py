from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_setting_view_model import AIForgedViewModelsSettingViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    only_key_values: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/UserSettings/GetAll".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "userId": user_id,
        "key": key,
        "onlyKeyValues": only_key_values,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsSettingViewModel]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsSettingViewModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsSettingViewModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    only_key_values: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsSettingViewModel]]:
    """Get user settings

    Args:
        user_id (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        only_key_values (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsSettingViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        key=key,
        only_key_values=only_key_values,
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
    user_id: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    only_key_values: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsSettingViewModel]]:
    """Get user settings

    Args:
        user_id (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        only_key_values (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsSettingViewModel]]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        key=key,
        only_key_values=only_key_values,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    only_key_values: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsSettingViewModel]]:
    """Get user settings

    Args:
        user_id (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        only_key_values (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsSettingViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        key=key,
        only_key_values=only_key_values,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    only_key_values: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsSettingViewModel]]:
    """Get user settings

    Args:
        user_id (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        only_key_values (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsSettingViewModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            key=key,
            only_key_values=only_key_values,
            x_api_version=x_api_version,
        )
    ).parsed
