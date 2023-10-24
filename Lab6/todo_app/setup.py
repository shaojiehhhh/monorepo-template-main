from setuptools import setup, find_packages

setup(
    name='todo_app',
    version='1.0.0',
    description='A simple to-do app',
    author='Shaojie Huang',
    author_email='huang.shaoj@northeastern.edu',
    packages=find_packages(exclude=['tests']),  # Exclude 'tests' directory
    install_requires=[
        'fastapi',
        'uvicorn',
        'pytest',
        'pytest-cov',
    ],
    entry_points={
        'console_scripts': [
            'todo-app = todo_app.src:main',
        ],
    },
)
