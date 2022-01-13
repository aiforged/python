from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    to_project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Services/Move".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "stpdId": stpd_id,
        "toProjectId": to_project_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[bool]:
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
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    to_project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Move a service to another project

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        to_project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        to_project_id=to_project_id,
        x_api_version=x_api_version,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    to_project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Move a service to another project

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        to_project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        to_project_id=to_project_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    to_project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Move a service to another project

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        to_project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        to_project_id=to_project_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    to_project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Move a service to another project

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        to_project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            project_id=project_id,
            stpd_id=stpd_id,
            to_project_id=to_project_id,
            x_api_version=x_api_version,
        )
    ).parsed
