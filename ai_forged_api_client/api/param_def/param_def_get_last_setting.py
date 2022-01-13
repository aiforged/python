from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_models_parameter_def_setting_view_model import (
    AIForgedDALModelsParameterDefSettingViewModel,
)
from ...models.ai_forged_dal_setting_type import AIForgedDALSettingType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pd_id: Union[Unset, None, int] = UNSET,
    type: Union[AIForgedDALSettingType, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/ParamDef/GetLastSetting".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_type: Union[None, Unset, int]
    if isinstance(type, Unset):
        json_type = UNSET
    elif type is None:
        json_type = None
    else:
        json_type = UNSET
        if not isinstance(type, Unset):
            json_type = type.value if type else None

    params: Dict[str, Any] = {
        "pdId": pd_id,
        "type": json_type,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedDALModelsParameterDefSettingViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedDALModelsParameterDefSettingViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedDALModelsParameterDefSettingViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pd_id: Union[Unset, None, int] = UNSET,
    type: Union[AIForgedDALSettingType, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedDALModelsParameterDefSettingViewModel]:
    """Get last setting for a definition

    Args:
        pd_id (Union[Unset, None, int]):
        type (Union[AIForgedDALSettingType, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedDALModelsParameterDefSettingViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        pd_id=pd_id,
        type=type,
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
    pd_id: Union[Unset, None, int] = UNSET,
    type: Union[AIForgedDALSettingType, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedDALModelsParameterDefSettingViewModel]:
    """Get last setting for a definition

    Args:
        pd_id (Union[Unset, None, int]):
        type (Union[AIForgedDALSettingType, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedDALModelsParameterDefSettingViewModel]
    """

    return sync_detailed(
        client=client,
        pd_id=pd_id,
        type=type,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pd_id: Union[Unset, None, int] = UNSET,
    type: Union[AIForgedDALSettingType, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedDALModelsParameterDefSettingViewModel]:
    """Get last setting for a definition

    Args:
        pd_id (Union[Unset, None, int]):
        type (Union[AIForgedDALSettingType, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedDALModelsParameterDefSettingViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        pd_id=pd_id,
        type=type,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pd_id: Union[Unset, None, int] = UNSET,
    type: Union[AIForgedDALSettingType, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedDALModelsParameterDefSettingViewModel]:
    """Get last setting for a definition

    Args:
        pd_id (Union[Unset, None, int]):
        type (Union[AIForgedDALSettingType, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedDALModelsParameterDefSettingViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            pd_id=pd_id,
            type=type,
            x_api_version=x_api_version,
        )
    ).parsed
