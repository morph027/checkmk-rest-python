from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_412_default_error import Api412DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.api_428_default_error import Api428DefaultError
from ...models.broker_connection_request_update import BrokerConnectionRequestUpdate
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: BrokerConnectionRequestUpdate,
    if_match: str,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/broker_connection/{connection_id}".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 412:
        response_412 = Api412DefaultError.from_dict(response.json())

        return response_412

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if response.status_code == 428:
        response_428 = Api428DefaultError.from_dict(response.json())

        return response_428

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BrokerConnectionRequestUpdate,
    if_match: str,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    """Edit a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (BrokerConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BrokerConnectionRequestUpdate,
    if_match: str,
    content_type: str,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
    | None
):
    """Edit a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (BrokerConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
        if_match=if_match,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BrokerConnectionRequestUpdate,
    if_match: str,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    """Edit a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (BrokerConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BrokerConnectionRequestUpdate,
    if_match: str,
    content_type: str,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
    | None
):
    """Edit a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (BrokerConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
            if_match=if_match,
            content_type=content_type,
        )
    ).parsed
