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
          "pytest",
          "requests",
          "requests-oauthlib",
          "PyMySQL",
          "WooCommerce",
      ]
      )