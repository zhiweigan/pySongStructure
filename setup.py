from distutils.core import setup
setup(
  name = 'pySongStructure',         
  packages = ['pySongStructure'],   
  version = '0.1',      
  license='MIT',       
  description = 'A high level song structure analysis library using the MSAF Library',   
  author = 'Zhi Wei Gan',                
  author_email = 'zgan@mit.edu',   
  url = 'https://github.com/zhiweigan/pySongStructure',   
  download_url = 'https://github.com/zhiweigan/pySongStructure/archive/v0.1.tar.gz',   
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[            
          'numpy',
          'librosa',
          'msaf',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',
  ],
)