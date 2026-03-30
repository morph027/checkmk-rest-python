from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_custom_error_5 import Api404CustomError5
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.update_discovery_phase import UpdateDiscoveryPhase
from ...types import Response


def _get_kwargs(
    host_name: str,
    *,
    body: UpdateDiscoveryPhase,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/host/{host_name}/actions/update_discovery_phase/invoke".format(
            host_name=quote(str(host_name), safe=""),
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
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404CustomError5.from_dict(response.json())

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
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDiscoveryPhase,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update the phase of a service



    This endpoint requires the following permissions:
     * All of:
       * `wato.service_discovery_to_monitored`: Service discovery: Move to monitored services
       * `wato.service_discovery_to_ignored`: Service discovery: Disabled services
       * `wato.service_discovery_to_undecided`: Service discovery: Move to undecided services
       * `wato.service_discovery_to_removed`: Service discovery: Remove services
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (UpdateDiscoveryPhase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api403DefaultError | Api404CustomError5 | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        body=body,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDiscoveryPhase,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update the phase of a service



    This endpoint requires the following permissions:
     * All of:
       * `wato.service_discovery_to_monitored`: Service discovery: Move to monitored services
       * `wato.service_discovery_to_ignored`: Service discovery: Disabled services
       * `wato.service_discovery_to_undecided`: Service discovery: Move to undecided services
       * `wato.service_discovery_to_removed`: Service discovery: Remove services
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (UpdateDiscoveryPhase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api403DefaultError | Api404CustomError5 | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        host_name=host_name,
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDiscoveryPhase,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update the phase of a service



    This endpoint requires the following permissions:
     * All of:
       * `wato.service_discovery_to_monitored`: Service discovery: Move to monitored services
       * `wato.service_discovery_to_ignored`: Service discovery: Disabled services
       * `wato.service_discovery_to_undecided`: Service discovery: Move to undecided services
       * `wato.service_discovery_to_removed`: Service discovery: Remove services
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (UpdateDiscoveryPhase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api403DefaultError | Api404CustomError5 | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDiscoveryPhase,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404CustomError5
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update the phase of a service



    This endpoint requires the following permissions:
     * All of:
       * `wato.service_discovery_to_monitored`: Service discovery: Move to monitored services
       * `wato.service_discovery_to_ignored`: Service discovery: Disabled services
       * `wato.service_discovery_to_undecided`: Service discovery: Move to undecided services
       * `wato.service_discovery_to_removed`: Service discovery: Remove services
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (UpdateDiscoveryPhase):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api403DefaultError | Api404CustomError5 | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
