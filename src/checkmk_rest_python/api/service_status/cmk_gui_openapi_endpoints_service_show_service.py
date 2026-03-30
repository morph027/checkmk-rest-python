from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    host_name: str,
    *,
    service_description: str,
    columns: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["service_description"] = service_description

    json_columns: list[str] | Unset = UNSET
    if not isinstance(columns, Unset):
        json_columns = columns

    params["columns"] = json_columns

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/host/{host_name}/actions/show_service/invoke".format(
            host_name=quote(str(host_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

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
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
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
    service_description: str,
    columns: list[str] | Unset = UNSET,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Show a single service of a specific host



    This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        service_description (str):  Example: Filesystem /boot.
        columns (list[str] | Unset):  Example: ['state', 'state_type'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        service_description=service_description,
        columns=columns,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    service_description: str,
    columns: list[str] | Unset = UNSET,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Show a single service of a specific host



    This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        service_description (str):  Example: Filesystem /boot.
        columns (list[str] | Unset):  Example: ['state', 'state_type'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        host_name=host_name,
        client=client,
        service_description=service_description,
        columns=columns,
    ).parsed


async def asyncio_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    service_description: str,
    columns: list[str] | Unset = UNSET,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Show a single service of a specific host



    This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        service_description (str):  Example: Filesystem /boot.
        columns (list[str] | Unset):  Example: ['state', 'state_type'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
        service_description=service_description,
        columns=columns,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
    service_description: str,
    columns: list[str] | Unset = UNSET,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Show a single service of a specific host



    This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        service_description (str):  Example: Filesystem /boot.
        columns (list[str] | Unset):  Example: ['state', 'state_type'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            service_description=service_description,
            columns=columns,
        )
    ).parsed
