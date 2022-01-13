from typing import Any, Dict, List, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    document_ids: Union[Unset, None, List[int]] = UNSET,
    force: Union[Unset, None, bool] = True,
    delete_child_docs: Union[Unset, None, bool] = False,
    delete_child_docs_recursive: Union[Unset, None, bool] = False,
    delete_previous_output_docs: Union[Unset, None, bool] = False,
    reset_results: Union[Unset, None, bool] = False,
    reset_comments: Union[Unset, None, bool] = False,
    resume_identifier: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Services/Process".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_api_version is not UNSET:
        headers["x-api-version"] = x_api_version

    json_document_ids: Union[Unset, None, List[int]] = UNSET
    if not isinstance(document_ids, Unset):
        if document_ids is None:
            json_document_ids = None
        else:
            json_document_ids = document_ids

    params: Dict[str, Any] = {
        "userId": user_id,
        "projectId": project_id,
        "stpdId": stpd_id,
        "documentIds": json_document_ids,
        "force": force,
        "deleteChildDocs": delete_child_docs,
        "deleteChildDocsRecursive": delete_child_docs_recursive,
        "deletePreviousOutputDocs": delete_previous_output_docs,
        "resetResults": reset_results,
        "resetComments": reset_comments,
        "resumeIdentifier": resume_identifier,
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
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    document_ids: Union[Unset, None, List[int]] = UNSET,
    force: Union[Unset, None, bool] = True,
    delete_child_docs: Union[Unset, None, bool] = False,
    delete_child_docs_recursive: Union[Unset, None, bool] = False,
    delete_previous_output_docs: Union[Unset, None, bool] = False,
    reset_results: Union[Unset, None, bool] = False,
    reset_comments: Union[Unset, None, bool] = False,
    resume_identifier: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Process service documents

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        document_ids (Union[Unset, None, List[int]]):
        force (Union[Unset, None, bool]):  Default: True.
        delete_child_docs (Union[Unset, None, bool]):
        delete_child_docs_recursive (Union[Unset, None, bool]):
        delete_previous_output_docs (Union[Unset, None, bool]):
        reset_results (Union[Unset, None, bool]):
        reset_comments (Union[Unset, None, bool]):
        resume_identifier (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        document_ids=document_ids,
        force=force,
        delete_child_docs=delete_child_docs,
        delete_child_docs_recursive=delete_child_docs_recursive,
        delete_previous_output_docs=delete_previous_output_docs,
        reset_results=reset_results,
        reset_comments=reset_comments,
        resume_identifier=resume_identifier,
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
    user_id: Union[Unset, None, str] = UNSET,
    project_id: Union[Unset, None, int] = UNSET,
    stpd_id: Union[Unset, None, int] = UNSET,
    document_ids: Union[Unset, None, List[int]] = UNSET,
    force: Union[Unset, None, bool] = True,
    delete_child_docs: Union[Unset, None, bool] = False,
    delete_child_docs_recursive: Union[Unset, None, bool] = False,
    delete_previous_output_docs: Union[Unset, None, bool] = False,
    reset_results: Union[Unset, None, bool] = False,
    reset_comments: Union[Unset, None, bool] = False,
    resume_identifier: Union[Unset, None, str] = UNSET,
    x_api_version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Process service documents

    Args:
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, None, int]):
        stpd_id (Union[Unset, None, int]):
        document_ids (Union[Unset, None, List[int]]):
        force (Union[Unset, None, bool]):  Default: True.
        delete_child_docs (Union[Unset, None, bool]):
        delete_child_docs_recursive (Union[Unset, None, bool]):
        delete_previous_output_docs (Union[Unset, None, bool]):
        reset_results (Union[Unset, None, bool]):
        reset_comments (Union[Unset, None, bool]):
        resume_identifier (Union[Unset, None, str]):
        x_api_version (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        project_id=project_id,
        stpd_id=stpd_id,
        document_ids=document_ids,
        force=force,
        delete_child_docs=delete_child_docs,
        delete_child_docs_recursive=delete_child_docs_recursive,
        delete_previous_output_docs=delete_previous_output_docs,
        reset_results=reset_results,
        reset_comments=reset_comments,
        resume_identifier=resume_identifier,
        x_api_version=x_api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
