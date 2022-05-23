from setuptools import setup

setup(
    name='src',
    version='0.0.1',
    author='Bappy Ahmed',
    description='To whom does your face match',
    packages=['src'],
    install_requires=['mtcnn','tensorflow','keras','pyaml','streamlit','keras-vggface','Keras-Applications','tqdm']
)