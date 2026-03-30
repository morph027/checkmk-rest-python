from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_409_default_error import Api409DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.parent_scan import ParentScan
from ...types import Response


def _get_kwargs(
    *,
    body: ParentScan,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/parent_scan/actions/start/invoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = Api409DefaultError.from_dict(response.json())

        return response_409

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
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ParentScan,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
]:
    """Start the parent scan background job



    This endpoint requires the following permissions:
     * All of:
       * `wato.hosts`: Access to the management of hosts and folders. This module has some additional
    permissions (see below).
       * `wato.parentscan`: This permission is necessary for performing automatic scans for network
    parents of hosts (making use of traceroute). Please note, that for actually modifying the parents
    via the scan and for the creation of gateway hosts proper permissions for host and folders are also
    necessary.

    Args:
        content_type (str):  Example: application/json.
        body (ParentScan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | Api409DefaultError | Api415DefaultError]
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
    body: ParentScan,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
    | None
):
    """Start the parent scan background job



    This endpoint requires the following permissions:
     * All of:
       * `wato.hosts`: Access to the management of hosts and folders. This module has some additional
    permissions (see below).
       * `wato.parentscan`: This permission is necessary for performing automatic scans for network
    parents of hosts (making use of traceroute). Please note, that for actually modifying the parents
    via the scan and for the creation of gateway hosts proper permissions for host and folders are also
    necessary.

    Args:
        content_type (str):  Example: application/json.
        body (ParentScan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | Api409DefaultError | Api415DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ParentScan,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
]:
    """Start the parent scan background job



    This endpoint requires the following permissions:
     * All of:
       * `wato.hosts`: Access to the management of hosts and folders. This module has some additional
    permissions (see below).
       * `wato.parentscan`: This permission is necessary for performing automatic scans for network
    parents of hosts (making use of traceroute). Please note, that for actually modifying the parents
    via the scan and for the creation of gateway hosts proper permissions for host and folders are also
    necessary.

    Args:
        content_type (str):  Example: application/json.
        body (ParentScan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | Api409DefaultError | Api415DefaultError]
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
    body: ParentScan,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | Api415DefaultError
    | None
):
    """Start the parent scan background job



    This endpoint requires the following permissions:
     * All of:
       * `wato.hosts`: Access to the management of hosts and folders. This module has some additional
    permissions (see below).
       * `wato.parentscan`: This permission is necessary for performing automatic scans for network
    parents of hosts (making use of traceroute). Please note, that for actually modifying the parents
    via the scan and for the creation of gateway hosts proper permissions for host and folders are also
    necessary.

    Args:
        content_type (str):  Example: application/json.
        body (ParentScan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | Api409DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
