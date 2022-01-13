import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ai_forged_dal_notification_area import AIForgedDALNotificationArea
from ...models.ai_forged_dal_notification_event import AIForgedDALNotificationEvent
from ...models.ai_forged_dal_notification_status import AIForgedDALNotificationStatus
from ...models.ai_forged_dal_notification_type import AIForgedDALNotificationType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    include_already_read: Union[Unset, None, bool] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    body: Union[Unset, None, str] = UNSET,
    error: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALNotificationType, None, Unset] = UNSET,
    status: Union[AIForgedDALNotificationStatus, None, Unset] = UNSET,
    area: Union[AIForgedDALNotificationArea, None, Unset] = UNSET,
    evnt: Union[AIForgedDALNotificationEvent, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Notification/GetCount".format(client.base_url)

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

    json_status: Union[None, Unset, int]
    if isinstance(status, Unset):
        json_status = UNSET
    elif status is None:
        json_status = None
    else:
        json_status = UNSET
        if not isinstance(status, Unset):
            json_status = status.value if status else None

    json_area: Union[None, Unset, int]
    if isinstance(area, Unset):
        json_area = UNSET
    elif area is None:
        json_area = None
    else:
        json_area = UNSET
        if not isinstance(area, Unset):
            json_area = area.value if area else None

    json_evnt: Union[None, Unset, int]
    if isinstance(evnt, Unset):
        json_evnt = UNSET
    elif evnt is None:
        json_evnt = None
    else:
        json_evnt = UNSET
        if not isinstance(evnt, Unset):
            json_evnt = evnt.value if evnt else None

    params: Dict[str, Any] = {
        "userId": user_id,
        "fromDate": json_from_date,
        "toDate": json_to_date,
        "includeAlreadyRead": include_already_read,
        "to": to,
        "subject": subject,
        "body": body,
        "error": error,
        "type": json_type,
        "status": json_status,
        "area": json_area,
        "evnt": json_evnt,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[int]:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[int]:
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
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    include_already_read: Union[Unset, None, bool] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    body: Union[Unset, None, str] = UNSET,
    error: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALNotificationType, None, Unset] = UNSET,
    status: Union[AIForgedDALNotificationStatus, None, Unset] = UNSET,
    area: Union[AIForgedDALNotificationArea, None, Unset] = UNSET,
    evnt: Union[AIForgedDALNotificationEvent, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Get Notifications Count

    Args:
        user_id (Union[Unset, None, str]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        include_already_read (Union[Unset, None, bool]):
        to (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        body (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
        type (Union[AIForgedDALNotificationType, None, Unset]):
        status (Union[AIForgedDALNotificationStatus, None, Unset]):
        area (Union[AIForgedDALNotificationArea, None, Unset]):
        evnt (Union[AIForgedDALNotificationEvent, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        from_date=from_date,
        to_date=to_date,
        include_already_read=include_already_read,
        to=to,
        subject=subject,
        body=body,
        error=error,
        type=type,
        status=status,
        area=area,
        evnt=evnt,
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
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    include_already_read: Union[Unset, None, bool] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    body: Union[Unset, None, str] = UNSET,
    error: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALNotificationType, None, Unset] = UNSET,
    status: Union[AIForgedDALNotificationStatus, None, Unset] = UNSET,
    area: Union[AIForgedDALNotificationArea, None, Unset] = UNSET,
    evnt: Union[AIForgedDALNotificationEvent, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Get Notifications Count

    Args:
        user_id (Union[Unset, None, str]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        include_already_read (Union[Unset, None, bool]):
        to (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        body (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
        type (Union[AIForgedDALNotificationType, None, Unset]):
        status (Union[AIForgedDALNotificationStatus, None, Unset]):
        area (Union[AIForgedDALNotificationArea, None, Unset]):
        evnt (Union[AIForgedDALNotificationEvent, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        from_date=from_date,
        to_date=to_date,
        include_already_read=include_already_read,
        to=to,
        subject=subject,
        body=body,
        error=error,
        type=type,
        status=status,
        area=area,
        evnt=evnt,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    include_already_read: Union[Unset, None, bool] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    body: Union[Unset, None, str] = UNSET,
    error: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALNotificationType, None, Unset] = UNSET,
    status: Union[AIForgedDALNotificationStatus, None, Unset] = UNSET,
    area: Union[AIForgedDALNotificationArea, None, Unset] = UNSET,
    evnt: Union[AIForgedDALNotificationEvent, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Get Notifications Count

    Args:
        user_id (Union[Unset, None, str]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        include_already_read (Union[Unset, None, bool]):
        to (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        body (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
        type (Union[AIForgedDALNotificationType, None, Unset]):
        status (Union[AIForgedDALNotificationStatus, None, Unset]):
        area (Union[AIForgedDALNotificationArea, None, Unset]):
        evnt (Union[AIForgedDALNotificationEvent, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        from_date=from_date,
        to_date=to_date,
        include_already_read=include_already_read,
        to=to,
        subject=subject,
        body=body,
        error=error,
        type=type,
        status=status,
        area=area,
        evnt=evnt,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    include_already_read: Union[Unset, None, bool] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    body: Union[Unset, None, str] = UNSET,
    error: Union[Unset, None, str] = UNSET,
    type: Union[AIForgedDALNotificationType, None, Unset] = UNSET,
    status: Union[AIForgedDALNotificationStatus, None, Unset] = UNSET,
    area: Union[AIForgedDALNotificationArea, None, Unset] = UNSET,
    evnt: Union[AIForgedDALNotificationEvent, None, Unset] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Get Notifications Count

    Args:
        user_id (Union[Unset, None, str]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        include_already_read (Union[Unset, None, bool]):
        to (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        body (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
        type (Union[AIForgedDALNotificationType, None, Unset]):
        status (Union[AIForgedDALNotificationStatus, None, Unset]):
        area (Union[AIForgedDALNotificationArea, None, Unset]):
        evnt (Union[AIForgedDALNotificationEvent, None, Unset]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            include_already_read=include_already_read,
            to=to,
            subject=subject,
            body=body,
            error=error,
            type=type,
            status=status,
            area=area,
            evnt=evnt,
            x_api_version=x_api_version,
        )
    ).parsed
