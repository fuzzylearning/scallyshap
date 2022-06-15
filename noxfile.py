import nox


@nox.session(python=[ "3.10.0","3.9.5"], venv_backend="venv")
def tests(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run("pytest")

@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8","black","isort")
    session.run("flake8","./scallyshap/src/feature_selector/")
    session.run("black","./scallyshap/")
    session.run("isort","./scallyshap/")
