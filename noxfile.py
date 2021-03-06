import functools

import nox

nox.options.reuse_existing_virtualenvs = True


def poetry_install(func):
    @functools.wraps(func)
    def wrapped_func(session: nox.session, *args, **kwargs):
        session.run("poetry", "install", external=True)

        return func(session)

    return wrapped_func


@nox.session
@poetry_install
def lint(session):
    session.run("poetry", "run", "black", "--check", "znd4", external=True)
    session.run("poetry", "run", "pylint", "znd4", external=True)


@nox.session
@poetry_install
def test(session):
    session.run("poetry", "run", "pytest", external=True)
