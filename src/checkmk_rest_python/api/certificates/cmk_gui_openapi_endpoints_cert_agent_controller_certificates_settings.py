from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_controller_certificate_settings import (
    AgentControllerCertificateSettings,
)
from ...models.api_403_custom_error_1 import Api403CustomError1
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent_controller_certificates_settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError | None
):
    if response.status_code == 200:
        response_200 = AgentControllerCertificateSettings.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Api403CustomError1.from_dict(response.json())

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
) -> Response[
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError
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
) -> Response[
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError
]:
    """Show agent controller certificate settings



    This endpoint requires the following permissions:
     * Any of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.global`: Access to the module <i>Global settings</i>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError | None
):
    """Show agent controller certificate settings



    This endpoint requires the following permissions:
     * Any of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.global`: Access to the module <i>Global settings</i>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError
]:
    """Show agent controller certificate settings



    This endpoint requires the following permissions:
     * Any of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.global`: Access to the module <i>Global settings</i>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError | None
):
    """Show agent controller certificate settings



    This endpoint requires the following permissions:
     * Any of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.global`: Access to the module <i>Global settings</i>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentControllerCertificateSettings | Api403CustomError1 | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
