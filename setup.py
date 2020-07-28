from distutils.core import setup
setup(
  name = 'pySongStructure',         
  packages = ['pySongStructure'],   
  version = '0.1',      
  license='MIT',       
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'Zhi Wei Gan',                   # Type in your name
  author_email = 'zgan@mit.edu',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'librosa',
          'msaf',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
  ],
)