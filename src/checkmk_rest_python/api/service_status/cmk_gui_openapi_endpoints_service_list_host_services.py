from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.service_parameters import ServiceParameters
from ...types import Response


def _get_kwargs(
    host_name: str,
    *,
    body: ServiceParameters,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/objects/host/{host_name}/collections/services".format(
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
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

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
    Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
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
    body: ServiceParameters,
    content_type: str,
) -> Response[
    Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
]:
    """Show the monitored services of a host

     This list is filterable by various parameters.This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (ServiceParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: ServiceParameters,
    content_type: str,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Show the monitored services of a host

     This list is filterable by various parameters.This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (ServiceParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
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
    body: ServiceParameters,
    content_type: str,
) -> Response[
    Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
]:
    """Show the monitored services of a host

     This list is filterable by various parameters.This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (ServiceParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: ServiceParameters,
    content_type: str,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Show the monitored services of a host

     This list is filterable by various parameters.This endpoint requires the following permissions:

    Args:
        host_name (str):  Example: example.com.
        content_type (str):  Example: application/json.
        body (ServiceParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
