from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_classes_view_model import AIForgedViewModelsClassesViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: AIForgedViewModelsClassesViewModel,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Classes/Create".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: AIForgedViewModelsClassesViewModel,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsClassesViewModel]:
    """Create a new category

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedViewModelsClassesViewModel): Categories/Classes for training and
            classification

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: AIForgedViewModelsClassesViewModel,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsClassesViewModel]:
    """Create a new category

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedViewModelsClassesViewModel): Categories/Classes for training and
            classification

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AIForgedViewModelsClassesViewModel,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[AIForgedViewModelsClassesViewModel]:
    """Create a new category

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedViewModelsClassesViewModel): Categories/Classes for training and
            classification

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AIForgedViewModelsClassesViewModel,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[AIForgedViewModelsClassesViewModel]:
    """Create a new category

    Args:
        x_api_version (Union[Unset, None, str]):
        json_body (AIForgedViewModelsClassesViewModel): Categories/Classes for training and
            classification

    Returns:
        Response[AIForgedViewModelsClassesViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_api_version=x_api_version,
        )
    ).parsed
