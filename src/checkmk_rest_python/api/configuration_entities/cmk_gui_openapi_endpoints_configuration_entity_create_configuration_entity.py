from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.api_422_default_error import Api422DefaultError
from ...models.create_configuration_entity import CreateConfigurationEntity
from ...types import Response


def _get_kwargs(
    *,
    body: CreateConfigurationEntity,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/configuration_entity/collections/all",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | Api422DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = Api422DefaultError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError
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
    body: CreateConfigurationEntity,
    content_type: str,
) -> Response[
    Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError
]:
    """Create a configuration entity

    Args:
        content_type (str):  Example: application/json.
        body (CreateConfigurationEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError]
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
    body: CreateConfigurationEntity,
    content_type: str,
) -> (
    Api400DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | Api422DefaultError
    | None
):
    """Create a configuration entity

    Args:
        content_type (str):  Example: application/json.
        body (CreateConfigurationEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConfigurationEntity,
    content_type: str,
) -> Response[
    Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError
]:
    """Create a configuration entity

    Args:
        content_type (str):  Example: application/json.
        body (CreateConfigurationEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError]
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
    body: CreateConfigurationEntity,
    content_type: str,
) -> (
    Api400DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | Api422DefaultError
    | None
):
    """Create a configuration entity

    Args:
        content_type (str):  Example: application/json.
        body (CreateConfigurationEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError | Api415DefaultError | Api422DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
