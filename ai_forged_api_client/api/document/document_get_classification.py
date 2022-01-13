from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_classes_view_model import AIForgedViewModelsClassesViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/GetClassification".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "stpdId": stpd_id,
        "projectId": project_id,
        "docId": doc_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedViewModelsClassesViewModel]:
    if response.status_code == 200:
        response_200 = AIForgedViewModelsClassesViewModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedViewModelsClassesViewModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsClassesViewModel]:
    """Upload get a document classification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        stpd_id=stpd_id,
        project_id=project_id,
        doc_id=doc_id,
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
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsClassesViewModel]:
    """Upload get a document classification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    return sync_detailed(
        client=client,
        stpd_id=stpd_id,
        project_id=project_id,
        doc_id=doc_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsClassesViewModel]:
    """Upload get a document classification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        stpd_id=stpd_id,
        project_id=project_id,
        doc_id=doc_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsClassesViewModel]:
    """Upload get a document classification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            stpd_id=stpd_id,
            project_id=project_id,
            doc_id=doc_id,
            x_api_version=x_api_version,
        )
    ).parsed
