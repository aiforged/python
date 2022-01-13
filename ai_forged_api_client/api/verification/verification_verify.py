from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.ai_forged_view_models_verification_view_model import AIForgedViewModelsVerificationViewModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: List[AIForgedViewModelsVerificationViewModel],
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Verification/Verify".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "docId": doc_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AIForgedViewModelsVerificationViewModel]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AIForgedViewModelsVerificationViewModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AIForgedViewModelsVerificationViewModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[AIForgedViewModelsVerificationViewModel],
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationViewModel]]:
    """Create a list of verifications

    Args:
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        json_body (List[AIForgedViewModelsVerificationViewModel]):

    Returns:
        Response[List[AIForgedViewModelsVerificationViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        doc_id=doc_id,
        x_api_version=x_api_version,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: List[AIForgedViewModelsVerificationViewModel],
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationViewModel]]:
    """Create a list of verifications

    Args:
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        json_body (List[AIForgedViewModelsVerificationViewModel]):

    Returns:
        Response[List[AIForgedViewModelsVerificationViewModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        doc_id=doc_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[AIForgedViewModelsVerificationViewModel],
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[List[AIForgedViewModelsVerificationViewModel]]:
    """Create a list of verifications

    Args:
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        json_body (List[AIForgedViewModelsVerificationViewModel]):

    Returns:
        Response[List[AIForgedViewModelsVerificationViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        doc_id=doc_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: List[AIForgedViewModelsVerificationViewModel],
    doc_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Optional[List[AIForgedViewModelsVerificationViewModel]]:
    """Create a list of verifications

    Args:
        doc_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        json_body (List[AIForgedViewModelsVerificationViewModel]):

    Returns:
        Response[List[AIForgedViewModelsVerificationViewModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            doc_id=doc_id,
            x_api_version=x_api_version,
        )
    ).parsed
