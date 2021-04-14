from distutils.core import setup, Extension

pkg = 'Extensions.UsbFormatWizard'
setup(name='enigma2-plugin-extensions-usbformatwizard',
       version='0.1',
       license='GPLv2',
       url='https://github.com/E2OpenPlugins/e2openplugin-UsbFormatWizard',
       description='Wizard to Format Usb devices',
       long_description='Easy way to format Usb devices for Linux',
       author='meo',
       author_email='lupomeo@hotmail.com',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
      )
