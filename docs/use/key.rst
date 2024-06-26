.. _api-key:

=======
API key
=======

.. include:: /../README.rst
   :start-after: key-get-start
   :end-before: key-get-end

It is recommended to configure your API key through an environment variable, so
that it can be picked by both the :ref:`command-line client <command_line>` and
the :ref:`Python client library <api>`:

-  On Windows:

   .. code-block:: shell

        > set ZYTE_API_KEY=YOUR_API_KEY

-  On macOS and Linux:

   .. code-block:: shell

        $ export ZYTE_API_KEY=YOUR_API_KEY

Alternatively, you may pass your API key to the clients directly:

-   To pass your API key directly to the command-line client, use the
    ``--api-key`` switch:

    .. code-block:: shell

        zyte-api --api-key YOUR_API_KEY …

-   To pass your API key directly to the Python client classes, use the
    ``api_key`` parameter when creating a client object:

    .. code-block:: python

        from zyte_api import ZyteAPI

        client = ZyteAPI(api_key="YOUR_API_KEY")

    .. code-block:: python

        from zyte_api import AsyncZyteAPI

        client = AsyncZyteAPI(api_key="YOUR_API_KEY")
