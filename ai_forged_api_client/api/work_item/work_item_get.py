import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_sort_direction import AIForgedDALSortDirection
from ...models.ai_forged_dal_sort_field import AIForgedDALSortField
from ...models.ai_forged_dal_work_item_action import AIForgedDALWorkItemAction
from ...models.ai_forged_dal_work_item_status import AIForgedDALWorkItemStatus
from ...models.ai_forged_dal_work_item_type import AIForgedDALWorkItemType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    type: Union[AIForgedDALWorkItemType, None, Unset] = UNSET,
    action: Union[AIForgedDALWorkItemAction, None, Unset] = UNSET,
    status: Union[AIForgedDALWorkItemStatus, None, Unset] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/WorkItem/Get".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_from_date: Union[Unset, None, str] = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat() if from_date else None

    json_to_date: Union[Unset, None, str] = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat() if to_date else None

    json_type: Union[None, Unset, int]
    if isinstance(type, Unset):
        json_type = UNSET
    elif type is None:
        json_type = None
    else:
        json_type = UNSET
        if not isinstance(type, Unset):
            json_type = type.value if type else None

    json_action: Union[None, Unset, int]
    if isinstance(action, Unset):
        json_action = UNSET
    elif action is None:
        json_action = None
    else:
        json_action = UNSET
        if not isinstance(action, Unset):
            json_action = action.value if action else None

    json_status: Union[None, Unset, int]
    if isinstance(status, Unset):
        json_status = UNSET
    elif status is None:
        json_status = None
    else:
        json_status = UNSET
        if not isinstance(status, Unset):
            json_status = status.value if status else None

    json_sort_field: Union[None, Unset, int]
    if isinstance(sort_field, Unset):
        json_sort_field = UNSET
    elif sort_field is None:
        json_sort_field = None
    else:
        json_sort_field = UNSET
        if not isinstance(sort_field, Unset):
            json_sort_field = sort_field.value if sort_field else None

    json_sort_direction: Union[None, Unset, int]
    if isinstance(sort_direction, Unset):
        json_sort_direction = UNSET
    elif sort_direction is None:
        json_sort_direction = None
    else:
        json_sort_direction = UNSET
        if not isinstance(sort_direction, Unset):
            json_sort_direction = sort_direction.value if sort_direction else None

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "fromDate": json_from_date,
        "toDate": json_to_date,
        "type": json_type,
        "action": json_action,
        "status": json_status,
        "docId": doc_id,
        "shredId": shred_id,
        "comment": comment,
        "pageNo": page_no,
        "pageSize": page_size,
        "sortField": json_sort_field,
        "sortDirection": json_sort_direction,
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
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    type: Union[AIForgedDALWorkItemType, None, Unset] = UNSET,
    action: Union[AIForgedDALWorkItemAction, None, Unset] = UNSET,
    status: Union[AIForgedDALWorkItemStatus, None, Unset] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get WorkItems

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        type (Union[AIForgedDALWorkItemType, None, Unset]):
        action (Union[AIForgedDALWorkItemAction, None, Unset]):
        status (Union[AIForgedDALWorkItemStatus, None, Unset]):
        doc_id (Union[Unset, None, int]):
        shred_id (Union[Unset, None, int]):
        comment (Union[Unset, None, str]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        from_date=from_date,
        to_date=to_date,
        type=type,
        action=action,
        status=status,
        doc_id=doc_id,
        shred_id=shred_id,
        comment=comment,
        page_no=page_no,
        page_size=page_size,
        sort_field=sort_field,
        sort_direction=sort_direction,
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
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    type: Union[AIForgedDALWorkItemType, None, Unset] = UNSET,
    action: Union[AIForgedDALWorkItemAction, None, Unset] = UNSET,
    status: Union[AIForgedDALWorkItemStatus, None, Unset] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get WorkItems

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        type (Union[AIForgedDALWorkItemType, None, Unset]):
        action (Union[AIForgedDALWorkItemAction, None, Unset]):
        status (Union[AIForgedDALWorkItemStatus, None, Unset]):
        doc_id (Union[Unset, None, int]):
        shred_id (Union[Unset, None, int]):
        comment (Union[Unset, None, str]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        from_date=from_date,
        to_date=to_date,
        type=type,
        action=action,
        status=status,
        doc_id=doc_id,
        shred_id=shred_id,
        comment=comment,
        page_no=page_no,
        page_size=page_size,
        sort_field=sort_field,
        sort_direction=sort_direction,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
