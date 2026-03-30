from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.audit_log_entry_collection import AuditLogEntryCollection
from ...models.cmk_gui_openapi_endpoints_audit_log_get_all_object_type import (
    CmkGuiOpenapiEndpointsAuditLogGetAllObjectType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    object_type: CmkGuiOpenapiEndpointsAuditLogGetAllObjectType
    | Unset = CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL,
    object_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    date: str,
    regexp: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_object_type: str | Unset = UNSET
    if not isinstance(object_type, Unset):
        json_object_type = object_type.value

    params["object_type"] = json_object_type

    params["object_id"] = object_id

    params["user_id"] = user_id

    params["date"] = date

    params["regexp"] = regexp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/audit_log/collections/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
    | None
):
    if response.status_code == 200:
        response_200 = AuditLogEntryCollection.from_dict(response.json())

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
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
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
    object_type: CmkGuiOpenapiEndpointsAuditLogGetAllObjectType
    | Unset = CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL,
    object_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    date: str,
    regexp: str | Unset = UNSET,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
]:
    """Get all audit log entries



    This endpoint requires the following permissions:
     * `wato.auditlog`: Access to the historic audit log. The currently pending changes can be seen by
    all users with access to Setup.

    Args:
        object_type (CmkGuiOpenapiEndpointsAuditLogGetAllObjectType | Unset):  Default:
            CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL. Example: Folder.
        object_id (str | Unset):  Example: host_01.
        user_id (str | Unset):  Example: my_admin_user.
        date (str):  Example: 2017-07-21.
        regexp (str | Unset):  Example: ^l.*m.*p.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | AuditLogEntryCollection]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
        date=date,
        regexp=regexp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    object_type: CmkGuiOpenapiEndpointsAuditLogGetAllObjectType
    | Unset = CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL,
    object_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    date: str,
    regexp: str | Unset = UNSET,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
    | None
):
    """Get all audit log entries



    This endpoint requires the following permissions:
     * `wato.auditlog`: Access to the historic audit log. The currently pending changes can be seen by
    all users with access to Setup.

    Args:
        object_type (CmkGuiOpenapiEndpointsAuditLogGetAllObjectType | Unset):  Default:
            CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL. Example: Folder.
        object_id (str | Unset):  Example: host_01.
        user_id (str | Unset):  Example: my_admin_user.
        date (str):  Example: 2017-07-21.
        regexp (str | Unset):  Example: ^l.*m.*p.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | AuditLogEntryCollection
    """

    return sync_detailed(
        client=client,
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
        date=date,
        regexp=regexp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    object_type: CmkGuiOpenapiEndpointsAuditLogGetAllObjectType
    | Unset = CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL,
    object_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    date: str,
    regexp: str | Unset = UNSET,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
]:
    """Get all audit log entries



    This endpoint requires the following permissions:
     * `wato.auditlog`: Access to the historic audit log. The currently pending changes can be seen by
    all users with access to Setup.

    Args:
        object_type (CmkGuiOpenapiEndpointsAuditLogGetAllObjectType | Unset):  Default:
            CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL. Example: Folder.
        object_id (str | Unset):  Example: host_01.
        user_id (str | Unset):  Example: my_admin_user.
        date (str):  Example: 2017-07-21.
        regexp (str | Unset):  Example: ^l.*m.*p.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api406DefaultError | AuditLogEntryCollection]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        user_id=user_id,
        date=date,
        regexp=regexp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    object_type: CmkGuiOpenapiEndpointsAuditLogGetAllObjectType
    | Unset = CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL,
    object_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    date: str,
    regexp: str | Unset = UNSET,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api406DefaultError
    | AuditLogEntryCollection
    | None
):
    """Get all audit log entries



    This endpoint requires the following permissions:
     * `wato.auditlog`: Access to the historic audit log. The currently pending changes can be seen by
    all users with access to Setup.

    Args:
        object_type (CmkGuiOpenapiEndpointsAuditLogGetAllObjectType | Unset):  Default:
            CmkGuiOpenapiEndpointsAuditLogGetAllObjectType.ALL. Example: Folder.
        object_id (str | Unset):  Example: host_01.
        user_id (str | Unset):  Example: my_admin_user.
        date (str):  Example: 2017-07-21.
        regexp (str | Unset):  Example: ^l.*m.*p.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api406DefaultError | AuditLogEntryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            object_type=object_type,
            object_id=object_id,
            user_id=user_id,
            date=date,
            regexp=regexp,
        )
    ).parsed
