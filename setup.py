from setuptools import setup, find_packages

setup(
    name='sevenapps-py-easy',
    version='0.0.8',
    license='MIT',
    description="Paquete creado para optimizar mi trabajo con python unificando lo más necesitado",
    author="SevenApps Studio",
    author_email="sevenapps.studio@gmail.com",
    packages=find_packages(),
    url='https://github.com/juanjp1992/sevenapps-py-easy.git',
    install_requires=[
        'google-cloud-firestore',
        'firebase-admin'
    ]
)
