from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_401_custom_error_1 import Api401CustomError1
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.link_host_uuid import LinkHostUUID
from ...types import Response


def _get_kwargs(
    host_name: str,
    *,
    body: LinkHostUUID,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/host_config_internal/{host_name}/actions/link_uuid/invoke".format(
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
    | Api401CustomError1
    | Api404DefaultError
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

    if response.status_code == 401:
        response_401 = Api401CustomError1.from_dict(response.json())

        return response_401

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
    | Api401CustomError1
    | Api404DefaultError
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
    body: LinkHostUUID,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api401CustomError1
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Link a host to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (LinkHostUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401CustomError1 | Api404DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: LinkHostUUID,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api401CustomError1
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Link a host to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (LinkHostUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401CustomError1 | Api404DefaultError | Api406DefaultError | Api415DefaultError
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
    body: LinkHostUUID,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api401CustomError1
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Link a host to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (LinkHostUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401CustomError1 | Api404DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: LinkHostUUID,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api401CustomError1
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Link a host to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (LinkHostUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401CustomError1 | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
