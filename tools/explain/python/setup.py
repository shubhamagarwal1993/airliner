from setuptools import setup, find_packages

setup(
    name='explain',
    version='1.0',
    author='Windhover Labs',
    author_email='evanderwerf@windhoverlabs.com',
    description='Generate structure mapping files for parsing Airliner logs.',
    url='windhoverlabs.com',
    license='3BSD-3-Clause',
    packages=find_packages(),
    install_requires=[
    ],
    package_data={
        'explain': ['ccsds_map.json']
    },
    entry_points={
        'console_scripts': [
            'elf_reader = explain.elf_reader:main',
            'explain = explain.__main__:main',
            'parse = explain.stream_parser:main'
        ]
    }
)
