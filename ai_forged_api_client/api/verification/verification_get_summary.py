from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_verification_summary import AIForgedViewModelsVerificationSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    latest_only: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Verification/GetSummary".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "projectId": project_id,
        "stpdId": stpd_id,
        "pdId": pd_id,
        "latestOnly": latest_only,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsVerificationSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsVerificationSummary]]:
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
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    latest_only: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationSummary]]:
    """Get a summary of verifications

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        latest_only (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        pd_id=pd_id,
        latest_only=latest_only,
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
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    latest_only: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    """Get a summary of verifications

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        latest_only (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        pd_id=pd_id,
        latest_only=latest_only,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    latest_only: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationSummary]]:
    """Get a summary of verifications

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        latest_only (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        stpd_id=stpd_id,
        pd_id=pd_id,
        latest_only=latest_only,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    pd_id: Union[Unset, None, int] = UNSET,
    latest_only: Union[Unset, None, bool] = True,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationSummary]]:
    """Get a summary of verifications

    Args:
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        pd_id (Union[Unset, None, int]):
        latest_only (Union[Unset, None, bool]):  Default: True.
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsVerificationSummary]]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            stpd_id=stpd_id,
            pd_id=pd_id,
            latest_only=latest_only,
            x_api_version=x_api_version,
        )
    ).parsed
