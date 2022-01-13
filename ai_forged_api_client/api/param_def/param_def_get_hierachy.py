from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    include_count: Union[Unset, None, bool] = False,
    include_settings: Union[Unset, None, bool] = True,
    include_children: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/ParamDef/GetHierachy".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "projectId": project_id,
        "stpdId": stpd_id,
        "includeCount": include_count,
        "includeSettings": include_settings,
        "includeChildren": include_children,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    include_count: Union[Unset, None, bool] = False,
    include_settings: Union[Unset, None, bool] = True,
    include_children: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get hierarchy of fields for a service

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        include_count (Union[Unset, None, bool]):
        include_settings (Union[Unset, None, bool]):  Default: True.
        include_children (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        include_count=include_count,
        include_settings=include_settings,
        include_children=include_children,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    include_count: Union[Unset, None, bool] = False,
    include_settings: Union[Unset, None, bool] = True,
    include_children: Union[Unset, None, bool] = False,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get hierarchy of fields for a service

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        include_count (Union[Unset, None, bool]):
        include_settings (Union[Unset, None, bool]):  Default: True.
        include_children (Union[Unset, None, bool]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        include_count=include_count,
        include_settings=include_settings,
        include_children=include_children,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
