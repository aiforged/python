from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_work_item_method import AIForgedDALWorkItemMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    method: Union[Unset, None, AIForgedDALWorkItemMethod] = UNSET,
    to_user_id: Union[Unset, None, str] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    graceperiod: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/WorkItem/RejectShred".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_method: Union[Unset, None, int] = UNSET
    if not isinstance(method, Unset):
        json_method = method.value if method else None

    params: Dict[str, Any] = {
        "docId": doc_id,
        "shredId": shred_id,
        "method": json_method,
        "toUserId": to_user_id,
        "comment": comment,
        "graceperiod": graceperiod,
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
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    method: Union[Unset, None, AIForgedDALWorkItemMethod] = UNSET,
    to_user_id: Union[Unset, None, str] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    graceperiod: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Reject work items for a shred

    Args:
        doc_id (Union[Unset, None, int]):
        shred_id (Union[Unset, None, int]):
        method (Union[Unset, None, AIForgedDALWorkItemMethod]): Work items assignment method
        to_user_id (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        graceperiod (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        shred_id=shred_id,
        method=method,
        to_user_id=to_user_id,
        comment=comment,
        graceperiod=graceperiod,
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
    doc_id: Union[Unset, None, int] = UNSET,
    shred_id: Union[Unset, None, int] = UNSET,
    method: Union[Unset, None, AIForgedDALWorkItemMethod] = UNSET,
    to_user_id: Union[Unset, None, str] = UNSET,
    comment: Union[Unset, None, str] = UNSET,
    graceperiod: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Reject work items for a shred

    Args:
        doc_id (Union[Unset, None, int]):
        shred_id (Union[Unset, None, int]):
        method (Union[Unset, None, AIForgedDALWorkItemMethod]): Work items assignment method
        to_user_id (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        graceperiod (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        shred_id=shred_id,
        method=method,
        to_user_id=to_user_id,
        comment=comment,
        graceperiod=graceperiod,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
