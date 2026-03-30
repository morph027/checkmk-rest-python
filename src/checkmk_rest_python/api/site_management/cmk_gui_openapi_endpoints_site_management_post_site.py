from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.site_connection_request_create import SiteConnectionRequestCreate
from ...types import Response


def _get_kwargs(
    *,
    body: SiteConnectionRequestCreate,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/site_connection/collections/all",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

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
) -> Response[
    Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError
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
    body: SiteConnectionRequestCreate,
    content_type: str,
) -> Response[
    Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError
]:
    """Create a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: SiteConnectionRequestCreate,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Create a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SiteConnectionRequestCreate,
    content_type: str,
) -> Response[
    Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError
]:
    """Create a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: SiteConnectionRequestCreate,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Create a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
