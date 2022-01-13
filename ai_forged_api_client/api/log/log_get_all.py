from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    service_id: Union[Unset, None, int] = UNSET,
    document_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    parameter_id: Union[Unset, None, int] = UNSET,
    ver_id: Union[Unset, None, int] = UNSET,
    workitem_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Log/GetAll".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "projectId": project_id,
        "serviceId": service_id,
        "documentId": document_id,
        "defId": def_id,
        "parameterId": parameter_id,
        "verId": ver_id,
        "workitemId": workitem_id,
        "userId": user_id,
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
    service_id: Union[Unset, None, int] = UNSET,
    document_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    parameter_id: Union[Unset, None, int] = UNSET,
    ver_id: Union[Unset, None, int] = UNSET,
    workitem_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get logs by search criteria

    Args:
        project_id (Union[Unset, None, int]):
        service_id (Union[Unset, None, int]):
        document_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        parameter_id (Union[Unset, None, int]):
        ver_id (Union[Unset, None, int]):
        workitem_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        service_id=service_id,
        document_id=document_id,
        def_id=def_id,
        parameter_id=parameter_id,
        ver_id=ver_id,
        workitem_id=workitem_id,
        user_id=user_id,
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
    project_id: Union[Unset, None, int] = UNSET,
    service_id: Union[Unset, None, int] = UNSET,
    document_id: Union[Unset, None, int] = UNSET,
    def_id: Union[Unset, None, int] = UNSET,
    parameter_id: Union[Unset, None, int] = UNSET,
    ver_id: Union[Unset, None, int] = UNSET,
    workitem_id: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get logs by search criteria

    Args:
        project_id (Union[Unset, None, int]):
        service_id (Union[Unset, None, int]):
        document_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        parameter_id (Union[Unset, None, int]):
        ver_id (Union[Unset, None, int]):
        workitem_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        service_id=service_id,
        document_id=document_id,
        def_id=def_id,
        parameter_id=parameter_id,
        ver_id=ver_id,
        workitem_id=workitem_id,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
