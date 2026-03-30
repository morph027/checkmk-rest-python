from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.quick_setup_complete_response import QuickSetupCompleteResponse
from ...models.quick_setup_final_action_request import QuickSetupFinalActionRequest
from ...types import UNSET, Response


def _get_kwargs(
    quick_setup_id: str,
    *,
    body: QuickSetupFinalActionRequest,
    object_id: str,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    params: dict[str, Any] = {}

    params["object_id"] = object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/quick_setup/{quick_setup_id}/actions/edit/invoke".format(
            quick_setup_id=quote(str(quick_setup_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
    | None
):
    if response.status_code == 200:
        response_200 = QuickSetupCompleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

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
) -> Response[
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupFinalActionRequest,
    object_id: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
]:
    """Edit the quick setup

    Args:
        quick_setup_id (str):  Example: aws.
        object_id (str):  Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.
        content_type (str):  Example: application/json.
        body (QuickSetupFinalActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupCompleteResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        body=body,
        object_id=object_id,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupFinalActionRequest,
    object_id: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
    | None
):
    """Edit the quick setup

    Args:
        quick_setup_id (str):  Example: aws.
        object_id (str):  Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.
        content_type (str):  Example: application/json.
        body (QuickSetupFinalActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupCompleteResponse
    """

    return sync_detailed(
        quick_setup_id=quick_setup_id,
        client=client,
        body=body,
        object_id=object_id,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupFinalActionRequest,
    object_id: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
]:
    """Edit the quick setup

    Args:
        quick_setup_id (str):  Example: aws.
        object_id (str):  Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.
        content_type (str):  Example: application/json.
        body (QuickSetupFinalActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupCompleteResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        body=body,
        object_id=object_id,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupFinalActionRequest,
    object_id: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupCompleteResponse
    | None
):
    """Edit the quick setup

    Args:
        quick_setup_id (str):  Example: aws.
        object_id (str):  Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.
        content_type (str):  Example: application/json.
        body (QuickSetupFinalActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupCompleteResponse
    """

    return (
        await asyncio_detailed(
            quick_setup_id=quick_setup_id,
            client=client,
            body=body,
            object_id=object_id,
            content_type=content_type,
        )
    ).parsed
