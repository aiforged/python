from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_grouping_type import AIForgedDALGroupingType
from ...models.ai_forged_dal_parameter_definition_category import AIForgedDALParameterDefinitionCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    doc_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    category: Union[AIForgedDALParameterDefinitionCategory, None, Unset] = UNSET,
    grouping: Union[AIForgedDALGroupingType, None, Unset] = UNSET,
    includeverification: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Parameters/Get".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_category: Union[None, Unset, int]
    if isinstance(category, Unset):
        json_category = UNSET
    elif category is None:
        json_category = None
    else:
        json_category = UNSET
        if not isinstance(category, Unset):
            json_category = category.value if category else None

    json_grouping: Union[None, Unset, int]
    if isinstance(grouping, Unset):
        json_grouping = UNSET
    elif grouping is None:
        json_grouping = None
    else:
        json_grouping = UNSET
        if not isinstance(grouping, Unset):
            json_grouping = grouping.value if grouping else None

    params: Dict[str, Any] = {
        "docId": doc_id,
        "stpdId": stpd_id,
        "category": json_category,
        "grouping": json_grouping,
        "includeverification": includeverification,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    category: Union[AIForgedDALParameterDefinitionCategory, None, Unset] = UNSET,
    grouping: Union[AIForgedDALGroupingType, None, Unset] = UNSET,
    includeverification: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get parameter value

    Args:
        doc_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        category (Union[AIForgedDALParameterDefinitionCategory, None, Unset]):
        grouping (Union[AIForgedDALGroupingType, None, Unset]):
        includeverification (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        stpd_id=stpd_id,
        category=category,
        grouping=grouping,
        includeverification=includeverification,
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
    doc_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    category: Union[AIForgedDALParameterDefinitionCategory, None, Unset] = UNSET,
    grouping: Union[AIForgedDALGroupingType, None, Unset] = UNSET,
    includeverification: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get parameter value

    Args:
        doc_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        category (Union[AIForgedDALParameterDefinitionCategory, None, Unset]):
        grouping (Union[AIForgedDALGroupingType, None, Unset]):
        includeverification (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        doc_id=doc_id,
        stpd_id=stpd_id,
        category=category,
        grouping=grouping,
        includeverification=includeverification,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
