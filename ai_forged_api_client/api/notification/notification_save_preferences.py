from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_dal_view_models_notification_preferences import AIForgedDALViewModelsNotificationPreferences
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: AIForgedDALViewModelsNotificationPreferences,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Notification/SavePreferences".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "userId": user_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AIForgedDALViewModelsNotificationPreferences]:
    if response.status_code == 200:
        response_200 = AIForgedDALViewModelsNotificationPreferences.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AIForgedDALViewModelsNotificationPreferences]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AIForgedDALViewModelsNotificationPreferences,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedDALViewModelsNotificationPreferences]:
    """Save the current user notification preferences

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedDALViewModelsNotificationPreferences):

    Returns:
        Response[AIForgedDALViewModelsNotificationPreferences]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        user_id=user_id,
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
    json_body: AIForgedDALViewModelsNotificationPreferences,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedDALViewModelsNotificationPreferences]:
    """Save the current user notification preferences

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedDALViewModelsNotificationPreferences):

    Returns:
        Response[AIForgedDALViewModelsNotificationPreferences]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AIForgedDALViewModelsNotificationPreferences,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedDALViewModelsNotificationPreferences]:
    """Save the current user notification preferences

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedDALViewModelsNotificationPreferences):

    Returns:
        Response[AIForgedDALViewModelsNotificationPreferences]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AIForgedDALViewModelsNotificationPreferences,
    user_id: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedDALViewModelsNotificationPreferences]:
    """Save the current user notification preferences

    Args:
        user_id (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedDALViewModelsNotificationPreferences):

    Returns:
        Response[AIForgedDALViewModelsNotificationPreferences]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
