import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puggi-bot",
    version="0.4.0",
    author="Tsukiyo Alex",
    author_email="alexandros.aug@gmail.com",
    description="Welcome to Gacha Life!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TsukiyoAlex/PuggiBot",
    project_urls={
        "Issue tracker": "https://github.com/TsukiyoAlex/PuggiBot/issues",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "discord.py",
        "flask",
        "python-dotenv",
        "PyNaCl",
        "dnspython",
    ],
    python_requires='>=3.6',
)
