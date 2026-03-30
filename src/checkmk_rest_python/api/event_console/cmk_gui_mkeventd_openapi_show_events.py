from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_mkeventd_openapi_show_events_phase import (
    CmkGuiMkeventdOpenapiShowEventsPhase,
)
from ...models.cmk_gui_mkeventd_openapi_show_events_state import (
    CmkGuiMkeventdOpenapiShowEventsState,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    host: str | Unset = UNSET,
    application: str | Unset = UNSET,
    state: CmkGuiMkeventdOpenapiShowEventsState | Unset = UNSET,
    phase: CmkGuiMkeventdOpenapiShowEventsPhase | Unset = UNSET,
    site_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["host"] = host

    params["application"] = application

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_phase: str | Unset = UNSET
    if not isinstance(phase, Unset):
        json_phase = phase.value

    params["phase"] = json_phase

    params["site_id"] = site_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/event_console/collections/all",
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
    host: str | Unset = UNSET,
    application: str | Unset = UNSET,
    state: CmkGuiMkeventdOpenapiShowEventsState | Unset = UNSET,
    phase: CmkGuiMkeventdOpenapiShowEventsPhase | Unset = UNSET,
    site_id: str | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError]:
    """Show events

    Args:
        host (str | Unset):  Example: host_1.
        application (str | Unset):  Example: app_1.
        state (CmkGuiMkeventdOpenapiShowEventsState | Unset):  Example: ok.
        phase (CmkGuiMkeventdOpenapiShowEventsPhase | Unset):  Example: open.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host=host,
        application=application,
        state=state,
        phase=phase,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    host: str | Unset = UNSET,
    application: str | Unset = UNSET,
    state: CmkGuiMkeventdOpenapiShowEventsState | Unset = UNSET,
    phase: CmkGuiMkeventdOpenapiShowEventsPhase | Unset = UNSET,
    site_id: str | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | None:
    """Show events

    Args:
        host (str | Unset):  Example: host_1.
        application (str | Unset):  Example: app_1.
        state (CmkGuiMkeventdOpenapiShowEventsState | Unset):  Example: ok.
        phase (CmkGuiMkeventdOpenapiShowEventsPhase | Unset):  Example: open.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError
    """

    return sync_detailed(
        client=client,
        host=host,
        application=application,
        state=state,
        phase=phase,
        site_id=site_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    host: str | Unset = UNSET,
    application: str | Unset = UNSET,
    state: CmkGuiMkeventdOpenapiShowEventsState | Unset = UNSET,
    phase: CmkGuiMkeventdOpenapiShowEventsPhase | Unset = UNSET,
    site_id: str | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError]:
    """Show events

    Args:
        host (str | Unset):  Example: host_1.
        application (str | Unset):  Example: app_1.
        state (CmkGuiMkeventdOpenapiShowEventsState | Unset):  Example: ok.
        phase (CmkGuiMkeventdOpenapiShowEventsPhase | Unset):  Example: open.
        site_id (str | Unset):  Example: mysite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host=host,
        application=application,
        state=state,
        phase=phase,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    host: str | Unset = UNSET,
    application: str | Unset = UNSET,
    state: CmkGuiMkeventdOpenapiShowEventsState | Unset = UNSET,
    phase: CmkGuiMkeventdOpenapiShowEventsPhase | Unset = UNSET,
    site_id: str | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | None:
    """Show events

    Args:
        host (str | Unset):  Example: host_1.
        application (str | Unset):  Example: app_1.
        state (CmkGuiMkeventdOpenapiShowEventsState | Unset):  Example: ok.
        phase (CmkGuiMkeventdOpenapiShowEventsPhase | Unset):  Example: open.
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
            host=host,
            application=application,
            state=state,
            phase=phase,
            site_id=site_id,
        )
    ).parsed
