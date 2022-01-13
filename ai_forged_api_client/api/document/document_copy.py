from typing import Any, Dict, List, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    include_all_data: Union[Unset, None, bool] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/Copy".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_status: Union[Unset, None, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    json_usage: Union[Unset, None, int] = UNSET
    if not isinstance(usage, Unset):
        json_usage = usage.value if usage else None

    json_doc_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(doc_ids, Unset):
        if doc_ids is None:
            json_doc_ids = None
        else:
            json_doc_ids = doc_ids

    params: Dict[str, Any] = {
        "projectId": project_id,
        "stpdId": stpd_id,
        "status": json_status,
        "usage": json_usage,
        "includeAllData": include_all_data,
        "docIds": json_doc_ids,
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
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    include_all_data: Union[Unset, None, bool] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Copy a document to another project/service and supply a new status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document
            in the system
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        include_all_data (Union[Unset, None, bool]):
        doc_ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        status=status,
        usage=usage,
        include_all_data=include_all_data,
        doc_ids=doc_ids,
        x_api_version=x_api_version,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    include_all_data: Union[Unset, None, bool] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Copy a document to another project/service and supply a new status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document
            in the system
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        include_all_data (Union[Unset, None, bool]):
        doc_ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        status=status,
        usage=usage,
        include_all_data=include_all_data,
        doc_ids=doc_ids,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
