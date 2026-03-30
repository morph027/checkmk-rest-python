from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import UNSET, Response


def _get_kwargs(
    downtime_id: str,
    *,
    site_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["site_id"] = site_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/downtime/{downtime_id}".format(
            downtime_id=quote(str(downtime_id), safe=""),
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
    downtime_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Show downtime



    This endpoint requires the following permissions:

    Args:
        downtime_id (str):  Example: 54.
        site_id (str):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        downtime_id=downtime_id,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    downtime_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Show downtime



    This endpoint requires the following permissions:

    Args:
        downtime_id (str):  Example: 54.
        site_id (str):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        downtime_id=downtime_id,
        client=client,
        site_id=site_id,
    ).parsed


async def asyncio_detailed(
    downtime_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Show downtime



    This endpoint requires the following permissions:

    Args:
        downtime_id (str):  Example: 54.
        site_id (str):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        downtime_id=downtime_id,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    downtime_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Show downtime



    This endpoint requires the following permissions:

    Args:
        downtime_id (str):  Example: 54.
        site_id (str):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            downtime_id=downtime_id,
            client=client,
            site_id=site_id,
        )
    ).parsed
