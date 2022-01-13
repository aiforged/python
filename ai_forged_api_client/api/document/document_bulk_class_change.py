from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    from_class_id: Union[Unset, None, int] = UNSET,
    to_class_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/BulkClassChange".format(client.base_url)

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

    params: Dict[str, Any] = {
        "projectId": project_id,
        "stpdIdFrom": stpd_id_from,
        "statusFrom": json_status_from,
        "usageFrom": json_usage_from,
        "fromClassId": from_class_id,
        "toClassId": to_class_id,
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
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    from_class_id: Union[Unset, None, int] = UNSET,
    to_class_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Bulk change document classes by status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        from_class_id (Union[Unset, None, int]):
        to_class_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        from_class_id=from_class_id,
        to_class_id=to_class_id,
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
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    from_class_id: Union[Unset, None, int] = UNSET,
    to_class_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Bulk change document classes by status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        from_class_id (Union[Unset, None, int]):
        to_class_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        from_class_id=from_class_id,
        to_class_id=to_class_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    from_class_id: Union[Unset, None, int] = UNSET,
    to_class_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[int]:
    """Bulk change document classes by status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        from_class_id (Union[Unset, None, int]):
        to_class_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id_from=stpd_id_from,
        status_from=status_from,
        usage_from=usage_from,
        from_class_id=from_class_id,
        to_class_id=to_class_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id_from: Union[Unset, None, int] = UNSET,
    status_from: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET,
    usage_from: Union[Unset, None, AIForgedDALUsageType] = UNSET,
    from_class_id: Union[Unset, None, int] = UNSET,
    to_class_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[int]:
    """Bulk change document classes by status and usage

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id_from (Union[Unset, None, int]):
        status_from (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a
            document in the system
        usage_from (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        from_class_id (Union[Unset, None, int]):
        to_class_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[int]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            stpd_id_from=stpd_id_from,
            status_from=status_from,
            usage_from=usage_from,
            from_class_id=from_class_id,
            to_class_id=to_class_id,
            x_api_version=x_api_version,
        )
    ).parsed
