from http import HTTPStatus
from io import BytesIO
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_openapi_endpoints_agent_download_agent_os_type import (
    CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
)
from ...types import UNSET, File, Response


def _get_kwargs(
    *,
    os_type: CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_os_type = os_type.value
    params["os_type"] = json_os_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/agent/actions/download/invoke",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

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
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    os_type: CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | File]:
    """Download agents shipped with Checkmk

    Args:
        os_type (CmkGuiOpenapiEndpointsAgentDownloadAgentOsType):  Example: linux_deb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | File]
    """

    kwargs = _get_kwargs(
        os_type=os_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    os_type: CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | File | None:
    """Download agents shipped with Checkmk

    Args:
        os_type (CmkGuiOpenapiEndpointsAgentDownloadAgentOsType):  Example: linux_deb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | File
    """

    return sync_detailed(
        client=client,
        os_type=os_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    os_type: CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
) -> Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | File]:
    """Download agents shipped with Checkmk

    Args:
        os_type (CmkGuiOpenapiEndpointsAgentDownloadAgentOsType):  Example: linux_deb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | File]
    """

    kwargs = _get_kwargs(
        os_type=os_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    os_type: CmkGuiOpenapiEndpointsAgentDownloadAgentOsType,
) -> Api400DefaultError | Api403DefaultError | Api406DefaultError | File | None:
    """Download agents shipped with Checkmk

    Args:
        os_type (CmkGuiOpenapiEndpointsAgentDownloadAgentOsType):  Example: linux_deb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | File
    """

    return (
        await asyncio_detailed(
            client=client,
            os_type=os_type,
        )
    ).parsed
