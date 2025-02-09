HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" content="width=device-width, initial-scale=1">
<title>{% word %}</title>
<style type="text/css">
    body{margin:40px auto;max-width:700px;line-height:1.6;font-size:18px;color:#333;padding:0 10px}
    h1,h2,h3{line-height:1.2}
</style>
</head>
<body>

{% content %}

</body>
</html>
"""

CONFIG_TEMPLATE = """\
[dikicli]
# Location where cached entries are stored.
# default: {data_dir}
data dir = {data_dir}
# Lines longer that linewidth value will be wrapped in terminal.
# set to 0 to disable line wrapping
# default: {linewidth}
linewidth = {linewidth}
"""
