from jinja2 import Template

# create template
template = Template('Hello, {{ name }}!')

# pass variable and render it
output = template.render(name='world')

# output the result
print(output)


