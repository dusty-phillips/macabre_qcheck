from gleam_builtins import Error, Ok


def rescue_error(f):
    try:
        return Ok(f())
    except Exception as e:
        return Error(str(e))
