from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_401_default_error import Api401DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_405_default_error import Api405DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.cmk_gui_openapi_endpoints_host_tag_group_delete_host_tag_group_mode_type_1 import (
    CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1,
)
from ...models.cmk_gui_openapi_endpoints_host_tag_group_delete_host_tag_group_mode_type_2_type_1 import (
    CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1,
)
from ...models.cmk_gui_openapi_endpoints_host_tag_group_delete_host_tag_group_mode_type_3_type_1 import (
    CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    repair: bool | Unset = False,
    mode: CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    | None
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["repair"] = repair

    json_mode: None | str | Unset
    if isinstance(mode, Unset):
        json_mode = UNSET
    elif isinstance(
        mode, CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    ):
        json_mode = mode.value
    elif isinstance(
        mode, CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    ):
        json_mode = mode.value
    elif isinstance(
        mode, CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    ):
        json_mode = mode.value
    else:
        json_mode = mode
    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/objects/host_tag_group/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Api401DefaultError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = Api405DefaultError.from_dict(response.json())

        return response_405

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
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    repair: bool | Unset = False,
    mode: CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    | None
    | Unset = UNSET,
) -> Response[
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
]:
    """Delete a host tag group



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.hosttags`: Create, remove and edit tags. Removing tags also might remove rules, so this
    permission should not be available to normal users.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        name (str):  Example: datasource.
        repair (bool | Unset):  Default: False.
        mode (CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1 | None | Unset):
            Example: delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api405DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        name=name,
        repair=repair,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    repair: bool | Unset = False,
    mode: CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    | None
    | Unset = UNSET,
) -> (
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
    | None
):
    """Delete a host tag group



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.hosttags`: Create, remove and edit tags. Removing tags also might remove rules, so this
    permission should not be available to normal users.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        name (str):  Example: datasource.
        repair (bool | Unset):  Default: False.
        mode (CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1 | None | Unset):
            Example: delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api405DefaultError | Api406DefaultError
    """

    return sync_detailed(
        name=name,
        client=client,
        repair=repair,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    repair: bool | Unset = False,
    mode: CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    | None
    | Unset = UNSET,
) -> Response[
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
]:
    """Delete a host tag group



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.hosttags`: Create, remove and edit tags. Removing tags also might remove rules, so this
    permission should not be available to normal users.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        name (str):  Example: datasource.
        repair (bool | Unset):  Default: False.
        mode (CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1 | None | Unset):
            Example: delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api405DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        name=name,
        repair=repair,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    repair: bool | Unset = False,
    mode: CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1
    | CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1
    | None
    | Unset = UNSET,
) -> (
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api405DefaultError
    | Api406DefaultError
    | None
):
    """Delete a host tag group



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.hosttags`: Create, remove and edit tags. Removing tags also might remove rules, so this
    permission should not be available to normal users.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        name (str):  Example: datasource.
        repair (bool | Unset):  Default: False.
        mode (CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType2Type1 |
            CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1 | None | Unset):
            Example: delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api405DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            repair=repair,
            mode=mode,
        )
    ).parsed
