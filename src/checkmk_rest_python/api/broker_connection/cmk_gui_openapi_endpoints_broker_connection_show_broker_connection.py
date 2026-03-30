from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs(
    connection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/broker_connection/{connection_id}".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api404DefaultError | Api406DefaultError | None:
    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api404DefaultError | Api406DefaultError]:
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
) -> Response[Api404DefaultError | Api406DefaultError]:
    """Show a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Api404DefaultError | Api406DefaultError | None:
    """Show a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api404DefaultError | Api406DefaultError]:
    """Show a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Api404DefaultError | Api406DefaultError | None:
    """Show a peer to peer broker connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        connection_id (str):  Example: connection_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
