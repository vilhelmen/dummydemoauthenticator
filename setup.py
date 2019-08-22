from setuptools import setup, find_packages

setup(
    name='jupyterhub-demoauthenticator',
    version='0.1',
    install_requires=[
        'jupyterhub>=1.0',
    ],
    python_requires='>=3.5',
    description='JupyterHub Demo Spawner',
    url='https://github.com/vilhelmen/demoauthenticator',
    packages=find_packages(),
)
