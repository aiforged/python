import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_sort_direction import AIForgedDALSortDirection
from ...models.ai_forged_dal_sort_field import AIForgedDALSortField
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...models.ai_forged_view_models_verification_summary import AIForgedViewModelsVerificationSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    filetype: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Verification/GetExtended".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_usage: Union[None, Unset, int]
    if isinstance(usage, Unset):
        json_usage = UNSET
    elif usage is None:
        json_usage = None
    else:
        json_usage = UNSET
        if not isinstance(usage, Unset):
            json_usage = usage.value if usage else None

    json_statuses: Union[Unset, None, List[int]] = UNSET
    if not isinstance(statuses, Unset):
        if statuses is None:
            json_statuses = None
        else:
            json_statuses = []
            for statuses_item_data in statuses:
                statuses_item = statuses_item_data.value

                json_statuses.append(statuses_item)

    json_start: Union[Unset, None, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat() if start else None

    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

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
        "stpdId": stpd_id,
        "usage": json_usage,
        "statuses": json_statuses,
        "classname": classname,
        "filename": filename,
        "filetype": filetype,
        "start": json_start,
        "end": json_end,
        "masterid": masterid,
        "pageNo": page_no,
        "pageSize": page_size,
        "sortField": json_sort_field,
        "sortDirection": json_sort_direction,
        "comment": comment,
        "result": result,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsVerificationSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsVerificationSummary]]:
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
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    filetype: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationSummary]]:
    """Get extended verification info

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        classname (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        filetype (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        masterid (Union[Unset, None, int]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        classname=classname,
        filename=filename,
        filetype=filetype,
        start=start,
        end=end,
        masterid=masterid,
        page_no=page_no,
        page_size=page_size,
        sort_field=sort_field,
        sort_direction=sort_direction,
        comment=comment,
        result=result,
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
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    filetype: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    """Get extended verification info

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        classname (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        filetype (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        masterid (Union[Unset, None, int]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        classname=classname,
        filename=filename,
        filetype=filetype,
        start=start,
        end=end,
        masterid=masterid,
        page_no=page_no,
        page_size=page_size,
        sort_field=sort_field,
        sort_direction=sort_direction,
        comment=comment,
        result=result,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    filetype: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationSummary]]:
    """Get extended verification info

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        classname (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        filetype (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        masterid (Union[Unset, None, int]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        classname=classname,
        filename=filename,
        filetype=filetype,
        start=start,
        end=end,
        masterid=masterid,
        page_no=page_no,
        page_size=page_size,
        sort_field=sort_field,
        sort_direction=sort_direction,
        comment=comment,
        result=result,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    filetype: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field: Union[AIForgedDALSortField, None, Unset] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    """Get extended verification info

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        classname (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        filetype (Union[Unset, None, str]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
        masterid (Union[Unset, None, int]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field (Union[AIForgedDALSortField, None, Unset]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            project_id=project_id,
            stpd_id=stpd_id,
            usage=usage,
            statuses=statuses,
            classname=classname,
            filename=filename,
            filetype=filetype,
            start=start,
            end=end,
            masterid=masterid,
            page_no=page_no,
            page_size=page_size,
            sort_field=sort_field,
            sort_direction=sort_direction,
            comment=comment,
            result=result,
            x_api_version=x_api_version,
        )
    ).parsed
