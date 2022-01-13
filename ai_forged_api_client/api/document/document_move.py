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
    to_stpd_id: Union[Unset, None, int] = UNSET,
    to_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    to_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/Move".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_to_status: Union[Unset, None, int] = UNSET
    if not isinstance(to_status, Unset):
        json_to_status = to_status.value if to_status else None

    json_to_usage: Union[Unset, None, int] = UNSET
    if not isinstance(to_usage, Unset):
        json_to_usage = to_usage.value if to_usage else None

    json_doc_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(doc_ids, Unset):
        if doc_ids is None:
            json_doc_ids = None
        else:
            json_doc_ids = doc_ids

    params: Dict[str, Any] = {
        "projectId": project_id,
        "toStpdId": to_stpd_id,
        "toStatus": json_to_status,
        "toUsage": json_to_usage,
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
    to_stpd_id: Union[Unset, None, int] = UNSET,
    to_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    to_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Move a document to another project and service

    Args:
        project_id (Union[Unset, None, int]):
        to_stpd_id (Union[Unset, None, int]):
        to_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        to_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        doc_ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        to_stpd_id=to_stpd_id,
        to_status=to_status,
        to_usage=to_usage,
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
    to_stpd_id: Union[Unset, None, int] = UNSET,
    to_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    to_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    doc_ids: Union[Unset, None, List[int]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Move a document to another project and service

    Args:
        project_id (Union[Unset, None, int]):
        to_stpd_id (Union[Unset, None, int]):
        to_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        to_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        doc_ids (Union[Unset, None, List[int]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        to_stpd_id=to_stpd_id,
        to_status=to_status,
        to_usage=to_usage,
        doc_ids=doc_ids,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
