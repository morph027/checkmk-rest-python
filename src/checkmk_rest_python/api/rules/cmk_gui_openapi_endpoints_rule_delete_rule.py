from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_custom_error import Api400CustomError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_custom_error_3 import Api404CustomError3
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs(
    rule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/objects/rule/{rule_id}".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Api400CustomError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404CustomError3.from_dict(response.json())

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
) -> Response[
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
]:
    """Delete a rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        rule_id (str):  Example: 0a168697-14a2-48d0-9c3c-ca65569a39e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400CustomError | Api403DefaultError | Api404CustomError3 | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
    | None
):
    """Delete a rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        rule_id (str):  Example: 0a168697-14a2-48d0-9c3c-ca65569a39e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400CustomError | Api403DefaultError | Api404CustomError3 | Api406DefaultError
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
]:
    """Delete a rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        rule_id (str):  Example: 0a168697-14a2-48d0-9c3c-ca65569a39e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400CustomError | Api403DefaultError | Api404CustomError3 | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | Api400CustomError
    | Api403DefaultError
    | Api404CustomError3
    | Api406DefaultError
    | None
):
    """Delete a rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        rule_id (str):  Example: 0a168697-14a2-48d0-9c3c-ca65569a39e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400CustomError | Api403DefaultError | Api404CustomError3 | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
        )
    ).parsed
