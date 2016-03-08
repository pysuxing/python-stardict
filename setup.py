from distutils.core import setup

setup(name="stardict",
      description="Python Module reading StarDict dictionaries.",
      requires=["struct", "types", "gzip"],
      provides=["stardict"],
      version="0.1",
      py_modules=["stardict"],
      author="SuXing",
      author_email="pysuxing@gmail.com")
