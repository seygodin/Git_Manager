from setuptools import setup, find_packages


setup(
    name="git_manager",
    version='0.1.0',
    packages=find_packages(include=['git_manager']),

    install_requires=[
        #"git_manager>=0.1.0",
    ],
    entry_points={
        "console_scripts": [
            # "명령어=패키지.모듈:함수" 형태
            "git_manager=git_manager.cli:main",
        ],
    },
    author="seungeon lee",
    description="git manager for managing git repositories",
    long_description=open("README.md", "r", encoding="utf-8").read(),
)