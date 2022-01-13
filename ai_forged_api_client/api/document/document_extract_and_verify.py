from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.document_extract_and_verify_multipart_data import DocumentExtractAndVerifyMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: DocumentExtractAndVerifyMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Document/ExtractAndVerify".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    params: Dict[str, Any] = {
        "stpdId": stpd_id,
        "projectId": project_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    multipart_data: DocumentExtractAndVerifyMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Upload and extract information for verification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        multipart_data (DocumentExtractAndVerifyMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        stpd_id=stpd_id,
        project_id=project_id,
        x_api_version=x_api_version,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: DocumentExtractAndVerifyMultipartData,
    stpd_id: Union[Unset, None, int] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Upload and extract information for verification

    Args:
        stpd_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        x_api_version (Union[Unset, None, str]):
        multipart_data (DocumentExtractAndVerifyMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        stpd_id=stpd_id,
        project_id=project_id,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
