from setuptools import setup, find_packages

setup(name='demoStore',
      version='1.0',
      description="Practice API testing",
      author='Jay Bae',
      author_email='jongsung.jay@gmail.com',
      url='https://github.com/jongsungbae/',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==7.1.3",
          "pytest-html==2.1.1",
          "requests==2.23.0",
          "requests-oauthlib==1.3.0",
          "PyMySQL==0.9.3",
          "WooCommerce==2.1.1",
      ]
      )
