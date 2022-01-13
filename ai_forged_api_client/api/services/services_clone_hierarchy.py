from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ai_forged_dal_parameter_definition_category import AIForgedDALParameterDefinitionCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    pd_id_src: Union[Unset, None, int] = UNSET,
    pd_id_dst: Union[Unset, None, int] = UNSET,
    categories: Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Services/CloneHierarchy".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_categories: Union[Unset, None, List[Optional[int]]] = UNSET
    if not isinstance(categories, Unset):
        if categories is None:
            json_categories = None
        else:
            json_categories = []
            for categories_item_data in categories:
                categories_item = categories_item_data.value if categories_item_data else None

                json_categories.append(categories_item)

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "pdIdSrc": pd_id_src,
        "pdIdDst": pd_id_dst,
        "categories": json_categories,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[bool]:
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
    project_id: Union[Unset, None, int] = UNSET,
    pd_id_src: Union[Unset, None, int] = UNSET,
    pd_id_dst: Union[Unset, None, int] = UNSET,
    categories: Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Clone a service CloneHierarchy result / settings

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        pd_id_src (Union[Unset, None, int]):
        pd_id_dst (Union[Unset, None, int]):
        categories (Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        pd_id_src=pd_id_src,
        pd_id_dst=pd_id_dst,
        categories=categories,
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
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    pd_id_src: Union[Unset, None, int] = UNSET,
    pd_id_dst: Union[Unset, None, int] = UNSET,
    categories: Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Clone a service CloneHierarchy result / settings

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        pd_id_src (Union[Unset, None, int]):
        pd_id_dst (Union[Unset, None, int]):
        categories (Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        project_id=project_id,
        pd_id_src=pd_id_src,
        pd_id_dst=pd_id_dst,
        categories=categories,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    pd_id_src: Union[Unset, None, int] = UNSET,
    pd_id_dst: Union[Unset, None, int] = UNSET,
    categories: Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[bool]:
    """Clone a service CloneHierarchy result / settings

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        pd_id_src (Union[Unset, None, int]):
        pd_id_dst (Union[Unset, None, int]):
        categories (Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        pd_id_src=pd_id_src,
        pd_id_dst=pd_id_dst,
        categories=categories,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    pd_id_src: Union[Unset, None, int] = UNSET,
    pd_id_dst: Union[Unset, None, int] = UNSET,
    categories: Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[bool]:
    """Clone a service CloneHierarchy result / settings

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        pd_id_src (Union[Unset, None, int]):
        pd_id_dst (Union[Unset, None, int]):
        categories (Union[Unset, None, List[Optional[AIForgedDALParameterDefinitionCategory]]]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[bool]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            project_id=project_id,
            pd_id_src=pd_id_src,
            pd_id_dst=pd_id_dst,
            categories=categories,
            x_api_version=x_api_version,
        )
    ).parsed
