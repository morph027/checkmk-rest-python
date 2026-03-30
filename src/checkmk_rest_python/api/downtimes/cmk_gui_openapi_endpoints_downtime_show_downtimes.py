from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_openapi_endpoints_downtime_show_downtimes_downtime_type import (
    CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service_description: str | Unset = UNSET,
    host_name: str | Unset = UNSET,
    downtime_type: CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType
    | Unset = CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH,
    site_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["service_description"] = service_description

    params["host_name"] = host_name

    json_downtime_type: str | Unset = UNSET
    if not isinstance(downtime_type, Unset):
        json_downtime_type = downtime_type.value

    params["downtime_type"] = json_downtime_type

    params["site_id"] = site_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/downtime/collections/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api400DefaultError | Api406DefaultError | None:
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api400DefaultError | Api406DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_description: str | Unset = UNSET,
    host_name: str | Unset = UNSET,
    downtime_type: CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType
    | Unset = CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH,
    site_id: str | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError]:
    """Show all scheduled downtimes



    This endpoint requires the following permissions:

    Args:
        service_description (str | Unset):  Example: Memory.
        host_name (str | Unset):  Example: example.com.
        downtime_type (CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType | Unset):  Default:
            CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH. Example: host.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        service_description=service_description,
        host_name=host_name,
        downtime_type=downtime_type,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    service_description: str | Unset = UNSET,
    host_name: str | Unset = UNSET,
    downtime_type: CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType
    | Unset = CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH,
    site_id: str | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | None:
    """Show all scheduled downtimes



    This endpoint requires the following permissions:

    Args:
        service_description (str | Unset):  Example: Memory.
        host_name (str | Unset):  Example: example.com.
        downtime_type (CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType | Unset):  Default:
            CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH. Example: host.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError
    """

    return sync_detailed(
        client=client,
        service_description=service_description,
        host_name=host_name,
        downtime_type=downtime_type,
        site_id=site_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_description: str | Unset = UNSET,
    host_name: str | Unset = UNSET,
    downtime_type: CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType
    | Unset = CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH,
    site_id: str | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError]:
    """Show all scheduled downtimes



    This endpoint requires the following permissions:

    Args:
        service_description (str | Unset):  Example: Memory.
        host_name (str | Unset):  Example: example.com.
        downtime_type (CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType | Unset):  Default:
            CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH. Example: host.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        service_description=service_description,
        host_name=host_name,
        downtime_type=downtime_type,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service_description: str | Unset = UNSET,
    host_name: str | Unset = UNSET,
    downtime_type: CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType
    | Unset = CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH,
    site_id: str | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | None:
    """Show all scheduled downtimes



    This endpoint requires the following permissions:

    Args:
        service_description (str | Unset):  Example: Memory.
        host_name (str | Unset):  Example: example.com.
        downtime_type (CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType | Unset):  Default:
            CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType.BOTH. Example: host.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            service_description=service_description,
            host_name=host_name,
            downtime_type=downtime_type,
            site_id=site_id,
        )
    ).parsed
