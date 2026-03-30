from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_custom_error_4 import Api403CustomError4
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_405_custom_error import Api405CustomError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.connection_mode import ConnectionMode
from ...models.register_host import RegisterHost
from ...types import Response


def _get_kwargs(
    host_name: str,
    *,
    body: RegisterHost,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/host_config_internal/{host_name}/actions/register/invoke".format(
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
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
    | None
):
    if response.status_code == 200:
        response_200 = ConnectionMode.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403CustomError4.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = Api405CustomError.from_dict(response.json())

        return response_405

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
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
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
    body: RegisterHost,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
]:
    """Register an existing host, ie. link it to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `agent_registration.register_any_existing_host`: This permission allows the registration of any
    existing host.
       * `agent_registration.register_managed_existing_host`: This permission allows the registration of
    any existing host the user is a contact of.
       * All of:
         * Optionally:
           * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
         * Any of:
           * `wato.all_folders`: Without this permission, operations on folders can only be done by
    users that are members of one of the folders contact groups. This permission grants full access to
    all folders and hosts.
           * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management
    of services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (RegisterHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403CustomError4 | Api404DefaultError | Api405CustomError | Api406DefaultError | Api415DefaultError | ConnectionMode]
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
    body: RegisterHost,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
    | None
):
    """Register an existing host, ie. link it to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `agent_registration.register_any_existing_host`: This permission allows the registration of any
    existing host.
       * `agent_registration.register_managed_existing_host`: This permission allows the registration of
    any existing host the user is a contact of.
       * All of:
         * Optionally:
           * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
         * Any of:
           * `wato.all_folders`: Without this permission, operations on folders can only be done by
    users that are members of one of the folders contact groups. This permission grants full access to
    all folders and hosts.
           * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management
    of services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (RegisterHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403CustomError4 | Api404DefaultError | Api405CustomError | Api406DefaultError | Api415DefaultError | ConnectionMode
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
    body: RegisterHost,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
]:
    """Register an existing host, ie. link it to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `agent_registration.register_any_existing_host`: This permission allows the registration of any
    existing host.
       * `agent_registration.register_managed_existing_host`: This permission allows the registration of
    any existing host the user is a contact of.
       * All of:
         * Optionally:
           * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
         * Any of:
           * `wato.all_folders`: Without this permission, operations on folders can only be done by
    users that are members of one of the folders contact groups. This permission grants full access to
    all folders and hosts.
           * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management
    of services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (RegisterHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403CustomError4 | Api404DefaultError | Api405CustomError | Api406DefaultError | Api415DefaultError | ConnectionMode]
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
    body: RegisterHost,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403CustomError4
    | Api404DefaultError
    | Api405CustomError
    | Api406DefaultError
    | Api415DefaultError
    | ConnectionMode
    | None
):
    """Register an existing host, ie. link it to a UUID



    This endpoint requires the following permissions:
     * Any of:
       * `agent_registration.register_any_existing_host`: This permission allows the registration of any
    existing host.
       * `agent_registration.register_managed_existing_host`: This permission allows the registration of
    any existing host the user is a contact of.
       * All of:
         * Optionally:
           * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
         * Any of:
           * `wato.all_folders`: Without this permission, operations on folders can only be done by
    users that are members of one of the folders contact groups. This permission grants full access to
    all folders and hosts.
           * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management
    of services (inventory) there is a separate permission (see below)

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (RegisterHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403CustomError4 | Api404DefaultError | Api405CustomError | Api406DefaultError | Api415DefaultError | ConnectionMode
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
