from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.via_host_group import ViaHostGroup
from ...models.via_host_query import ViaHostQuery
from ...models.via_service_group import ViaServiceGroup
from ...models.via_service_query import ViaServiceQuery
from ...models.via_specific_host import ViaSpecificHost
from ...models.via_specific_service import ViaSpecificService
from ...types import Response


def _get_kwargs(
    *,
    body: ViaHostGroup
    | ViaHostQuery
    | ViaServiceGroup
    | ViaServiceQuery
    | ViaSpecificHost
    | ViaSpecificService,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/acknowledge/actions/delete/invoke",
    }

    if isinstance(body, ViaSpecificHost):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, ViaHostGroup):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, ViaHostQuery):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, ViaSpecificService):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, ViaServiceGroup):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

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
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ViaHostGroup
    | ViaHostQuery
    | ViaServiceGroup
    | ViaServiceQuery
    | ViaSpecificHost
    | ViaSpecificService,
    content_type: str,
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    """Remove acknowledgement on host or service problems.



    This endpoint requires the following permissions:
     * `action.acknowledge`: Acknowledge host and service problems and remove acknowledgements

    Args:
        content_type (str):  Example: application/json.
        body (ViaHostGroup | ViaHostQuery | ViaServiceGroup | ViaServiceQuery | ViaSpecificHost |
            ViaSpecificService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: ViaHostGroup
    | ViaHostQuery
    | ViaServiceGroup
    | ViaServiceQuery
    | ViaSpecificHost
    | ViaSpecificService,
    content_type: str,
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    """Remove acknowledgement on host or service problems.



    This endpoint requires the following permissions:
     * `action.acknowledge`: Acknowledge host and service problems and remove acknowledgements

    Args:
        content_type (str):  Example: application/json.
        body (ViaHostGroup | ViaHostQuery | ViaServiceGroup | ViaServiceQuery | ViaSpecificHost |
            ViaSpecificService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ViaHostGroup
    | ViaHostQuery
    | ViaServiceGroup
    | ViaServiceQuery
    | ViaSpecificHost
    | ViaSpecificService,
    content_type: str,
) -> Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]:
    """Remove acknowledgement on host or service problems.



    This endpoint requires the following permissions:
     * `action.acknowledge`: Acknowledge host and service problems and remove acknowledgements

    Args:
        content_type (str):  Example: application/json.
        body (ViaHostGroup | ViaHostQuery | ViaServiceGroup | ViaServiceQuery | ViaSpecificHost |
            ViaSpecificService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api406DefaultError | Api415DefaultError]
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
    body: ViaHostGroup
    | ViaHostQuery
    | ViaServiceGroup
    | ViaServiceQuery
    | ViaSpecificHost
    | ViaSpecificService,
    content_type: str,
) -> Any | Api400DefaultError | Api406DefaultError | Api415DefaultError | None:
    """Remove acknowledgement on host or service problems.



    This endpoint requires the following permissions:
     * `action.acknowledge`: Acknowledge host and service problems and remove acknowledgements

    Args:
        content_type (str):  Example: application/json.
        body (ViaHostGroup | ViaHostQuery | ViaServiceGroup | ViaServiceQuery | ViaSpecificHost |
            ViaSpecificService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
