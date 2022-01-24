{
   "targets": [
      {
         'target_name': 'msgpackBinding',
         'sources': [
            'src/msgpack.cc',
         ],
         'include_dirs': [
            'deps/msgpack',
            '<!(node -e "require(\'nan\')")'
         ],
         'dependencies': [
            'deps/msgpack/msgpack.gyp:libmsgpack'
         ],
         'cflags_cc': [
               '-Wall',
               '-Ofast',
               '-flto',
               '-std=c++17',
            ],
            'cflags': [
               '-Wall',
               '-Ofast',
               '-flto',
            ],
         'cflags!': [
           '-fno-exceptions',
           '-Wno-unused-function'
         ],
         'cflags_cc!': [
           '-fno-exceptions',
           '-Wno-unused-function'
         ],
         'conditions': [
            ['OS=="mac"', {
               'configurations': {
                  'Debug': {
                     'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'WARNING_CFLAGS': ['-Wall', '-Wno-unused-function'],
                        'OTHER_CFLAGS': ['-std=c++17'],
                     }
                  },
                  'Release': {
                     'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'WARNING_CFLAGS': ['-Wall', '-Wno-unused-function'],
                        'OTHER_CFLAGS': ['-std=c++17'],
                     },
                  },
               },
            }],
            ['OS=="win"', {
               'configurations': {
                  'Debug': {
                     'msvs_settings': {
                        'VCCLCompilerTool': {
                           'CompileAs': '2',
                           'ExceptionHandling': '1',
                        },
                     },
                  },
                  'Release': {
                     'msvs_settings': {
                        'VCCLCompilerTool': {
                           'CompileAs': '2',
                           'ExceptionHandling': '1',
                        },
                     },
                  },
               },
            }]
         ]
      },
   ]
}
