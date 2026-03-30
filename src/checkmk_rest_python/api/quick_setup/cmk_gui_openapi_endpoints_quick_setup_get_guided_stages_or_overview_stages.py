from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_openapi_endpoints_quick_setup_get_guided_stages_or_overview_stages_mode import (
    CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode,
)
from ...models.quick_setup_guided_response import QuickSetupGuidedResponse
from ...models.quick_setup_overview_response import QuickSetupOverviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    quick_setup_id: str,
    *,
    mode: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode
    | Unset = CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED,
    object_id: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params["object_id"] = object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/quick_setup/{quick_setup_id}".format(
            quick_setup_id=quote(str(quick_setup_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> QuickSetupGuidedResponse | QuickSetupOverviewResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_quick_setup_response_type_0 = (
                    QuickSetupGuidedResponse.from_dict(data)
                )

                return componentsschemas_quick_setup_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_quick_setup_response_type_1 = (
                QuickSetupOverviewResponse.from_dict(data)
            )

            return componentsschemas_quick_setup_response_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

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
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode
    | Unset = CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED,
    object_id: str | Unset = "",
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
]:
    """Get guided stages or overview stages

    Args:
        quick_setup_id (str):  Example: aws.
        mode (CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode | Unset):
            Default: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED.
            Example: overview.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupGuidedResponse | QuickSetupOverviewResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        mode=mode,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode
    | Unset = CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED,
    object_id: str | Unset = "",
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
    | None
):
    """Get guided stages or overview stages

    Args:
        quick_setup_id (str):  Example: aws.
        mode (CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode | Unset):
            Default: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED.
            Example: overview.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupGuidedResponse | QuickSetupOverviewResponse
    """

    return sync_detailed(
        quick_setup_id=quick_setup_id,
        client=client,
        mode=mode,
        object_id=object_id,
    ).parsed


async def asyncio_detailed(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode
    | Unset = CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED,
    object_id: str | Unset = "",
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
]:
    """Get guided stages or overview stages

    Args:
        quick_setup_id (str):  Example: aws.
        mode (CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode | Unset):
            Default: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED.
            Example: overview.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupGuidedResponse | QuickSetupOverviewResponse]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        mode=mode,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quick_setup_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode
    | Unset = CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED,
    object_id: str | Unset = "",
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupGuidedResponse
    | QuickSetupOverviewResponse
    | None
):
    """Get guided stages or overview stages

    Args:
        quick_setup_id (str):  Example: aws.
        mode (CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode | Unset):
            Default: CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode.GUIDED.
            Example: overview.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupGuidedResponse | QuickSetupOverviewResponse
    """

    return (
        await asyncio_detailed(
            quick_setup_id=quick_setup_id,
            client=client,
            mode=mode,
            object_id=object_id,
        )
    ).parsed
