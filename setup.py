from setuptools import setup

# This file allows us to install our portfolio site as a Python package, which makes it much easier to deploy to our host later.
# The file `MANIFEST.in` in the same directory is related.

setup(
   name="portfolio_site",
   version="1.0.0",
   description='Showcase your Wagtail skills!',
   packages=["portfolio_site"],
   include_package_data=True,
   install_requires=[
        "Django>=4.2,<4.3",
        "wagtail>=5.0,<5.1",
   ],
)