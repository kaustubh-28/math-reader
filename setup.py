import setuptools

with open("longdescription.txt", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

try:
    setuptools.setup(
        name = 'mathreader',
        version = '0.162',
        author = 'Kaustubh Srivastava',
        author_email = 'kaustubh282.s@gmail.com',
        long_description = long_description,
        #long_description_content_type="text/markdown",
        url="https://github.com/kaustubh-28/math-reader",
        packages = setuptools.find_packages(),
        install_requires=required,
        include_package_data=True,
        python_requires='>=3.6'
    )
except Exception as e:
    pass
