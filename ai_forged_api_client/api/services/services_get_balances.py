import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_account_balance_item import AIForgedViewModelsAccountBalanceItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stl: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    all_related: Union[Unset, None, bool] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Services/GetBalances".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_from_date: Union[Unset, None, str] = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat() if from_date else None

    json_to_date: Union[Unset, None, str] = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat() if to_date else None

    params: Dict[str, Any] = {
        "userId": user_id,
        "stl": stl,
        "stpdId": stpd_id,
        "projectId": project_id,
        "allRelated": all_related,
        "fromDate": json_from_date,
        "toDate": json_to_date,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsAccountBalanceItem]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsAccountBalanceItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsAccountBalanceItem]]:
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
    stl: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    all_related: Union[Unset, None, bool] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsAccountBalanceItem]]:
    """Get service balances

    Args:
        user_id (Union[Unset, None, str]):
        stl (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        all_related (Union[Unset, None, bool]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsAccountBalanceItem]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        stl=stl,
        stpd_id=stpd_id,
        project_id=project_id,
        all_related=all_related,
        from_date=from_date,
        to_date=to_date,
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
    stl: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    all_related: Union[Unset, None, bool] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsAccountBalanceItem]]:
    """Get service balances

    Args:
        user_id (Union[Unset, None, str]):
        stl (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        all_related (Union[Unset, None, bool]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsAccountBalanceItem]]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        stl=stl,
        stpd_id=stpd_id,
        project_id=project_id,
        all_related=all_related,
        from_date=from_date,
        to_date=to_date,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stl: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    all_related: Union[Unset, None, bool] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsAccountBalanceItem]]:
    """Get service balances

    Args:
        user_id (Union[Unset, None, str]):
        stl (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        all_related (Union[Unset, None, bool]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsAccountBalanceItem]]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        stl=stl,
        stpd_id=stpd_id,
        project_id=project_id,
        all_related=all_related,
        from_date=from_date,
        to_date=to_date,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    stl: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    all_related: Union[Unset, None, bool] = UNSET,
    from_date: Union[Unset, None, datetime.datetime] = UNSET,
    to_date: Union[Unset, None, datetime.datetime] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsAccountBalanceItem]]:
    """Get service balances

    Args:
        user_id (Union[Unset, None, str]):
        stl (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        all_related (Union[Unset, None, bool]):
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[List[AIForgedViewModelsAccountBalanceItem]]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            stl=stl,
            stpd_id=stpd_id,
            project_id=project_id,
            all_related=all_related,
            from_date=from_date,
            to_date=to_date,
            x_api_version=x_api_version,
        )
    ).parsed
