from setuptools import setup, find_packages

setup(
    name="universal-scraper-shlok", 
    version="1.0.0",
    
    # 1. The Package Finder
    packages=find_packages(), 
    
    # 2. The Dependency Manager
    install_requires=[
        "pandas",
        "beautifulsoup4",
        "requests",
        "lxml",
        "rich"
    ],
    
    # 3. The Magic Terminal Link
    entry_points={
        "console_scripts": [
            "run-scraper=scraper.cli:main",
        ]
    }
)