from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.delete_comment_by_id import DeleteCommentById
from ...models.delete_comments_by_params import DeleteCommentsByParams
from ...models.delete_comments_by_query import DeleteCommentsByQuery
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/comment/actions/delete/invoke",
    }

    if isinstance(body, DeleteCommentById):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DeleteCommentsByQuery):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery,
    content_type: str,
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    """Delete comments



    This endpoint requires the following permissions:
     * `action.addcomment`: Add comments to hosts or services, and remove comments

    Args:
        content_type (str):  Example: application/json.
        body (DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        body=body,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery,
    content_type: str,
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    """Delete comments



    This endpoint requires the following permissions:
     * `action.addcomment`: Add comments to hosts or services, and remove comments

    Args:
        content_type (str):  Example: application/json.
        body (DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery,
    content_type: str,
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    """Delete comments



    This endpoint requires the following permissions:
     * `action.addcomment`: Add comments to hosts or services, and remove comments

    Args:
        content_type (str):  Example: application/json.
        body (DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery,
    content_type: str,
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    """Delete comments



    This endpoint requires the following permissions:
     * `action.addcomment`: Add comments to hosts or services, and remove comments

    Args:
        content_type (str):  Example: application/json.
        body (DeleteCommentById | DeleteCommentsByParams | DeleteCommentsByQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
