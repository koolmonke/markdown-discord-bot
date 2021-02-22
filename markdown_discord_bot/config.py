import os

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

# noinspection SpellCheckingInspection
EXTS = {'bib', 'for', 'sublime-menu', 'xrl', 'c-objdump', 'njs', 'rabl', 'vshader', 'psc1', 'mak', 'pri', 'tsx', 'volt',
        'gco', 'wsgi', 'abap', 'bzl', 'plt', 'scrbl', 'php', 'nse', 'wiki', 'sch', '4th', 'p6m', 'cdf',
        'sublime_session', 'txt', 'geojson', 'hrl', 'flux', '9', 'psm1', 'prefab', 'rbxs', 'po', 'nb', 'cljs.hl', 'red',
        'mdpolicy', 'frg', 'hx', 'go', 'vrx', '3in', 'pike', 'prefs', 'vssettings', 'mediawiki', 'rbw', 'krl', 'io',
        'capnp', 'sublime-macro', 'tex', 'ru', 'asmx', 'ditaval', 'vcl', 'js', 'ceylon', 'rpy', 'p', 'mkii', 'clw',
        'fish', 'b', 'gnu', 'nbp', 'dcl', 'eliom', 'vsh', 'psc', 'rhtml', 'ads', 'hats', 'coffee', 'dpr', 'matlab',
        'lasso8', 'ss', 'reek', 'gms', 'es6', 'desktop.in', 'plsql', 'mkiv', 'jsm', 'json5', 'xojo_menu', 'sml', 'pxd',
        'gemspec', 'cljscm', 'nit', 'emacs.desktop', 'sp', 'unity', 'mspec', 'xsjs', 'xqy', 'ex', 'csv', '4', 'rg',
        'scd', 'xml.dist', 'wsf', 'dll.config', 'urdf', 'hlsl', 'dlm', 'mirah', 'cson', 'h++', 'aw', 'mu', 'dart',
        'monkey', 'xlf', 'ma', 'lol', 'nut', 'xs', 'duby', 'ftl', 'rest.txt', 'rkt', 'scpt', 'mcr', 'xquery', 'pyt',
        'cps', 'smt2', 'maxpat', 'rktd', 'cls', 'vbs', 'sublime-theme', 'wxi', 'gawk', 'lean', 'ino', 'cpp-objdump',
        'plist', 'emberscript', 'boot', 'omgrofl', 'mako', 'ipf', 'yml', 'auk', 'tool', 'lgt', 'darcspatch', 'irbrc',
        'als', 'maxhelp', 'htm', 'cbx', 'mt', 'ascx', 'xc', 'mata', 'xproj', 'ck', 'dats', 'axi', 'sty', 'dot', 'gcode',
        'ninja', 'xproc', 'f77', 'mao', 'dotsettings', 'asp', 'thor', 'lua', 'xojo_window', 'rake', 'ik', 'ihlp',
        'yaml', 'qml', 'gd', 'el', 'sc', 'awk', 'numpy', 'logtalk', 'ML', 'metal', 'jss', 'props', 'pbi', 'maxproj',
        'hy', 'desktop', 'yaml-tmlanguage', 'weechatlog', 'ebuild', 'gs', 'zcml', 'cmake.in', 'glslv', 'c', 'lsl',
        'rst.txt', 'jbuilder', 'fs', '7', 'nsh', 'sbt', 'oxygene', 'n', 'thy', 'vert', 'fth', 'podspec', '_js', 'jscad',
        'agda', 'sagews', 'stTheme', 'numpyw', 'dyalog', 'hxsl', 'cljx', 'pir', 'sublime-keymap', 'mtml', 'less', 'xml',
        'watchr', 'rbtbar', 'py', 'mkd', 'fpp', 'ld', 'al', 'uno', 'mawk', 'pm6', 'osm', '8', 'feature', 'apl', 'di',
        'cc', 'wlt', 'f', 'fsx', 'zimpl', 'sqf', 'tcl', 'rb', 'ahkl', 'fsproj', 'sps', 'jl', 'xacro', 'anim', 'swift',
        '3m', 'nix', 'gyp', 'sublime-settings', 'sparql', 'j', 'cpy', 'pmod', 'pd', 'lex', 'vala', 'glsl', 'ps',
        'sublime-project', 'nu', 'elm', 'ash', 'pb', 'bsv', 'xtend', 'sj', 'pl', 'gst', 'cljc', 'zpl', 'tmPreferences',
        'xojo_report', 'dita', 'bat', 'kid', 'kit', 'xi', 'arc', 'epj', 'gshader', 'exs', 'yrl', 'sci', 'fsh', 'muf',
        'shader', 'fxh', 'eclass', 'cproject', 'gap', 'factor', 'sats', 'tmCommand', 'aux', 'tml', 'apacheconf',
        'lookml', 'sig', 'pyx', 'uc', 'rest', 'gsx', 'pac', 'djs', 'php4', 'geo', 'ct', 'fp', 'ec', 'x3d', 'ado',
        'pd_lua', 'pks', 'nasm', 'ui', 'plx', 'druby', 'prw', 'dtx', 'meta', 'r3', 'hic', '6pm', 'upc', 'ooc', 'ktm',
        'st', 'arpa', '5', 'lid', 'json', 'hsc', 'rs.in', 'ada', 'jsx', 'nc', 'srdf', 'styl', 'plot', 'gvy', 'nim',
        'xojo_toolbar', 'cp', 'd', 'eps', 'inl', 'rbfrm', 'filters', 'bbx', 'launch', 'rbx', 'opa', 'pod', 'moon',
        'xib', 'ipp', 'l', 'wxl', 'rdoc', 'xpy', 'ccp', 'robot', 'ston', 'sv', 'sl', 'axd', 'cl', 'xsp-config', 'gml',
        'cfg', 'dfm', 'jsb', 'ant', 'y', 'lbx', 'au3', 'mkfile', 'p6', 'golo', 'sh.in', 'grace', 'command', 'coq',
        'bas', 'mli', 'wxs', 'txl', 'hb', 'proto', 'ur', 'tac', 'vhost', 'rst', 'ampl', 'clj', 'jsproj', 'udf', 'pyw',
        'v', 'jsp', 'eh', 'vxml', 'targets', 'jelly', 'sublime-build', 'cfml', 'nimrod', 'cats', 'fshader', 'rktl',
        'jake', 'mkdn', 'glf', 'lfe', 'm', 'hqf', 'mask', 'iss', 'ron', 'sexp', 'nlogo', 'xhtml', 'erb', 'll', 'cy',
        'lslp', 'm4', 'properties', 'mm', 'scad', 'frx', 'glade', 'smali', 'vapi', 'vark', 'scss', 'pkb', 'wl', 'sls',
        'fsi', 'nsi', 'ncl', 'plb', 'pde', 'erl', 'f90', 'xqm', 'aug', 'ins', 'c++-objdump', 'xsd', 'handlebars', 'tm',
        'cljs', 'grt', 'tpp', 'sublime-snippet', 'rno', 'idr', 'ijs', 'pasm', 'jade', 'hlsli', 'hs', 'rviz', 'apib',
        'bb', 'sas', 'lhs', 'mxml', 'cobol', 'adb', 'i7x', 'html', 'graphql', 'iml', 'com', 'nawk', 'litcoffee', 'jsfl',
        'idc', 't', 'gsp', 'lagda', 'hh', 'dyl', 'las', 'pt', 'toc', 'mmk', 'vbproj', 'tf', 'sublime-mousemap', 'sass',
        'cu', 'cbl', 'groovy', 'gnuplot', 'ini', 'bmx', 'axs.erb', 'patch', 'e', 'vim', 'veo', 'md', 'nuspec', 'hbs',
        'a51', 'slim', 'vhi', 'viw', 'pwn', 'tmSnippet', 'brd', 'as', 'ashx', 'ddl', 'rmd', 'decls', 'rd', 'me', 'shen',
        'psgi', '_ls', 'kts', 'xojo_code', 'vhs', 'mk', 'oxh', 'applescript', 'clixml', 'mir', 'pub', 'kt', 'p6l',
        'pkl', '1in', 'sthlp', 'ivy', 'r2', 'eam.fs', 'fxml', 'asc', 'kml', 'd-objdump', 'gradle', 'fan', 'sage',
        'http', 'lmi', 'cl2', 'mkvi', 'lds', 'rbuild', 'ltx', 'ldml', 'fancypack', 'lsp', 'click', 'forth', 'db2',
        'mat', 'tea', 'prc', 'odd', 'fy', 'rebol', 'fr', 'dm', 'tst', 'oz', 'h', 'gp', 'org', 'es', 'qbs', 'icl', 'sld',
        'roff', 'parrot', 'pl6', 'bones', 'sh-session', 'chs', 's', '3x', 'cpp', 'purs', 'php3', 'mod', 'csh', 'pas',
        'vb', 'ny', 'java', 'cirru', 'creole', 'ch', 'axs', 'ahk', 'tcc', 'yap', 'frm', 'pat', 'asciidoc', 'ux', 'rl',
        'storyboard', 'lisp', 'vht', 'erb.deface', 'rbbas', 'mll', 'bro', 'dpatch', 'xsp.metadata', 'css', 'ts', 'pls',
        'dockerfile', 'pony', 'lidr', 'mss', 'gv', 'ps1', 'cshtml', 'pm', 'minid', '3', 'cmake', 'ox', 'tab', 'iced',
        'x10', 'brs', 'rs', 'g4', 'sublime-workspace', 'fcgi', 'php5', 'ttl', 'cuh', 'fun', 'ni', 'vh', 'webidl',
        'syntax', 'asm', 'tu', 'pot', 'eliomi', 'urs', 'pro', 'doh', 'pov', 'scm', 'cql', 'ipynb', 'topojson', 'scxml',
        'csl', 'irclog', 'ctp', 'ditamap', 'yy', 'pck', 'f08', 'pan', 'lpr', 'ruby', 'numsc', 'reds', 'cs', 'phps',
        'aj', 'nqp', 'perl', 'bison', 'pp', 'moo', 'cjsx', 'pxi', 'lasso', 'hlean', 'scaml', 'opencl', 'cxx', 'vhdl',
        'hcl', 'zmpl', 'emacs', 'sh', 'jq', 'tmTheme', 'fx', 'wisp', 'svh', 'vcxproj', 'owl', 'kicad_pcb', 'twig',
        'god', 'escript', 'mms', 'do', 'myt', 'zone', 'csproj', 'xojo_script', 'geom', 'ml', 'latte', '1', 'cfm', 'sjs',
        'mxt', 'asset', 'scala', 'diff', 'textile', 'bash', 'ps1xml', 'sublime-completions', 'xmi', 'prg', '1x', 'frag',
        'r', 'axml', 'gf', 'hxx', 'sublime-syntax', 'mumps', 'psd1', 'rbmnu', 'self', 'aspx', 'svg', 'gi', 'flex',
        'ily', 'cfc', 'markdown', 'ml4', 'jinja', 'xslt', 'podsl', 'em', 'inc', 'sma', 'asax', 'xht', 'ssjs', 'cake',
        'sublime_metrics', 'xul', 'g', 'objdump', 'no', 'ms', 'wsdl', 'vue', 'rbres', 'builder', 'grxml', 'eclxml',
        'cob', 'cppobjdump', 'html.hl', 'xql', 'cw', 'lvproj', 'tmux', 'vhf', 'man', 'dylan', 'jsonld', 'rsh',
        'c++objdump', 'yang', 'vhd', 'csx', '1m', 'liquid', 'mo', 'bats', 'ly', 'xsjslib', 'matah', '6pl', 'ls',
        'phtml', 'phpt', 'sublime-commands', 'pogo', 'nginxconf', 'adp', 'raw', 'nproj', 'spin', 'w', 'asd', 'adoc',
        'mly', 'mkdown', 'vho', 'rdf', 'haml.deface', 'xsl', 'lock', 'eex', 'lasso9', 'xpl', 'rbuistate', 'nl',
        'thrift', 'sce', 'stan', 'hpp', 'f95', 'pyde', 'f03', 'E', 'chpl', 'mustache', 'pyp', 'rq', 'opal', 'intr', '6',
        'ksh', 'cmd', 'haml', 'jflex', 'smt', 'edn', '3qt', '_coffee', 'bf', 'yacc', 'vhw', 'wlua', 'gtpl', 'cgi',
        'zep', '2', 'tmLanguage', 'pluginspec', 'vbhtml', 'raml', 'pytb', 'cxx-objdump', 'sql', 'mathematica', 'clp',
        'vba', 'boo', 'frt', 'toml', 'ph', 'befunge', 'xq', 'cr', 'x', 'ccxml', 'xm', 'axi.erb', 'c++', 'rss', 'prolog',
        'xliff', 'tpl', 'ecl', 'xaml', 'reb', 'oxo', 'pig', 'tcsh', 'rsx', 'zsh'}
