# src/tools/data_tool.py
import traceback
from typing import Any
from langchain.tools import BaseTool

template_globals = {
    "pd": None,
    "np": None,
    "sklearn": None,
}

def _safe_exec(code: str) -> str:
    """
    Execute user code in a controlled namespace with pre-imported pandas/numpy/sklearn.
    Returns text output or error trace.
    """
    import pandas as pd
    import numpy as np
    import sklearn

    # small sandbox
    local_ns = {}
    global_ns = {"pd": pd, "np": np, "sklearn": sklearn}

    try:
        exec(code, global_ns, local_ns)
        # If user defined a variable `result`, show it. Otherwise list local vars created.
        if "result" in local_ns:
            return repr(local_ns["result"])
        else:
            # summarize objects
            keys = list(local_ns.keys())
            summary = {k: type(local_ns[k]).__name__ for k in keys}
            return f"Execution OK. Local variables: {summary}"
    except Exception as e:
        return "ERROR:\n" + traceback.format_exc()

class DataScienceTool(BaseTool):
    name = "data_science"
    description = (
        "Execute short python data-science snippets. Pre-imported: pandas as pd, numpy as np, sklearn.\n"
        "Return value: if you set `result = ...` that will be returned, otherwise a summary of variables."
    )

    def _run(self, code: str) -> str:
        return _safe_exec(code)

    async def _arun(self, code: str) -> str:
        return _safe_exec(code)
