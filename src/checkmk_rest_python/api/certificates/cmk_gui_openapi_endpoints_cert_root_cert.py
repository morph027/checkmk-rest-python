from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_custom_error_3 import Api403CustomError3
from ...models.api_406_default_error import Api406DefaultError
from ...models.x509pem import X509PEM
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/root_cert",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api403CustomError3 | Api406DefaultError | X509PEM | None:
    if response.status_code == 200:
        response_200 = X509PEM.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Api403CustomError3.from_dict(response.json())

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
) -> Response[Api403CustomError3 | Api406DefaultError | X509PEM]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api403CustomError3 | Api406DefaultError | X509PEM]:
    """X.509 PEM-encoded root certificate



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403CustomError3 | Api406DefaultError | X509PEM]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Api403CustomError3 | Api406DefaultError | X509PEM | None:
    """X.509 PEM-encoded root certificate



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403CustomError3 | Api406DefaultError | X509PEM
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api403CustomError3 | Api406DefaultError | X509PEM]:
    """X.509 PEM-encoded root certificate



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403CustomError3 | Api406DefaultError | X509PEM]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Api403CustomError3 | Api406DefaultError | X509PEM | None:
    """X.509 PEM-encoded root certificate



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403CustomError3 | Api406DefaultError | X509PEM
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
