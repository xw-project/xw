xw
==

xw

# Installation instructions
```
git clone https://github.com/xw-project/xw.git
mkvirtualenv -a xw xw
pip install -e .
initialize_xw_db development.ini
pserve development.ini
```

You may occasionally need to reinstall the directory to pull in any new dependencies.

Also, it may be helpful to have both
`coffee -o static/js -w coffee`
and
`scss --watch scss:static/css`
going.

I took a bunch from html5 boilerplate.
