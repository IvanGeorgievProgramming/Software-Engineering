import nox

@nox.session(name = "SHw1", python=["3.11.2"])
def tests(session):
    session.install("pytest")
    session.install("pandas")
    session.run("pytest", "-v", "tests.py")
    session.run("python", "main.py")