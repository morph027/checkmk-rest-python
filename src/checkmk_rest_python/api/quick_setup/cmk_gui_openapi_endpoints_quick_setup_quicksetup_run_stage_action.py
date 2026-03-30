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
from ...models.quick_setup_stage_action_request import QuickSetupStageActionRequest
from ...models.quick_setup_stage_action_response import QuickSetupStageActionResponse
from ...types import Response


def _get_kwargs(
    quick_setup_id: str,
    *,
    body: QuickSetupStageActionRequest,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/objects/quick_setup/{quick_setup_id}/actions/run-stage-action/invoke".format(
            quick_setup_id=quote(str(quick_setup_id), safe=""),
        ),
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
    | QuickSetupStageActionResponse
    | None
):
    if response.status_code == 200:
        response_200 = QuickSetupStageActionResponse.from_dict(response.json())

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
    | QuickSetupStageActionResponse
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
    body: QuickSetupStageActionRequest,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupStageActionResponse
]:
    """Run a Quick setup stage validation and recap action

    Args:
        quick_setup_id (str):  Example: aws.
        content_type (str):  Example: application/json.
        body (QuickSetupStageActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupStageActionResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        body=body,
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
    body: QuickSetupStageActionRequest,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupStageActionResponse
    | None
):
    """Run a Quick setup stage validation and recap action

    Args:
        quick_setup_id (str):  Example: aws.
        content_type (str):  Example: application/json.
        body (QuickSetupStageActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupStageActionResponse
    """

    return sync_detailed(
        quick_setup_id=quick_setup_id,
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupStageActionRequest,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupStageActionResponse
]:
    """Run a Quick setup stage validation and recap action

    Args:
        quick_setup_id (str):  Example: aws.
        content_type (str):  Example: application/json.
        body (QuickSetupStageActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupStageActionResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: QuickSetupStageActionRequest,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | QuickSetupStageActionResponse
    | None
):
    """Run a Quick setup stage validation and recap action

    Args:
        quick_setup_id (str):  Example: aws.
        content_type (str):  Example: application/json.
        body (QuickSetupStageActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError | QuickSetupStageActionResponse
    """

    return (
        await asyncio_detailed(
            quick_setup_id=quick_setup_id,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
