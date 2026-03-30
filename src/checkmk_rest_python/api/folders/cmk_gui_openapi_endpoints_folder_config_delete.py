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
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_409_default_error import Api409DefaultError
from ...models.cmk_gui_openapi_endpoints_folder_config_delete_delete_mode import (
    CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder: str,
    *,
    delete_mode: CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode
    | Unset = CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_delete_mode: str | Unset = UNSET
    if not isinstance(delete_mode, Unset):
        json_delete_mode = delete_mode.value

    params["delete_mode"] = json_delete_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/objects/folder_config/{folder}".format(
            folder=quote(str(folder), safe=""),
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
    | Api406DefaultError
    | Api409DefaultError
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

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = Api409DefaultError.from_dict(response.json())

        return response_409

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
    | Api406DefaultError
    | Api409DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode
    | Unset = CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE,
) -> Response[
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409DefaultError
]:
    """Delete a folder



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.manage_folders`: Add new folders and delete existing folders. If a folder to be deleted
    contains hosts then the permission to delete hosts is also required.
       * Optionally:
         * `wato.manage_hosts`: Add hosts to the monitoring and remove hosts from the monitoring. Please
    also add the permission <i>Modify existing hosts</i>.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        folder (str):  Example: ~my~fine~folder.
        delete_mode (CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode | Unset):  Default:
            CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE. Example: abort_on_nonempty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409DefaultError]
    """

    kwargs = _get_kwargs(
        folder=folder,
        delete_mode=delete_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode
    | Unset = CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE,
) -> (
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | None
):
    """Delete a folder



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.manage_folders`: Add new folders and delete existing folders. If a folder to be deleted
    contains hosts then the permission to delete hosts is also required.
       * Optionally:
         * `wato.manage_hosts`: Add hosts to the monitoring and remove hosts from the monitoring. Please
    also add the permission <i>Modify existing hosts</i>.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        folder (str):  Example: ~my~fine~folder.
        delete_mode (CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode | Unset):  Default:
            CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE. Example: abort_on_nonempty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409DefaultError
    """

    return sync_detailed(
        folder=folder,
        client=client,
        delete_mode=delete_mode,
    ).parsed


async def asyncio_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode
    | Unset = CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE,
) -> Response[
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409DefaultError
]:
    """Delete a folder



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.manage_folders`: Add new folders and delete existing folders. If a folder to be deleted
    contains hosts then the permission to delete hosts is also required.
       * Optionally:
         * `wato.manage_hosts`: Add hosts to the monitoring and remove hosts from the monitoring. Please
    also add the permission <i>Modify existing hosts</i>.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        folder (str):  Example: ~my~fine~folder.
        delete_mode (CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode | Unset):  Default:
            CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE. Example: abort_on_nonempty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409DefaultError]
    """

    kwargs = _get_kwargs(
        folder=folder,
        delete_mode=delete_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode
    | Unset = CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE,
) -> (
    Any
    | Api400DefaultError
    | Api401DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api409DefaultError
    | None
):
    """Delete a folder



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.manage_folders`: Add new folders and delete existing folders. If a folder to be deleted
    contains hosts then the permission to delete hosts is also required.
       * Optionally:
         * `wato.manage_hosts`: Add hosts to the monitoring and remove hosts from the monitoring. Please
    also add the permission <i>Modify existing hosts</i>.
       * Optionally:
         * `wato.all_folders`: Without this permission, operations on folders can only be done by users
    that are members of one of the folders contact groups. This permission grants full access to all
    folders and hosts.

    Args:
        folder (str):  Example: ~my~fine~folder.
        delete_mode (CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode | Unset):  Default:
            CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode.RECURSIVE. Example: abort_on_nonempty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api409DefaultError
    """

    return (
        await asyncio_detailed(
            folder=folder,
            client=client,
            delete_mode=delete_mode,
        )
    ).parsed
