from gleam_builtins import Error, Ok, GleamPanic


def rescue_error(f):
    try:
        return Ok(f())
    except GleamPanic as e:
        info = e.args[0] if e.args else None
        if isinstance(info, dict) and "message" in info:
            return Error(info["message"])
        return Error(str(e))
