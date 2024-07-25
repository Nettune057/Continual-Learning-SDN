from setuptools import setup, find_packages

setup(
    name='Continual-Learning-SDN',                 # Replace with your project's name
    version='0.1.0',                     # Replace with your project's version
    author='Thanh Tung Nguyen',                  # Replace with your name
    author_email='nettune057@example.com',  # Replace with your email address
    description='Apply Continual Learning in Software-Defined Network Environment',
    long_description=open('README.md').read(),  # Detailed description (read from README)
    long_description_content_type='text/markdown',  # Format of long description
    url='https://github.com/Nettune057/Continual-Learning-SDN',  # URL to the project repository
    packages=find_packages(),            # Automatically find and include all packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',  # Specify compatible Python versions
        'License :: OSI Approved :: MIT License',  # Specify license type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',             # Specify Python version requirements
    install_requires=[
        # List your project dependencies here
        'numpy>=1.18.5',
        'pandas>=1.1.0',
        'scikit-learn>=0.23.0',
        'torch --index-url https://download.pytorch.org/whl/cu121',
        'torchvision --index-url https://download.pytorch.org/whl/cu121',
        'torchaudio --index-url https://download.pytorch.org/whl/cu121'
        # Add any additional dependencies required by your project
    ],
    extras_require={
        'dev': [
            'pytest>=3.7',
            'black',
            # Add development dependencies here
        ],
    },
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',  # Add command-line scripts if needed
        ],
    },
    include_package_data=True,            # Include files specified in MANIFEST.in
    package_data={
        '': ['*.txt', '*.rst'],            # Include additional files in the package
    },
    zip_safe=False,
)
