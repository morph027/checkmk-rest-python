from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_openapi_endpoints_configuration_entity_get_configuration_entity_form_spec_schema_entity_type import (
    CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
)
from ...types import UNSET, Response


def _get_kwargs(
    entity_type: CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
    *,
    entity_type_specifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["entity_type_specifier"] = entity_type_specifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/form_spec/collections/{entity_type}".format(
            entity_type=quote(str(entity_type), safe=""),
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
    entity_type: CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
    *,
    client: AuthenticatedClient | Client,
    entity_type_specifier: str,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Get a configuration entity form spec schema

    Args:
        entity_type
            (CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType):
            Example: notification_parameter.
        entity_type_specifier (str):  Example: mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_type_specifier=entity_type_specifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_type: CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
    *,
    client: AuthenticatedClient | Client,
    entity_type_specifier: str,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Get a configuration entity form spec schema

    Args:
        entity_type
            (CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType):
            Example: notification_parameter.
        entity_type_specifier (str):  Example: mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        entity_type=entity_type,
        client=client,
        entity_type_specifier=entity_type_specifier,
    ).parsed


async def asyncio_detailed(
    entity_type: CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
    *,
    client: AuthenticatedClient | Client,
    entity_type_specifier: str,
) -> Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]:
    """Get a configuration entity form spec schema

    Args:
        entity_type
            (CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType):
            Example: notification_parameter.
        entity_type_specifier (str):  Example: mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_type_specifier=entity_type_specifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_type: CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType,
    *,
    client: AuthenticatedClient | Client,
    entity_type_specifier: str,
) -> Api400DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Get a configuration entity form spec schema

    Args:
        entity_type
            (CmkGuiOpenapiEndpointsConfigurationEntityGetConfigurationEntityFormSpecSchemaEntityType):
            Example: notification_parameter.
        entity_type_specifier (str):  Example: mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            entity_type=entity_type,
            client=client,
            entity_type_specifier=entity_type_specifier,
        )
    ).parsed
