from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent: str | Unset = UNSET,
    recursive: bool | Unset = False,
    show_hosts: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["parent"] = parent

    params["recursive"] = recursive

    params["show_hosts"] = show_hosts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/folder_config/collections/all",
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
    parent: str | Unset = UNSET,
    recursive: bool | Unset = False,
    show_hosts: bool | Unset = False,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]:
    """Show all folders



    This endpoint requires the following permissions:
     * Optionally:
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        parent (str | Unset):  Example: /servers.
        recursive (bool | Unset):  Default: False.
        show_hosts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        parent=parent,
        recursive=recursive,
        show_hosts=show_hosts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent: str | Unset = UNSET,
    recursive: bool | Unset = False,
    show_hosts: bool | Unset = False,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | None:
    """Show all folders



    This endpoint requires the following permissions:
     * Optionally:
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        parent (str | Unset):  Example: /servers.
        recursive (bool | Unset):  Default: False.
        show_hosts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError
    """

    return sync_detailed(
        client=client,
        parent=parent,
        recursive=recursive,
        show_hosts=show_hosts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent: str | Unset = UNSET,
    recursive: bool | Unset = False,
    show_hosts: bool | Unset = False,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]:
    """Show all folders



    This endpoint requires the following permissions:
     * Optionally:
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        parent (str | Unset):  Example: /servers.
        recursive (bool | Unset):  Default: False.
        show_hosts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        parent=parent,
        recursive=recursive,
        show_hosts=show_hosts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent: str | Unset = UNSET,
    recursive: bool | Unset = False,
    show_hosts: bool | Unset = False,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | None:
    """Show all folders



    This endpoint requires the following permissions:
     * Optionally:
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.

    Args:
        parent (str | Unset):  Example: /servers.
        recursive (bool | Unset):  Default: False.
        show_hosts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            parent=parent,
            recursive=recursive,
            show_hosts=show_hosts,
        )
    ).parsed
