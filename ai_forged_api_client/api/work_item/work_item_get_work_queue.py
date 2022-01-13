from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ...models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ...models.ai_forged_view_models_documents_summary import AIForgedViewModelsDocumentsSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/WorkItem/GetWorkQueue".format(client.base_url)

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

    params: Dict[str, Any] = {
        "userId": user_id,
        "stpdId": stpd_id,
        "usage": json_usage,
        "statuses": json_statuses,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsDocumentsSummary]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsDocumentsSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsDocumentsSummary]]:
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
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsDocumentsSummary]]:
    """Get document work queue

    Args:
        user_id (Union[Unset, None, str]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentsSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsDocumentsSummary]]:
    """Get document work queue

    Args:
        user_id (Union[Unset, None, str]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentsSummary]]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsDocumentsSummary]]:
    """Get document work queue

    Args:
        user_id (Union[Unset, None, str]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentsSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        stpd_id=stpd_id,
        usage=usage,
        statuses=statuses,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    usage: Union[AIForgedDALUsageType, None, Unset] = UNSET,
    statuses: Union[Unset, None, List[AIForgedDALDocumentStatus]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsDocumentsSummary]]:
    """Get document work queue

    Args:
        user_id (Union[Unset, None, str]):
        stpd_id (Union[Unset, None, int]):
        usage (Union[AIForgedDALUsageType, None, Unset]):
        statuses (Union[Unset, None, List[AIForgedDALDocumentStatus]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsDocumentsSummary]]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            stpd_id=stpd_id,
            usage=usage,
            statuses=statuses,
            x_api_version=x_api_version,
        )
    ).parsed
