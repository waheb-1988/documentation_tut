Mermaid Diagram Example
=======================

Here is an example of a simple flowchart using Mermaid syntax:

.. mermaid::

    graph LR
        A[Start] --> B{Is it working?}
        B -->|Yes| C[Continue]
        B -->|No| D[Fix it]
        D --> B
        C --> E[End]