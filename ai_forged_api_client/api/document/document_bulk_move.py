from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_from_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    project_to_id: Union[Unset, None, int] = UNSET,
    stpd_id_to: Union[Unset, None, int] = UNSET,
    status_to: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_to: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/BulkMove".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_status_from: Union[Unset, None, int] = UNSET
    if not isinstance(status_from, Unset):
        json_status_from = status_from.value if status_from else None

    json_usage_from: Union[Unset, None, int] = UNSET
    if not isinstance(usage_from, Unset):
        json_usage_from = usage_from.value if usage_from else None

    json_status_to: Union[Unset, None, int] = UNSET
    if not isinstance(status_to, Unset):
        json_status_to = status_to.value if status_to else None

    json_usage_to: Union[Unset, None, int] = UNSET
    if not isinstance(usage_to, Unset):
        json_usage_to = usage_to.value if usage_to else None

    params: Dict[str, Any] = {
        "projectFromId": project_from_id,
        "stpdIdFrom": stpd_id_from,
        "statusFrom": json_status_from,
        "usageFrom": json_usage_from,
        "projectToId": project_to_id,
        "stpdIdTo": stpd_id_to,
        "statusTo": json_status_to,
        "usageTo": json_usage_to,
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
    project_from_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    project_to_id: Union[Unset, None, int] = UNSET,
    stpd_id_to: Union[Unset, None, int] = UNSET,
    status_to: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_to: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Bulk Mode document by status and usage to another service

    Args:
        project_from_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        project_to_id (Union[Unset, None, int]):
        stpd_id_to (Union[Unset, None, int]):
        status_to (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_to (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        project_from_id=project_from_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        project_to_id=project_to_id,
        stpd_id_to=stpd_id_to,
        status_to=status_to,
        usage_to=usage_to,
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
    project_from_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    project_to_id: Union[Unset, None, int] = UNSET,
    stpd_id_to: Union[Unset, None, int] = UNSET,
    status_to: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_to: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Bulk Mode document by status and usage to another service

    Args:
        project_from_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        project_to_id (Union[Unset, None, int]):
        stpd_id_to (Union[Unset, None, int]):
        status_to (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_to (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return sync_detailed(
        client=client,
        project_from_id=project_from_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        project_to_id=project_to_id,
        stpd_id_to=stpd_id_to,
        status_to=status_to,
        usage_to=usage_to,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    project_from_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    project_to_id: Union[Unset, None, int] = UNSET,
    stpd_id_to: Union[Unset, None, int] = UNSET,
    status_to: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_to: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Bulk Mode document by status and usage to another service

    Args:
        project_from_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        project_to_id (Union[Unset, None, int]):
        stpd_id_to (Union[Unset, None, int]):
        status_to (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_to (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        project_from_id=project_from_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        project_to_id=project_to_id,
        stpd_id_to=stpd_id_to,
        status_to=status_to,
        usage_to=usage_to,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    project_from_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    project_to_id: Union[Unset, None, int] = UNSET,
    stpd_id_to: Union[Unset, None, int] = UNSET,
    status_to: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_to: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Bulk Mode document by status and usage to another service

    Args:
        project_from_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        project_to_id (Union[Unset, None, int]):
        stpd_id_to (Union[Unset, None, int]):
        status_to (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_to (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_from_id=project_from_id,
            stpd_id_from=stpd_id_from,
            status_from=status_from,
            usage_from=usage_from,
            project_to_id=project_to_id,
            stpd_id_to=stpd_id_to,
            status_to=status_to,
            usage_to=usage_to,
            x_api_version=x_api_version,
        )
    ).parsed
