# Python Checkmk REST API client

Created from builtin openapi spec (available at `<checkmk-host>/<site-name>/check_mk/api/1.0/openapi-swagger-ui.yaml`) using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Usage Example

* Authenticate
* Start Discovery (default mode: refresh = FIX_ALL)
* Apply pending changes


```python
from checkmk_rest_python.api.activate_changes import (
    cmk_gui_openapi_endpoints_activate_changes_activate_changes as activate,
)
from checkmk_rest_python.api.activate_changes import (
    cmk_gui_openapi_endpoints_activate_changes_list_pending_changes as list_pending,
)
from checkmk_rest_python.api.service_discovery import (
    cmk_gui_openapi_endpoints_service_discovery_execute_service_discovery as execute_discovery,
)
from checkmk_rest_python.api.service_discovery import (
    cmk_gui_openapi_endpoints_service_discovery_service_discovery_run_wait_for_completion as wait_discovery,
)
from checkmk_rest_python.client import AuthenticatedClient
from checkmk_rest_python.models.activate_changes import ActivateChanges
from checkmk_rest_python.models.discover_services import DiscoverServices


def main():
    client = AuthenticatedClient(
        base_url="<url>",
        token="<user> <token>",
    )
    
    discover = execute_discovery.sync_detailed(
        client=client,
        body=DiscoverServices(host_name="<host>"),
        content_type="application/json",
    )
    
    wait_discovery.sync_detailed(host_name="<host>", client=client)
    
    pending = list_pending.sync_detailed(client=client)
    
    # etag is messed up currently as stringed string
    # like '"..........-gzip"' with '-gzip' suffix
    
    etag = pending.headers.get("ETag", "").strip('"').rstrip("-gzip")
    
    activate = activate.sync_detailed(
        client=client,
        body=ActivateChanges(redirect=False, force_foreign_changes=False),
        if_match=etag,
        content_type="application/json",
    )


main()
```

Also works async:

```python
import asyncio


async def main():
    client = AuthenticatedClient(
        base_url="<url>",
        token="<user> <token>",
    )

    discover = await execute_discovery.asyncio_detailed(
        client=client,
        body=DiscoverServices(host_name="<host>"),
        content_type="application/json",
    )

    await wait_discovery.asyncio_detailed(host_name="<host>", client=client)

    pending = await list_pending.asyncio_detailed(client=client)

    etag = pending.headers.get("ETag", "").strip('"').rstrip("-gzip")

    result = await activate.asyncio_detailed(
        client=client,
        body=ActivateChanges(redirect=False, force_foreign_changes=False),
        if_match=etag,
        content_type="application/json",
    )


asyncio.run(main())
```
