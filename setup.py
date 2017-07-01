from setuptools import setup

version = "0.1.0"

setup(name="quickrun",
      packages=["quickrun"],
      version=version,
      description="Quickly run SLURM jobs",
      author='Matthew Hartley',
      author_email="matthew.hartley@jic.ac.uk",
      install_requires=[
          "pyyaml",
          "click",
          "jinja2",
      ],
      entry_points={
          'console_scripts': ['quickrun=quickrun.cli:cli']
      },
      license="MIT")
