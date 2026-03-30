from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.bulk_update_host import BulkUpdateHost
from ...types import Response


def _get_kwargs(
    *,
    body: BulkUpdateHost,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/domain-types/host_config/actions/bulk-update/invoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api403DefaultError | Api406DefaultError | Api415DefaultError | None:
    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

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
) -> Response[Api403DefaultError | Api406DefaultError | Api415DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkUpdateHost,
    content_type: str,
) -> Response[Api403DefaultError | Api406DefaultError | Api415DefaultError]:
    r"""Bulk update hosts

     Please be aware that when doing bulk updates, it is not possible to prevent the
    [Updating Values](\"lost update problem\"), which is normally prevented by the ETag locking
    mechanism. Use at your own risk.This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        content_type (str):  Example: application/json.
        body (BulkUpdateHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: BulkUpdateHost,
    content_type: str,
) -> Api403DefaultError | Api406DefaultError | Api415DefaultError | None:
    r"""Bulk update hosts

     Please be aware that when doing bulk updates, it is not possible to prevent the
    [Updating Values](\"lost update problem\"), which is normally prevented by the ETag locking
    mechanism. Use at your own risk.This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        content_type (str):  Example: application/json.
        body (BulkUpdateHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkUpdateHost,
    content_type: str,
) -> Response[Api403DefaultError | Api406DefaultError | Api415DefaultError]:
    r"""Bulk update hosts

     Please be aware that when doing bulk updates, it is not possible to prevent the
    [Updating Values](\"lost update problem\"), which is normally prevented by the ETag locking
    mechanism. Use at your own risk.This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        content_type (str):  Example: application/json.
        body (BulkUpdateHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: BulkUpdateHost,
    content_type: str,
) -> Api403DefaultError | Api406DefaultError | Api415DefaultError | None:
    r"""Bulk update hosts

     Please be aware that when doing bulk updates, it is not possible to prevent the
    [Updating Values](\"lost update problem\"), which is normally prevented by the ETag locking
    mechanism. Use at your own risk.This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        content_type (str):  Example: application/json.
        body (BulkUpdateHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
