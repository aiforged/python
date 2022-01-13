from typing import Any, Dict, List, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_link_type import AIForgedDALLinkType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    service_id: Union[Unset, None, int] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, AIForgedDALLinkType] = UNSET,
    other_user_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    permission: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/MarketPlace/LinkUsers".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_type: Union[Unset, None, int] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    json_other_user_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(other_user_ids, Unset):
        if other_user_ids is None:
            json_other_user_ids = None
        else:
            json_other_user_ids = other_user_ids

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "serviceId": service_id,
        "groupId": group_id,
        "type": json_type,
        "otherUserIds": json_other_user_ids,
        "role": role,
        "permission": permission,
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
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    service_id: Union[Unset, None, int] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, AIForgedDALLinkType] = UNSET,
    other_user_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    permission: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Link / Shared users to project service group

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        service_id (Union[Unset, None, int]):
        group_id (Union[Unset, None, int]):
        type (Union[Unset, None, AIForgedDALLinkType]): Type of link prokect user access
        other_user_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        permission (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        service_id=service_id,
        group_id=group_id,
        type=type,
        other_user_ids=other_user_ids,
        role=role,
        permission=permission,
        x_api_version=x_api_version,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    service_id: Union[Unset, None, int] = UNSET,
    group_id: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, AIForgedDALLinkType] = UNSET,
    other_user_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    permission: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Link / Shared users to project service group

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        service_id (Union[Unset, None, int]):
        group_id (Union[Unset, None, int]):
        type (Union[Unset, None, AIForgedDALLinkType]): Type of link prokect user access
        other_user_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        permission (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        service_id=service_id,
        group_id=group_id,
        type=type,
        other_user_ids=other_user_ids,
        role=role,
        permission=permission,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)
