from gleam_builtins import Error, Ok


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return Ok(f.read())
    except OSError:
        return Error(None)
