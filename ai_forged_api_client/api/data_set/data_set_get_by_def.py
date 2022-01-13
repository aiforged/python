from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_sort_direction import AIForgedDALSortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field_def_id: Union[Unset, None, int] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    search_filter: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/DataSet/GetByDef".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_sort_direction: Union[None, Unset, int]
    if isinstance(sort_direction, Unset):
        json_sort_direction = UNSET
    elif sort_direction is None:
        json_sort_direction = None
    else:
        json_sort_direction = UNSET
        if not isinstance(sort_direction, Unset):
            json_sort_direction = sort_direction.value if sort_direction else None

    params: Dict[str, Any] = {
        "projectId": project_id,
        "stpdId": stpd_id,
        "pdId": pd_id,
        "includeData": include_data,
        "pageNo": page_no,
        "pageSize": page_size,
        "sortFieldDefId": sort_field_def_id,
        "sortDirection": json_sort_direction,
        "searchFilter": search_filter,
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
    pd_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field_def_id: Union[Unset, None, int] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    search_filter: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Extract custom dataset

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field_def_id (Union[Unset, None, int]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        search_filter (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        pd_id=pd_id,
        include_data=include_data,
        page_no=page_no,
        page_size=page_size,
        sort_field_def_id=sort_field_def_id,
        sort_direction=sort_direction,
        search_filter=search_filter,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    include_data: Union[Unset, None, bool] = UNSET,
    page_no: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    sort_field_def_id: Union[Unset, None, int] = UNSET,
    sort_direction: Union[AIForgedDALSortDirection, None, Unset] = UNSET,
    search_filter: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Extract custom dataset

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        include_data (Union[Unset, None, bool]):
        page_no (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_field_def_id (Union[Unset, None, int]):
        sort_direction (Union[AIForgedDALSortDirection, None, Unset]):
        search_filter (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        pd_id=pd_id,
        include_data=include_data,
        page_no=page_no,
        page_size=page_size,
        sort_field_def_id=sort_field_def_id,
        sort_direction=sort_direction,
        search_filter=search_filter,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
