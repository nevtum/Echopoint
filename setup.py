from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Echopoint',
      version='0.2.1',
      description = 'A lightweight pub-sub library.',
      long_description = readme(),
      classifiers = [
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
      ],
      keywords = 'pub sub event sourcing es',
      url = 'https://github.com/nevtum/Echopoint.git',
      author = 'Neville Tummon',
      author_email = 'nt.devs@gmail.com',
      license = 'Apache License 2.0',
      packages = ['echopoint']
)
