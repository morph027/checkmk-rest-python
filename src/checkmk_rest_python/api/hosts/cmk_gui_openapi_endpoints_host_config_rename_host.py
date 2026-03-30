from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_409_custom_error_1 import Api409CustomError1
from ...models.api_412_default_error import Api412DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.api_422_custom_error_3 import Api422CustomError3
from ...models.api_428_default_error import Api428DefaultError
from ...models.rename_host import RenameHost
from ...types import Response


def _get_kwargs(
    host_name: str,
    *,
    body: RenameHost,
    if_match: str,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/host_config/{host_name}/actions/rename/invoke".format(
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
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
    | None
):
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = Api409CustomError1.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = Api412DefaultError.from_dict(response.json())

        return response_412

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = Api422CustomError3.from_dict(response.json())

        return response_422

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
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
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
    body: RenameHost,
    if_match: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
]:
    """Rename a host

     This endpoint will start a background job to rename the host. Only one rename background job
    can run at a time.This endpoint requires the following permissions:
     * All of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * `wato.rename_hosts`: Rename existing hosts. Please also add the permission <i>Modify existing
    hosts</i>.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (RenameHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409CustomError1 | Api412DefaultError | Api415DefaultError | Api422CustomError3 | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        body=body,
        if_match=if_match,
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
    body: RenameHost,
    if_match: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
    | None
):
    """Rename a host

     This endpoint will start a background job to rename the host. Only one rename background job
    can run at a time.This endpoint requires the following permissions:
     * All of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * `wato.rename_hosts`: Rename existing hosts. Please also add the permission <i>Modify existing
    hosts</i>.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (RenameHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409CustomError1 | Api412DefaultError | Api415DefaultError | Api422CustomError3 | Api428DefaultError
    """

    return sync_detailed(
        host_name=host_name,
        client=client,
        body=body,
        if_match=if_match,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameHost,
    if_match: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
]:
    """Rename a host

     This endpoint will start a background job to rename the host. Only one rename background job
    can run at a time.This endpoint requires the following permissions:
     * All of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * `wato.rename_hosts`: Rename existing hosts. Please also add the permission <i>Modify existing
    hosts</i>.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (RenameHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409CustomError1 | Api412DefaultError | Api415DefaultError | Api422CustomError3 | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameHost,
    if_match: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409CustomError1
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError3
    | Api428DefaultError
    | None
):
    """Rename a host

     This endpoint will start a background job to rename the host. Only one rename background job
    can run at a time.This endpoint requires the following permissions:
     * All of:
       * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.
       * `wato.edit_hosts`: Modify the properties of existing hosts. Please note: for the management of
    services (inventory) there is a separate permission (see below)
       * `wato.rename_hosts`: Rename existing hosts. Please also add the permission <i>Modify existing
    hosts</i>.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        host_name (str):  Example: example.com.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (RenameHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409CustomError1 | Api412DefaultError | Api415DefaultError | Api422CustomError3 | Api428DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            body=body,
            if_match=if_match,
            content_type=content_type,
        )
    ).parsed
