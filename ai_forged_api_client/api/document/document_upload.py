from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...models.document_upload_multipart_data import DocumentUploadMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: DocumentUploadMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    class_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/Upload".format(client.base_url)

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

    params: Dict[str, Any] = {
        "stpdId": stpd_id,
        "userId": user_id,
        "projectId": project_id,
        "classId": class_id,
        "status": json_status,
        "usage": json_usage,
        "masterid": masterid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    multipart_data: DocumentUploadMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    class_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Upload a document

    Args:
        stpd_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        class_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document
            in the system
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        masterid (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        multipart_data (DocumentUploadMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        stpd_id=stpd_id,
        user_id=user_id,
        project_id=project_id,
        class_id=class_id,
        status=status,
        usage=usage,
        masterid=masterid,
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
    multipart_data: DocumentUploadMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    class_id: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    masterid: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Upload a document

    Args:
        stpd_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        class_id (Union[Unset, None, int]):
        status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document
            in the system
        usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        masterid (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        multipart_data (DocumentUploadMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        stpd_id=stpd_id,
        user_id=user_id,
        project_id=project_id,
        class_id=class_id,
        status=status,
        usage=usage,
        masterid=masterid,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
