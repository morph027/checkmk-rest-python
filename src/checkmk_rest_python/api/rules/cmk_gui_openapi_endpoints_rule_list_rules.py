from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ruleset_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ruleset_name"] = ruleset_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/rule/collections/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | None:
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ruleset_name: str,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]:
    """List rules



    This endpoint requires the following permissions:
     * All of:
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        ruleset_name (str):  Example: host_groups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        ruleset_name=ruleset_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ruleset_name: str,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | None:
    """List rules



    This endpoint requires the following permissions:
     * All of:
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        ruleset_name (str):  Example: host_groups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError
    """

    return sync_detailed(
        client=client,
        ruleset_name=ruleset_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ruleset_name: str,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]:
    """List rules



    This endpoint requires the following permissions:
     * All of:
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        ruleset_name (str):  Example: host_groups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        ruleset_name=ruleset_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ruleset_name: str,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | None:
    """List rules



    This endpoint requires the following permissions:
     * All of:
       * `wato.rulesets`: Access to the module for managing Checkmk rules. Please note that a user can
    only manage rules in folders he has permissions to.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        ruleset_name (str):  Example: host_groups.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            ruleset_name=ruleset_name,
        )
    ).parsed
