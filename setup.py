from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'django>=2.0',
]

testing_extras = [
    'coverage>=3.7.0',
]

setup(
    name='django-feather',
    version='0.1',
    author='Jonas Drotleff',
    author_email='j.drotleff@desk-lab.de',
    description='A simple Tag to implement Feather Icons in Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jnsdrtlf/django-feather',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ]
)