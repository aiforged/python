from typing import Any, Dict, List, Union

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
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/FindLatestChild".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_usage: Union[Unset, None, int] = UNSET
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

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "stpdId": stpd_id,
        "usage": json_usage,
        "statuses": json_statuses,
        "filename": filename,
        "classname": classname,
        "masterid": masterid,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Find latest child document to assist with verification

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        filename (Union[Unset, None, str]):
        classname (Union[Unset, None, str]):
        masterid (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        filename=filename,
        classname=classname,
        masterid=masterid,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
    classname: Union[Unset, None, str] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Find latest child document to assist with verification

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        filename (Union[Unset, None, str]):
        classname (Union[Unset, None, str]):
        masterid (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        filename=filename,
        classname=classname,
        masterid=masterid,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
