from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.site_connection_request_update import SiteConnectionRequestUpdate
from ...types import Response


def _get_kwargs(
    site_id: str,
    *,
    body: SiteConnectionRequestUpdate,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/site_connection/{site_id}".format(
            site_id=quote(str(site_id), safe=""),
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
    | Api403DefaultError
    | Api404DefaultError
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
    Api400DefaultError
    | Api403DefaultError
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
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SiteConnectionRequestUpdate,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        site_id (str):  Example: prod.
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        body=body,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SiteConnectionRequestUpdate,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        site_id (str):  Example: prod.
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SiteConnectionRequestUpdate,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        site_id (str):  Example: prod.
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SiteConnectionRequestUpdate,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update a site connection



    This endpoint requires the following permissions:
     * `wato.sites`: Access to the module for managing connections to remote monitoring sites.

    Args:
        site_id (str):  Example: prod.
        content_type (str):  Example: application/json.
        body (SiteConnectionRequestUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
