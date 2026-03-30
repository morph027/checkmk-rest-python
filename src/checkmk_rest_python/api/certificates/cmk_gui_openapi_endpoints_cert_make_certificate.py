from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_custom_error_2 import Api403CustomError2
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.x509_req_pemuuid import X509ReqPEMUUID
from ...models.x509pem import X509PEM
from ...types import Response


def _get_kwargs(
    *,
    body: X509ReqPEMUUID,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/csr",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
    | None
):
    if response.status_code == 200:
        response_200 = X509PEM.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403CustomError2.from_dict(response.json())

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
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
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
    body: X509ReqPEMUUID,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
]:
    """X.509 PEM-encoded Certificate Signing Requests (CSRs)



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Args:
        content_type (str):  Example: application/json.
        body (X509ReqPEMUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403CustomError2 | Api406DefaultError | Api415DefaultError | X509PEM]
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
    body: X509ReqPEMUUID,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
    | None
):
    """X.509 PEM-encoded Certificate Signing Requests (CSRs)



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Args:
        content_type (str):  Example: application/json.
        body (X509ReqPEMUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403CustomError2 | Api406DefaultError | Api415DefaultError | X509PEM
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: X509ReqPEMUUID,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
]:
    """X.509 PEM-encoded Certificate Signing Requests (CSRs)



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Args:
        content_type (str):  Example: application/json.
        body (X509ReqPEMUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403CustomError2 | Api406DefaultError | Api415DefaultError | X509PEM]
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
    body: X509ReqPEMUUID,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403CustomError2
    | Api406DefaultError
    | Api415DefaultError
    | X509PEM
    | None
):
    """X.509 PEM-encoded Certificate Signing Requests (CSRs)



    This endpoint requires the following permissions:
     * `general.agent_pairing`: Only relevant for the agent controller shipped with Checkmk 2.1. Pairing
    of Checkmk agents with the monitoring site. This step establishes trust between the agent and the
    monitoring site.

    Args:
        content_type (str):  Example: application/json.
        body (X509ReqPEMUUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403CustomError2 | Api406DefaultError | Api415DefaultError | X509PEM
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
