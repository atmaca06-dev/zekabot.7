def run_code(code):
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return {"output": exec_globals}
    except Exception as e:
        return {"error": str(e)}