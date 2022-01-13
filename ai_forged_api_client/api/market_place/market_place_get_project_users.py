from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_link_type import AIForgedDALLinkType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALLinkType, None, Unset] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/MarketPlace/GetProjectUsers".format(client.base_url)

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
        "projectId": project_id,
        "role": role,
        "type": json_type,
        "groupId": group_id,
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
    project_id: Union[Unset, None, int] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALLinkType, None, Unset] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        project_id (Union[Unset, None, int]):
        role (Union[Unset, None, str]):
        type (Union[AIForgedDALLinkType, None, Unset]):
        group_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        role=role,
        type=type,
        group_id=group_id,
        x_api_version=x_api_version,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALLinkType, None, Unset] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        project_id (Union[Unset, None, int]):
        role (Union[Unset, None, str]):
        type (Union[AIForgedDALLinkType, None, Unset]):
        group_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        role=role,
        type=type,
        group_id=group_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
