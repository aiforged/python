from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.microsoft_power_bi_api_models_group_user import MicrosoftPowerBIApiModelsGroupUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    groupid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Reports/GetGroupUsers".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "groupid": groupid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[MicrosoftPowerBIApiModelsGroupUser]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MicrosoftPowerBIApiModelsGroupUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[MicrosoftPowerBIApiModelsGroupUser]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    groupid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[MicrosoftPowerBIApiModelsGroupUser]]:
    """Get goup users

    Args:
        groupid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[MicrosoftPowerBIApiModelsGroupUser]]
    """

    kwargs = _get_kwargs(
        client=client,
        groupid=groupid,
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
    groupid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[MicrosoftPowerBIApiModelsGroupUser]]:
    """Get goup users

    Args:
        groupid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[MicrosoftPowerBIApiModelsGroupUser]]
    """

    return sync_detailed(
        client=client,
        groupid=groupid,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    groupid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[MicrosoftPowerBIApiModelsGroupUser]]:
    """Get goup users

    Args:
        groupid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[MicrosoftPowerBIApiModelsGroupUser]]
    """

    kwargs = _get_kwargs(
        client=client,
        groupid=groupid,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    groupid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[MicrosoftPowerBIApiModelsGroupUser]]:
    """Get goup users

    Args:
        groupid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[MicrosoftPowerBIApiModelsGroupUser]]
    """

    return (
        await asyncio_detailed(
            client=client,
            groupid=groupid,
            x_api_version=x_api_version,
        )
    ).parsed
