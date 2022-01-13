import datetime
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
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
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    result_id: Union[Unset, None, str] = UNSET,
    result_index: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    doc_guid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/GetExtendedCount".format(client.base_url)

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
        "comment": comment,
        "result": result,
        "resultId": result_id,
        "resultIndex": result_index,
        "externalId": external_id,
        "docGuid": doc_guid,
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
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    result_id: Union[Unset, None, str] = UNSET,
    result_index: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    doc_guid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Find documnets count by using structured search criteria
    This is used to detemine paging

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
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        result_id (Union[Unset, None, str]):
        result_index (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        doc_guid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
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
        comment=comment,
        result=result,
        result_id=result_id,
        result_index=result_index,
        external_id=external_id,
        doc_guid=doc_guid,
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
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    result_id: Union[Unset, None, str] = UNSET,
    result_index: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    doc_guid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Find documnets count by using structured search criteria
    This is used to detemine paging

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
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        result_id (Union[Unset, None, str]):
        result_index (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        doc_guid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
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
        comment=comment,
        result=result,
        result_id=result_id,
        result_index=result_index,
        external_id=external_id,
        doc_guid=doc_guid,
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
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    result_id: Union[Unset, None, str] = UNSET,
    result_index: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    doc_guid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Find documnets count by using structured search criteria
    This is used to detemine paging

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
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        result_id (Union[Unset, None, str]):
        result_index (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        doc_guid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
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
        comment=comment,
        result=result,
        result_id=result_id,
        result_index=result_index,
        external_id=external_id,
        doc_guid=doc_guid,
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
    comment: Union[Unset, None, str] = UNSET,
    result: Union[Unset, None, str] = UNSET,
    result_id: Union[Unset, None, str] = UNSET,
    result_index: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    doc_guid: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Find documnets count by using structured search criteria
    This is used to detemine paging

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
        comment (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
        result_id (Union[Unset, None, str]):
        result_index (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        doc_guid (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
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
            comment=comment,
            result=result,
            result_id=result_id,
            result_index=result_index,
            external_id=external_id,
            doc_guid=doc_guid,
            x_api_version=x_api_version,
        )
    ).parsed
