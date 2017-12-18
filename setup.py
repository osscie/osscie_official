from setuptools import setup, find_packages

cfg = dict(
    name             = 'osscie_official',
    version          = '1.0.0',
    description      = (
        'Official django package of Osscie.com'
    ),
    packages         = find_packages(),
    zip_safe         = False,
    include_package_data = True,
    install_requires = [
        'requests'
    ]
)

if __name__ == '__main__':
    setup(**cfg)
