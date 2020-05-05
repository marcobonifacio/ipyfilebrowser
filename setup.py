import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ipyfilebrowser',
    version='0.1.0',
    author='Marco Bonifacio',
    author_email='bonifacio.marco@gmail.com',
    description='A file browser widget for Jupyter / Jupyterlab based on ipywidgets.VBox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mbonix/ipyfilebrowser',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'ipywidgets'
    ],
)
